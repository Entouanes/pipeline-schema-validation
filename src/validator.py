import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

# Load environment variables from .env file
load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"), 
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version="2024-08-01-preview"
)

SYSTEM_MESSAGE = """
    Assistant is an intelligent chatbot designed to help validating the compliance of 
    JSON schema to the Bicep guidelines. 
    """

class Observation(BaseModel):
    violation_line: str
    description: str
    type: str

class Observations(BaseModel):
    observations: list[Observation]

def load_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def observations(
        schema: str,
        guidelines: str, 
        example_schema: str, 
        example_observation: str
    ) -> str:
    SYSTEM_MESSAGE = f"""
        You are a software architect working on a JSON schema.
        The schema must comply with the guidelines: \n{ guidelines }\n 
        Based on the guidelines, review the following JSON schema and provide feedback.
        Your task is to list all suspected violation of the guidelines. 
        All suspected violation should be based on the guidelines provided.
        """
    print(SYSTEM_MESSAGE)
    response = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": example_schema},
            {"role": "assistant", "content": f"{example_observation}"},
            {"role": "user", "content": schema},
        ],
        response_format=Observations
    )

    return response.choices[0].message.content

def validate(observations):
    # Check the observation and validate they comply with the guidelines
    validation_results = []
    for observation in observations:
        # Placeholder for actual validation logic
        validation_results.append((observation, True))  # Assuming all observations are valid
    return validation_results

def correct(observations):
    # Suggest a correction based on the guideline for each observation
    corrections = []
    for observation in observations:
        # Placeholder for actual correction logic
        corrections.append(f"Correction for {observation}")
    return corrections

def review(file_path):
    # Aggregate the results into a well structured output report
    obs = observations(file_path)
    validation_results = validate(obs)
    corrections = correct(obs)
    
    report = {
        "observations": obs,
        "validation_results": validation_results,
        "corrections": corrections
    }
    return report

# os path to the current file
curr = os.path.abspath(__file__)

# Load the JSON schema, guidelines, and example observation
schema = load_file(os.path.join(os.path.dirname(curr), "../samples/non_compliant_test.json.txt"))
guidelines = load_file(os.path.join(os.path.dirname(curr), "graph_guidelines.md"))
example_schema = load_file(os.path.join(os.path.dirname(curr), "../samples/non_compliant.json.txt"))
example_observation = load_file(os.path.join(os.path.dirname(curr), "../samples/non_compliant_explanation.json.txt"))


result = observations(
    schema=schema, 
    guidelines=guidelines, 
    example_schema=example_schema,
    example_observation=example_observation
)
print(result)
