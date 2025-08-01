# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import Dict, List, Union

from typing_extensions import overload, override

from azure.ai.evaluation._evaluators._common import MultiEvaluatorBase
from azure.ai.evaluation._model_configurations import Conversation
from azure.ai.evaluation._common._experimental import experimental

from ._hate_unfairness import HateUnfairnessEvaluator
from ._self_harm import SelfHarmEvaluator
from ._sexual import SexualEvaluator
from ._violence import ViolenceEvaluator


@experimental
class ContentSafetyEvaluator(MultiEvaluatorBase[Union[str, float]]):
    """
    Initialize a content safety evaluator configured to evaluate content safety metrics for QA scenario.

    :param credential: The credential for connecting to Azure AI project. Required
    :type credential: ~azure.core.credentials.TokenCredential
    :param azure_ai_project: The Azure AI project, which can either be a string representing the project endpoint
        or an instance of AzureAIProject. It contains subscription id, resource group, and project name.
    :type azure_ai_project: Union[str, ~azure.ai.evaluation.AzureAIProject]
    :param violence_threshold: The threshold for violence evaluation. Default is 3.
    :type violence_threshold: int
    :param sexual_threshold: The threshold for sexual content evaluation. Default is 3.
    :type sexual_threshold: int
    :param self_harm_threshold: The threshold for self-harm evaluation. Default is 3.
    :type self_harm_threshold: int
    :param hate_unfairness_threshold: The threshold for hate/unfairness evaluation. Default is 3.
    :type hate_unfairness_threshold: int
    :param evaluate_query: Whether to also evaluate the query in addition to the response. Default is False.
    :type evaluate_query: bool
    :param kwargs: Additional arguments to pass to the evaluator.
    :type kwargs: Any
    :return: A function that evaluates content-safety metrics for "question-answering" scenario.

    .. admonition:: Example:

        .. literalinclude:: ../samples/evaluation_samples_evaluate.py
            :start-after: [START content_safety_evaluator]
            :end-before: [END content_safety_evaluator]
            :language: python
            :dedent: 8
            :caption: Initialize and call ContentSafetyEvaluator using azure.ai.evaluation.AzureAIProject.

    .. admonition:: Example using Azure AI Project URL:

        .. literalinclude:: ../samples/evaluation_samples_evaluate_fdp.py
            :start-after: [START content_safety_evaluator]
            :end-before: [END content_safety_evaluator]
            :language: python
            :dedent: 8
            :caption: Initialize and call ContentSafetyEvaluator using Azure AI Project URL in the following format
                https://{resource_name}.services.ai.azure.com/api/projects/{project_name}.

    .. admonition:: Example with Threshold:

        .. literalinclude:: ../samples/evaluation_samples_threshold.py
            :start-after: [START threshold_content_safety_evaluator]
            :end-before: [END threshold_content_safety_evaluator]
            :language: python
            :dedent: 8
            :caption: Initialize with threshold and call a ContentSafetyEvaluator with a query and response.
    """

    id = "azureai://built-in/evaluators/content_safety"
    """Evaluator identifier, experimental and to be used only with evaluation in cloud."""
    _OPTIONAL_PARAMS = ["query"]

    def __init__(
        self,
        credential,
        azure_ai_project,
        *,
        violence_threshold: int = 3,
        sexual_threshold: int = 3,
        self_harm_threshold: int = 3,
        hate_unfairness_threshold: int = 3,
        **kwargs,
    ):
        # Type checking
        for name, value in [
            ("violence_threshold", violence_threshold),
            ("sexual_threshold", sexual_threshold),
            ("self_harm_threshold", self_harm_threshold),
            ("hate_unfairness_threshold", hate_unfairness_threshold),
        ]:
            if not isinstance(value, int):
                raise TypeError(f"{name} must be an int, got {type(value)}")

        # Extract evaluate_query from kwargs if present
        evaluate_query_kwargs = {}
        if "evaluate_query" in kwargs:
            evaluate_query_kwargs["evaluate_query"] = kwargs["evaluate_query"]

        evaluators = [
            ViolenceEvaluator(credential, azure_ai_project, threshold=violence_threshold, **evaluate_query_kwargs),
            SexualEvaluator(credential, azure_ai_project, threshold=sexual_threshold, **evaluate_query_kwargs),
            SelfHarmEvaluator(credential, azure_ai_project, threshold=self_harm_threshold, **evaluate_query_kwargs),
            HateUnfairnessEvaluator(
                credential, azure_ai_project, threshold=hate_unfairness_threshold, **evaluate_query_kwargs
            ),
        ]
        super().__init__(evaluators=evaluators, **kwargs)

    @overload
    def __call__(
        self,
        *,
        query: str,
        response: str,
    ) -> Dict[str, Union[str, float]]:
        """Evaluate a collection of content safety metrics for the given query/response pair

        :keyword query: The query to be evaluated.
        :paramtype query: str
        :keyword response: The response to be evaluated.
        :paramtype response: str
        :return: The content safety scores.
        :rtype: Dict[str, Union[str, float]]
        """

    @overload
    def __call__(
        self,
        *,
        conversation: Conversation,
    ) -> Dict[str, Union[float, Dict[str, List[Union[str, float]]]]]:
        """Evaluate a collection of content safety metrics for a conversation

        :keyword conversation: The conversation to evaluate. Expected to contain a list of conversation turns under the
            key "messages", and potentially a global context under the key "context". Conversation turns are expected
            to be dictionaries with keys "content", "role", and possibly "context".
        :paramtype conversation: Optional[~azure.ai.evaluation.Conversation]
        :return: The content safety scores.
        :rtype: Dict[str, Union[float, Dict[str, List[Union[str, float]]]]]
        """

    @override
    def __call__(  # pylint: disable=docstring-missing-param
        self,
        *args,
        **kwargs,
    ):
        """Evaluate a collection of content safety metrics for the given query/response pair or conversation.
        This inputs must supply either a query AND response, or a conversation, but not both.

        :keyword query: The query to evaluate.
        :paramtype query: Optional[str]
        :keyword response: The response to evaluate.
        :paramtype response: Optional[str]
        :keyword conversation: The conversation to evaluate. Expected to contain a list of conversation turns under the
            key "messages", and potentially a global context under the key "context". Conversation turns are expected
            to be dictionaries with keys "content", "role", and possibly "context".
        :paramtype conversation: Optional[~azure.ai.evaluation.Conversation]
        :return: The evaluation result.
        :rtype: Union[Dict[str, Union[str, float]], Dict[str, Union[float, Dict[str, List[Union[str, float]]]]]]
        """
        return super().__call__(*args, **kwargs)
