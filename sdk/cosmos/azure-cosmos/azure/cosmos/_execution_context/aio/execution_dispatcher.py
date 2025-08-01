# The MIT License (MIT)
# Copyright (c) 2021 Microsoft Corporation

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Internal class for proxy query execution context implementation in the Azure
Cosmos database service.
"""

import os
from azure.cosmos._execution_context.aio import endpoint_component, multi_execution_aggregator
from azure.cosmos._execution_context.aio import non_streaming_order_by_aggregator, hybrid_search_aggregator
from azure.cosmos._execution_context.aio.base_execution_context import _QueryExecutionContextBase
from azure.cosmos._execution_context.aio.base_execution_context import _DefaultQueryExecutionContext
from azure.cosmos._execution_context.execution_dispatcher import _is_partitioned_execution_info,\
    _is_hybrid_search_query, _verify_valid_hybrid_search_query
from azure.cosmos._execution_context.query_execution_info import _PartitionedQueryExecutionInfo
from azure.cosmos.documents import _DistinctType
from azure.cosmos.exceptions import CosmosHttpResponseError
from azure.cosmos.http_constants import StatusCodes
from ..._constants import _Constants as Constants

# pylint: disable=protected-access

class _ProxyQueryExecutionContext(_QueryExecutionContextBase):  # pylint: disable=abstract-method
    """Represents a proxy execution context wrapper.

    By default, uses _DefaultQueryExecutionContext.

    If backend responds a 400 error code with a Query Execution Info, switches
    to _MultiExecutionContextAggregator
    """

    def __init__(self, client, resource_link, query, options, fetch_function,
                 response_hook, raw_response_hook, resource_type):
        """
        Constructor
        """
        super(_ProxyQueryExecutionContext, self).__init__(client, options)

        self._execution_context = _DefaultQueryExecutionContext(client, options, fetch_function)
        self._resource_link = resource_link
        self._query = query
        self._fetch_function = fetch_function
        self._resource_type = resource_type
        self._response_hook = response_hook
        self._raw_response_hook = raw_response_hook
        self._fetched_query_plan = False

    async def _create_execution_context_with_query_plan(self):
        self._fetched_query_plan = True
        query_to_use = self._query if self._query is not None else "Select * from root r"
        query_execution_info = _PartitionedQueryExecutionInfo(await self._client._GetQueryPlanThroughGateway
        (query_to_use, self._resource_link, self._options.get('excludedLocations')))
        self._execution_context = await self._create_pipelined_execution_context(query_execution_info)

    async def __anext__(self):
        """Returns the next query result.

        :return: The next query result.
        :rtype: dict
        :raises StopIteration: If no more result is left.

        """
        try:
            return await self._execution_context.__anext__()
        except CosmosHttpResponseError as e:
            if _is_partitioned_execution_info(e) or _is_hybrid_search_query(self._query, e):
                await self._create_execution_context_with_query_plan()
            else:
                raise e

        return await self._execution_context.__anext__()

    async def fetch_next_block(self):
        """Returns a block of results.

        This method only exists for backward compatibility reasons. (Because
        QueryIterable has exposed fetch_next_block api).

        :return: List of results.
        :rtype: list
        """
        try:
            return await self._execution_context.fetch_next_block()
        except CosmosHttpResponseError as e:
            if _is_partitioned_execution_info(e) or _is_hybrid_search_query(self._query, e):
                await self._create_execution_context_with_query_plan()
            else:
                raise e

        return await self._execution_context.fetch_next_block()

    async def _create_pipelined_execution_context(self, query_execution_info):

        assert self._resource_link, "code bug, resource_link is required."
        if query_execution_info.has_aggregates() and not query_execution_info.has_select_value():
            if self._options and ("enableCrossPartitionQuery" in self._options
                                  and self._options["enableCrossPartitionQuery"]):
                raise CosmosHttpResponseError(StatusCodes.BAD_REQUEST,
                                  "Cross partition query only supports 'VALUE <AggregateFunc>' for aggregates")

        # throw exception here for vector search query without limit filter or limit > max_limit
        if query_execution_info.get_non_streaming_order_by():
            total_item_buffer = (query_execution_info.get_top() or 0) or \
                                ((query_execution_info.get_limit() or 0) + (query_execution_info.get_offset() or 0))
            if total_item_buffer == 0:
                raise ValueError("Executing a vector search query without TOP or LIMIT can consume many" +
                                 " RUs very fast and have long runtimes. Please ensure you are using one" +
                                 " of the two filters with your vector search query.")
            if total_item_buffer > int(os.environ.get(Constants.MAX_ITEM_BUFFER_VS_CONFIG,
                                                      Constants.MAX_ITEM_BUFFER_VS_CONFIG_DEFAULT)):
                raise ValueError("Executing a vector search query with more items than the max is not allowed. " +
                                 "Please ensure you are using a limit smaller than the max, or change the max.")
            execution_context_aggregator =\
                non_streaming_order_by_aggregator._NonStreamingOrderByContextAggregator(self._client,
                                                                                        self._resource_link,
                                                                                        self._query,
                                                                                        self._options,
                                                                                        query_execution_info,
                                                                                        self._response_hook,
                                                                                        self._raw_response_hook)
            await execution_context_aggregator._configure_partition_ranges()
        elif query_execution_info.has_hybrid_search_query_info():
            hybrid_search_query_info = query_execution_info._query_execution_info['hybridSearchQueryInfo']
            _verify_valid_hybrid_search_query(hybrid_search_query_info)
            execution_context_aggregator = \
                hybrid_search_aggregator._HybridSearchContextAggregator(self._client,
                                                                        self._resource_link,
                                                                        self._options,
                                                                        query_execution_info,
                                                                        hybrid_search_query_info,
                                                                        self._response_hook,
                                                                        self._raw_response_hook)
            await execution_context_aggregator._run_hybrid_search()
        else:
            execution_context_aggregator = multi_execution_aggregator._MultiExecutionContextAggregator(
                self._client, self._resource_link, self._query, self._options, query_execution_info,
                self._response_hook, self._raw_response_hook)
            await execution_context_aggregator._configure_partition_ranges()
        return _PipelineExecutionContext(self._client, self._options, execution_context_aggregator,
                                         query_execution_info)


class _PipelineExecutionContext(_QueryExecutionContextBase):  # pylint: disable=abstract-method

    DEFAULT_PAGE_SIZE = 1000

    def __init__(self, client, options, execution_context, query_execution_info):
        super(_PipelineExecutionContext, self).__init__(client, options)

        if options.get("maxItemCount"):
            self._page_size = options["maxItemCount"]
        else:
            self._page_size = _PipelineExecutionContext.DEFAULT_PAGE_SIZE

        self._execution_context = execution_context

        self._endpoint = endpoint_component._QueryExecutionEndpointComponent(execution_context)

        order_by = query_execution_info.get_order_by()
        if query_execution_info.get_non_streaming_order_by():
            self._endpoint = endpoint_component._QueryExecutionNonStreamingEndpointComponent(self._endpoint)
        elif order_by:
            self._endpoint = endpoint_component._QueryExecutionOrderByEndpointComponent(self._endpoint)

        aggregates = query_execution_info.get_aggregates()
        if aggregates:
            self._endpoint = endpoint_component._QueryExecutionAggregateEndpointComponent(self._endpoint, aggregates)

        distinct_type = query_execution_info.get_distinct_type()
        if distinct_type != _DistinctType.NoneType:
            if distinct_type == _DistinctType.Ordered:
                self._endpoint = endpoint_component._QueryExecutionDistinctOrderedEndpointComponent(self._endpoint)
            else:
                self._endpoint = endpoint_component._QueryExecutionDistinctUnorderedEndpointComponent(self._endpoint)

        offset = query_execution_info.get_offset()
        if offset is not None:
            self._endpoint = endpoint_component._QueryExecutionOffsetEndpointComponent(self._endpoint, offset)

        top = query_execution_info.get_top()
        if top is not None:
            self._endpoint = endpoint_component._QueryExecutionTopEndpointComponent(self._endpoint, top)

        limit = query_execution_info.get_limit()
        if limit is not None:
            self._endpoint = endpoint_component._QueryExecutionTopEndpointComponent(self._endpoint, limit)

    async def __anext__(self):
        """Returns the next query result.

        :return: The next query result.
        :rtype: dict
        :raises StopIteration: If no more result is left.
        """
        return await self._endpoint.__anext__()

    async def fetch_next_block(self):
        """Returns a block of results.

        This method only exists for backward compatibility reasons. (Because
        QueryIterable has exposed fetch_next_block api).

        This method internally invokes next() as many times required to collect
        the requested fetch size.

        :return: List of results.
        :rtype: list
        """

        results = []
        for _ in range(self._page_size):
            try:
                results.append(await self.__anext__())
            except StopAsyncIteration:
                # no more results
                break
        return results
