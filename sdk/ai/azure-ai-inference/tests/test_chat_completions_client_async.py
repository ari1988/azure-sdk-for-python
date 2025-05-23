# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import os
import json
import azure.ai.inference as sdk
import azure.ai.inference.aio as async_sdk

from model_inference_test_base import (
    ModelClientTestBase,
    ServicePreparerChatCompletions,
    ServicePreparerAOAIChatCompletions,
)

from devtools_testutils.aio import recorded_by_proxy_async
from azure.core.exceptions import ServiceRequestError
from azure.core.credentials import AzureKeyCredential


# The test class name needs to start with "Test" to get collected by pytest
class TestChatCompletionsClientAsync(ModelClientTestBase):

    # **********************************************************************************
    #
    #         CHAT COMPLETIONS REGRESSION TESTS - NO SERVICE RESPONSE REQUIRED
    #
    # **********************************************************************************

    # Regression test. Send a request that includes all supported types of input objects. Make sure the resulting
    # JSON payload that goes up to the service (including headers) is the correct one after hand-inspection.
    @ServicePreparerChatCompletions()  # Not sure why this is needed. It errors out if not present. We don't use the env variables in this test.
    async def test_async_chat_completions_request_payload(self, **kwargs):

        client = async_sdk.ChatCompletionsClient(
            endpoint="http://does.not.exist",
            credential=AzureKeyCredential("key-value"),
            headers={"some_header": "some_header_value"},
            user_agent="MyAppId",
        )

        for _ in range(2):
            try:
                _ = await client.complete(
                    messages=[
                        sdk.models.SystemMessage(content="system prompt"),
                        sdk.models.UserMessage(content="user prompt 1"),
                        sdk.models.AssistantMessage(
                            tool_calls=[
                                sdk.models.ChatCompletionsToolCall(
                                    function=sdk.models.FunctionCall(
                                        name="my-first-function-name",
                                        arguments={"first_argument": "value1", "second_argument": "value2"},
                                    ),
                                    id="some-id",
                                ),
                                sdk.models.ChatCompletionsToolCall(
                                    function=sdk.models.FunctionCall(
                                        name="my-second-function-name", arguments={"first_argument": "value1"}
                                    ),
                                    id="some-other-id",
                                ),
                            ]
                        ),
                        sdk.models.ToolMessage(tool_call_id="some id", content="function response"),
                        sdk.models.AssistantMessage(content="assistant prompt"),
                        sdk.models.UserMessage(
                            content=[
                                sdk.models.TextContentItem(text="user prompt 2"),
                                sdk.models.ImageContentItem(
                                    image_url=sdk.models.ImageUrl(
                                        url="https://does.not.exit/image.png",
                                        detail=sdk.models.ImageDetailLevel.HIGH,
                                    ),
                                ),
                            ],
                        ),
                    ],
                    model_extras={
                        "key1": 1,
                        "key2": True,
                        "key3": "Some value",
                        "key4": [1, 2, 3],
                        "key5": {"key6": 2, "key7": False, "key8": "Some other value", "key9": [4, 5, 6, 7]},
                    },
                    frequency_penalty=0.123,
                    max_tokens=321,
                    model="some-model-id",
                    presence_penalty=4.567,
                    response_format="json_object",
                    seed=654,
                    stop=["stop1", "stop2"],
                    stream=True,
                    temperature=8.976,
                    tool_choice=sdk.models.ChatCompletionsToolChoicePreset.AUTO,
                    tools=[ModelClientTestBase.TOOL1, ModelClientTestBase.TOOL2],
                    top_p=9.876,
                    raw_request_hook=self.request_callback,
                )
                await client.close()
                assert False
            except ServiceRequestError as _:
                # The test should throw this exception!
                self._validate_chat_completions_json_request_payload()
                continue
        await client.close()

    # Regression test. Send a request that includes all supported types of input objects, with chat settings
    # specified in the constructor. Make sure the resulting JSON payload that goes up to the service
    # is the correct one after hand-inspection.
    @ServicePreparerChatCompletions()  # Not sure why this is needed. It errors out if not present. We don't use the env variables in this test.
    async def test_async_chat_completions_request_payload_with_defaults(self, **kwargs):

        client = async_sdk.ChatCompletionsClient(
            endpoint="http://does.not.exist",
            credential=AzureKeyCredential("key-value"),
            headers={"some_header": "some_header_value"},
            user_agent="MyAppId",
            model_extras={
                "key1": 1,
                "key2": True,
                "key3": "Some value",
                "key4": [1, 2, 3],
                "key5": {"key6": 2, "key7": False, "key8": "Some other value", "key9": [4, 5, 6, 7]},
            },
            frequency_penalty=0.123,
            max_tokens=321,
            model="some-model-id",
            presence_penalty=4.567,
            response_format="json_object",
            seed=654,
            stop=["stop1", "stop2"],
            temperature=8.976,
            tool_choice=sdk.models.ChatCompletionsToolChoicePreset.AUTO,
            tools=[ModelClientTestBase.TOOL1, ModelClientTestBase.TOOL2],
            top_p=9.876,
        )

        for _ in range(2):
            try:
                _ = await client.complete(
                    messages=[
                        sdk.models.SystemMessage("system prompt"),
                        sdk.models.UserMessage("user prompt 1"),
                        sdk.models.AssistantMessage(
                            tool_calls=[
                                sdk.models.ChatCompletionsToolCall(
                                    function=sdk.models.FunctionCall(
                                        name="my-first-function-name",
                                        arguments={"first_argument": "value1", "second_argument": "value2"},
                                    ),
                                    id="some-id",
                                ),
                                sdk.models.ChatCompletionsToolCall(
                                    function=sdk.models.FunctionCall(
                                        name="my-second-function-name", arguments={"first_argument": "value1"}
                                    ),
                                    id="some-other-id",
                                ),
                            ]
                        ),
                        sdk.models.ToolMessage("function response", tool_call_id="some id"),
                        sdk.models.AssistantMessage("assistant prompt"),
                        sdk.models.UserMessage(
                            [
                                sdk.models.TextContentItem(text="user prompt 2"),
                                sdk.models.ImageContentItem(
                                    image_url=sdk.models.ImageUrl(
                                        url="https://does.not.exit/image.png",
                                        detail=sdk.models.ImageDetailLevel.HIGH,
                                    ),
                                ),
                            ],
                        ),
                    ],
                    stream=True,
                    raw_request_hook=self.request_callback,
                )
                await client.close()
                assert False
            except ServiceRequestError as _:
                # The test should throw this exception!
                self._validate_chat_completions_json_request_payload()
                continue
        await client.close()

    # Regression test. Send a request that includes all supported types of input objects, with chat settings
    # specified in the constructor and all of them overwritten in the 'complete' call.
    # Make sure the resulting JSON payload that goes up to the service is the correct one after hand-inspection.
    @ServicePreparerChatCompletions()  # Not sure why this is needed. It errors out if not present. We don't use the env variables in this test.
    async def test_async_chat_completions_request_payload_with_defaults_and_overrides(self, **kwargs):

        client = async_sdk.ChatCompletionsClient(
            endpoint="http://does.not.exist",
            credential=AzureKeyCredential("key-value"),
            headers={"some_header": "some_header_value"},
            user_agent="MyAppId",
            model_extras={
                "key1": 2,
                "key3": False,
                "key4": "Some other value",
                "key9": "Yet another value",
            },
            frequency_penalty=0.456,
            max_tokens=768,
            model="some-other-model-id",
            presence_penalty=1.234,
            response_format="text",
            seed=987,
            stop=["stop3", "stop5"],
            temperature=5.432,
            tool_choice=sdk.models.ChatCompletionsToolChoicePreset.REQUIRED,
            tools=[ModelClientTestBase.TOOL2],
            top_p=3.456,
        )

        for _ in range(2):
            try:
                _ = await client.complete(
                    messages=[
                        sdk.models.SystemMessage(content="system prompt"),
                        sdk.models.UserMessage(content="user prompt 1"),
                        sdk.models.AssistantMessage(
                            tool_calls=[
                                sdk.models.ChatCompletionsToolCall(
                                    function=sdk.models.FunctionCall(
                                        name="my-first-function-name",
                                        arguments={"first_argument": "value1", "second_argument": "value2"},
                                    ),
                                    id="some-id",
                                ),
                                sdk.models.ChatCompletionsToolCall(
                                    function=sdk.models.FunctionCall(
                                        name="my-second-function-name", arguments={"first_argument": "value1"}
                                    ),
                                    id="some-other-id",
                                ),
                            ]
                        ),
                        sdk.models.ToolMessage(tool_call_id="some id", content="function response"),
                        sdk.models.AssistantMessage(content="assistant prompt"),
                        sdk.models.UserMessage(
                            content=[
                                sdk.models.TextContentItem(text="user prompt 2"),
                                sdk.models.ImageContentItem(
                                    image_url=sdk.models.ImageUrl(
                                        url="https://does.not.exit/image.png",
                                        detail=sdk.models.ImageDetailLevel.HIGH,
                                    ),
                                ),
                            ],
                        ),
                    ],
                    model_extras={
                        "key1": 1,
                        "key2": True,
                        "key3": "Some value",
                        "key4": [1, 2, 3],
                        "key5": {"key6": 2, "key7": False, "key8": "Some other value", "key9": [4, 5, 6, 7]},
                    },
                    frequency_penalty=0.123,
                    max_tokens=321,
                    model="some-model-id",
                    presence_penalty=4.567,
                    response_format="json_object",
                    seed=654,
                    stop=["stop1", "stop2"],
                    stream=True,
                    temperature=8.976,
                    tool_choice=sdk.models.ChatCompletionsToolChoicePreset.AUTO,
                    tools=[ModelClientTestBase.TOOL1, ModelClientTestBase.TOOL2],
                    top_p=9.876,
                    raw_request_hook=self.request_callback,
                )
                await client.close()
                assert False
            except ServiceRequestError as _:
                # The test should throw this exception!
                self._validate_chat_completions_json_request_payload()
                continue
        await client.close()

    # **********************************************************************************
    #
    #                      HAPPY PATH TESTS - CHAT COMPLETIONS
    #
    # **********************************************************************************

    @ServicePreparerChatCompletions()
    @recorded_by_proxy_async
    async def test_async_load_chat_completions_client(self, **kwargs):

        client = await self._load_async_chat_client(**kwargs)
        assert isinstance(client, async_sdk.ChatCompletionsClient)
        assert client._model_info

        response1 = await client.get_model_info()
        self._print_model_info_result(response1)
        self._validate_model_info_result(
            response1, "chat-completion"  # TODO: This should be chat_completions based on REST API spec...
        )  # TODO: This should be ModelType.CHAT_COMPLETION once the model is fixed
        await client.close()

    @ServicePreparerChatCompletions()
    @recorded_by_proxy_async
    async def test_async_get_model_info_on_chat_client(self, **kwargs):
        client = self._create_async_chat_client(**kwargs)
        assert not client._model_info  # pylint: disable=protected-access

        response1 = await client.get_model_info()
        assert client._model_info  # pylint: disable=protected-access
        self._print_model_info_result(response1)
        self._validate_model_info_result(
            response1, "chat-completion"
        )  # TODO: This should be ModelType.CHAT_COMPLETION once the model is fixed

        # Get the model info again. No network calls should be made here,
        # as the response is cached in the client.
        response2 = await client.get_model_info()
        self._print_model_info_result(response2)
        assert response1 == response2
        await client.close()

    @ServicePreparerChatCompletions()
    @recorded_by_proxy_async
    async def test_async_chat_completions_with_entra_id_auth(self, **kwargs):
        async with self._create_async_chat_client(key_auth=False, **kwargs) as client:
            messages = [
                sdk.models.SystemMessage(
                    content="You are a helpful assistant answering questions regarding length units."
                ),
                sdk.models.UserMessage(content="How many feet are in a mile?"),
            ]
            response = await client.complete(messages=messages)
            self._print_chat_completions_result(response)
            self._validate_chat_completions_result(response, ["5280", "5,280"])
            assert json.dumps(response.as_dict(), indent=2) == response.__str__()

    @ServicePreparerChatCompletions()
    @recorded_by_proxy_async
    async def test_async_chat_completions_multi_turn(self, **kwargs):
        messages = [
            sdk.models.SystemMessage(content="You are a helpful assistant answering questions regarding length units."),
            sdk.models.UserMessage(content="How many feet are in a mile?"),
        ]
        async with self._create_async_chat_client(**kwargs) as client:
            response = await client.complete(messages=messages)
            self._print_chat_completions_result(response)
            self._validate_chat_completions_result(response, ["5280", "5,280"])
            assert json.dumps(response.as_dict(), indent=2) == response.__str__()
            messages.append(sdk.models.AssistantMessage(content=response.choices[0].message.content))
            messages.append(sdk.models.UserMessage(content="and how many yards?"))
            response = await client.complete(messages=messages)
            self._print_chat_completions_result(response)
            self._validate_chat_completions_result(response, ["1760", "1,760"])

    @ServicePreparerChatCompletions()
    @recorded_by_proxy_async
    async def test_async_chat_completions_with_model_extras(self, **kwargs):
        client = self._create_async_chat_client(**kwargs)
        response = await client.complete(
            messages=[sdk.models.UserMessage(content="How many feet are in a mile?")],
            model_extras={"n": 1},
            raw_request_hook=self.request_callback,
        )
        self._print_chat_completions_result(response)
        self._validate_chat_completions_result(response, ["5280", "5,280"])
        self._validate_model_extras(self.pipeline_request.http_request.data, self.pipeline_request.http_request.headers)
        await client.close()

    @ServicePreparerChatCompletions()
    @recorded_by_proxy_async
    async def test_async_chat_completions_streaming(self, **kwargs):
        async with self._create_async_chat_client(Sync=False, **kwargs) as client:
            async with await client.complete(
                stream=True,
                messages=[
                    sdk.models.SystemMessage(content="You are a helpful assistant."),
                    sdk.models.UserMessage(content="Give me 3 good reasons why I should exercise every day."),
                ],
            ) as response:
                await self._validate_async_chat_completions_streaming_result(response)

    @ServicePreparerChatCompletions()
    @recorded_by_proxy_async
    async def test_async_chat_completions_with_json_input(self, **kwargs):
        client = self._create_async_chat_client(**kwargs)
        request_body = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "How many feet are in a mile?"},
            ]
        }
        response = await client.complete(request_body)
        self._validate_chat_completions_result(response, ["5280", "5,280"])
        await client.close()

    @ServicePreparerChatCompletions()
    @recorded_by_proxy_async
    async def test_async_chat_completions_with_bytes_input(self, **kwargs):
        client = self._create_async_chat_client(**kwargs)
        response = await client.complete(self._read_text_file("chat.test.json"))
        self._validate_chat_completions_result(response, ["5280", "5,280"])
        await client.close()

    @ServicePreparerChatCompletions()
    @recorded_by_proxy_async
    async def test_async_chat_completions_streaming_with_json_input(self, **kwargs):
        client = self._create_async_chat_client(**kwargs)
        request_body = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Give me 3 good reasons why I should exercise every day."},
            ],
            "stream": True,
        }
        response = await client.complete(request_body)
        await self._validate_async_chat_completions_streaming_result(response)
        await client.close()

    # We use AOAI endpoint here because at the moment there is no MaaS model that supports
    # input image.
    @ServicePreparerAOAIChatCompletions()
    @recorded_by_proxy_async
    async def test_async_chat_completions_with_input_image_file(self, **kwargs):
        client = self._create_async_aoai_chat_client(**kwargs)

        # Construct the full path to the image file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_file_path = os.path.join(script_dir, "test_image1.png")

        response = await client.complete(
            messages=[
                sdk.models.SystemMessage(content="You are an AI assistant that describes images in details."),
                sdk.models.UserMessage(
                    content=[
                        sdk.models.TextContentItem(text="What's in this image?"),
                        sdk.models.ImageContentItem(
                            image_url=sdk.models.ImageUrl.load(
                                image_file=image_file_path,
                                image_format="png",
                                detail=sdk.models.ImageDetailLevel.HIGH,
                            ),
                        ),
                    ],
                ),
            ],
        )
        self._print_chat_completions_result(response)
        self._validate_chat_completions_result(
            response, ["juggling", "balls", "blue", "red", "green", "yellow"], is_aoai=True
        )
        await client.close()

    # We use AOAI endpoint here because at the moment there is no MaaS model that supports
    # input image.
    @ServicePreparerAOAIChatCompletions()
    @recorded_by_proxy_async
    async def test_async_chat_completions_with_input_image_url(self, **kwargs):
        url = "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/main/sdk/ai/azure-ai-inference/tests/test_image1.png"
        client = self._create_async_aoai_chat_client(**kwargs)
        response = await client.complete(
            messages=[
                sdk.models.SystemMessage(content="You are an AI assistant that describes images in details."),
                sdk.models.UserMessage(
                    content=[
                        sdk.models.TextContentItem(text="What's in this image?"),
                        sdk.models.ImageContentItem(
                            image_url=sdk.models.ImageUrl(url=url, detail=sdk.models.ImageDetailLevel.AUTO)
                        ),
                    ],
                ),
            ],
        )
        self._print_chat_completions_result(response)
        self._validate_chat_completions_result(
            response, ["juggling", "balls", "blue", "red", "green", "yellow"], is_aoai=True
        )
        await client.close()

    # We use AOAI endpoint here because at the moment MaaS does not support Entra ID auth.
    @ServicePreparerAOAIChatCompletions()
    @recorded_by_proxy_async
    async def test_async_aoai_chat_completions_with_entra_id_auth(self, **kwargs):
        client = self._create_async_aoai_chat_client(key_auth=False, **kwargs)
        messages = [
            sdk.models.SystemMessage(content="You are a helpful assistant answering questions regarding length units."),
            sdk.models.UserMessage(content="How many feet are in a mile?"),
        ]
        response = await client.complete(messages=messages)
        self._print_chat_completions_result(response)
        self._validate_chat_completions_result(response, ["5280", "5,280"], is_aoai=True)
        await client.close()

    @ServicePreparerAOAIChatCompletions()
    @recorded_by_proxy_async
    async def test_async_aoai_chat_completions_with_structured_output(self, **kwargs):
        client = self._create_async_aoai_chat_client(key_auth=True, **kwargs)
        response_format = sdk.models.JsonSchemaFormat(
            name="Test_JSON_Schema",
            schema=ModelClientTestBase.OUTPUT_FORMAT_JSON_SCHEMA,
            description="Describes a set of distances between locations",
            strict=True,
        )
        print(type(response_format))
        messages = [
            sdk.models.SystemMessage(content="You are a helpful assistant answering questions on US geography"),
            sdk.models.UserMessage(content="What's the distance between Seattle and Portland, as the crow flies?"),
        ]
        response = await client.complete(messages=messages, response_format=response_format)
        self._print_chat_completions_result(response)
        self._validate_chat_completions_result(
            response, ["distances", "location1", "Seattle", "location2", "Portland"], is_aoai=True, is_json=True
        )
        await client.close()

    # We use AOAI endpoint here because at the moment there is no MaaS model that supports
    # input audio.
    @ServicePreparerAOAIChatCompletions()
    @recorded_by_proxy_async
    async def test_chat_completions_with_audio_input(self, **kwargs):
        client = self._create_async_aoai_audio_chat_client(**kwargs)

        # Construct the full path to the image file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        audio_file_path = os.path.join(script_dir, "hello_how_are_you.mp3")

        response = await client.complete(
            messages=[
                sdk.models.SystemMessage(
                    content="You are an AI assistant for translating and transcribing audio clips."
                ),
                sdk.models.UserMessage(
                    content=[
                        sdk.models.TextContentItem(text="Please translate this audio snippet to spanish."),
                        sdk.models.AudioContentItem(
                            input_audio=sdk.models.InputAudio.load(
                                audio_file=audio_file_path, audio_format=sdk.models.AudioContentFormat.MP3
                            )
                        ),
                    ],
                ),
            ],
        )
        self._print_chat_completions_result(response)
        self._validate_chat_completions_result(response, ["Hola", "cómo", "estás"], is_aoai=True)
        await client.close()
