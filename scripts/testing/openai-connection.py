import openai

# Hardcoded variables
AZURE_OPENAI_API_KEY = "1e604d8d229e43acaf964e049892cc3c"
AZURE_OPENAI_ENDPOINT = "https://erasmusbot-tom-claes.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT_NAME = "erasmubot-open-ai"

openai.api_key = AZURE_OPENAI_API_KEY
openai.api_base = AZURE_OPENAI_ENDPOINT

def test_openai_api():
    try:
        response = openai.Completion.create(
            engine=AZURE_OPENAI_DEPLOYMENT_NAME,
            prompt="Test prompt",
            max_tokens=50
        )
        print(response.choices[0].text.strip())
    except Exception as e:
        print(f"Error: {e}")

test_openai_api()
