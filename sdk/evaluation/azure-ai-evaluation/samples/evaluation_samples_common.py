# coding: utf-8
# type: ignore

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
DESCRIPTION:
    These samples demonstrate usage of various classes and methods commonly used in the azure-ai-evaluation library.

USAGE:
    python evaluation_samples_common.py
"""


class EvaluationCommonSamples(object):
    def evaluation_common_classes_methods(self):
        # [START create_AOAI_model_config]
        from azure.ai.evaluation._model_configurations import AzureOpenAIModelConfiguration

        model_config = AzureOpenAIModelConfiguration(
            azure_endpoint="https://abcdefghijklmnopqrstuvwxyz.api.cognitive.microsoft.com",
            api_key="my-aoai-api-key",
            api_version="2024-04-01-preview",
            azure_deployment="my-aoai-deployment-name",
        )

        # [END create_AOAI_model_config]

        # [START create_OAI_model_config]
        from azure.ai.evaluation._model_configurations import OpenAIModelConfiguration

        oai_model_config = OpenAIModelConfiguration(
            api_key="my-oai-api-key", base_url="https://api.openai.com/v1", model="gpt-35-turbo"
        )

        # [END create_OAI_model_config]

        # [START create_azure_ai_project_object]
        from azure.ai.evaluation._model_configurations import AzureAIProject

        project = AzureAIProject(
            subscription_id="my-subscription-id",
            resource_group_name="my-resource-group-name",
            project_name="my-project-name",
        )

        # [END create_azure_ai_project_object]

        # [START python_grader_example]
        from azure.ai.evaluation import AzureOpenAIPythonGrader, evaluate
        from azure.ai.evaluation._model_configurations import AzureOpenAIModelConfiguration
        import os

        # Configure your Azure OpenAI connection
        model_config = AzureOpenAIModelConfiguration(
            azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
            api_key=os.environ["AZURE_OPENAI_API_KEY"],
            api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            azure_deployment=os.environ["MODEL_DEPLOYMENT_NAME"],
        )

        # Create a Python grader with custom evaluation logic
        python_grader = AzureOpenAIPythonGrader(
            model_config=model_config,
            name="custom_accuracy",
            image_tag="2025-05-08",
            pass_threshold=0.8,  # 80% threshold for passing
            source="""
        def grade(sample: dict, item: dict) -> float:
            \"\"\"
            Custom grading logic that compares model output to expected label.
            
            Args:
                sample: Dictionary that is typically empty in Azure AI Evaluation
                item: Dictionary containing ALL the data including model output and ground truth
            
            Returns:
                Float score between 0.0 and 1.0
            \"\"\"
            # Important: In Azure AI Evaluation, all data is in 'item', not 'sample'
            # The 'sample' parameter is typically an empty dictionary
            
            # Get the model's response/output from item
            output = item.get("response", "") or item.get("output", "") or item.get("output_text", "")
            output = output.lower()
            
            # Get the expected label/ground truth from item
            label = item.get("ground_truth", "") or item.get("label", "") or item.get("expected", "")
            label = label.lower()
            
            # Handle empty cases
            if not output or not label:
                return 0.0
            
            # Exact match gets full score
            if output == label:
                return 1.0
            
            # Partial match logic (customize as needed)
            if output in label or label in output:
                return 0.5
            
            return 0.0
        """,
        )

        # Run evaluation
        evaluation_result = evaluate(
            data="evaluation_data.jsonl",  # JSONL file with columns: query, response, ground_truth, etc.
            evaluators={"custom_accuracy": python_grader},
        )

        # Access results
        print(f"Pass rate: {evaluation_result['metrics']['custom_accuracy.pass_rate']}")
        # [END python_grader_example]


if __name__ == "__main__":
    print("Loading samples in evaluation_samples_common.py")
    sample = EvaluationCommonSamples()
    print("Samples loaded successfully!")
    print("Running samples in evaluation_samples_common.py")
    sample.evaluation_common_classes_methods()
    print("Samples ran successfully!")
