import os
from openai import AzureOpenAI

# -----------------------------------------------
# Azure OpenAI Translation Script – Milestone 2
# -----------------------------------------------

def translate_text(text, target_language="fr"):
    """
    Translate text using Azure OpenAI (GPT-based) model.
    target_language examples: 'fr' (French), 'es' (Spanish), 'ta' (Tamil)
    """
    # Set environment variables or replace below with your credentials
    AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "YOUR_AZURE_OPENAI_KEY")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "YOUR_ENDPOINT_URL")
    DEPLOYMENT_NAME = "gpt-4o-mini"   # replace with your deployment name

    client = AzureOpenAI(
        api_key=AZURE_OPENAI_KEY,
        api_version="2024-08-01-preview",
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )

    prompt = f"Translate the following English text to {target_language}: {text}"

    response = client.responses.create(
        model=DEPLOYMENT_NAME,
        input=prompt
    )

    translated = response.output[0].content[0].text
    return translated

if __name__ == "__main__":
    print("🌐 Azure OpenAI Translation Demo")
    input_text = input("Enter text to translate: ")
    lang = input("Enter target language code (e.g., fr, es, ta): ")

    translated_output = translate_text(input_text, lang)
    print(f"\n🗣️ Translated Text ({lang}): {translated_output}")
