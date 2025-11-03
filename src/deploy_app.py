"""
Milestone 4 – Deployment API for Real-Time Translation
This FastAPI app exposes a REST endpoint for text translation.
"""

from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import AzureOpenAI
import os

app = FastAPI(title="AI Speech Translation API", version="1.0")

# ---------- CONFIGURATION ----------
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "YOUR_AZURE_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "YOUR_ENDPOINT")
DEPLOYMENT_NAME = "gpt-4o-mini"  # Replace with your Azure model deployment

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-08-01-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

# ---------- INPUT MODEL ----------
class TranslationRequest(BaseModel):
    text: str
    target_lang: str

# ---------- ROUTES ----------
@app.get("/")
def home():
    return {"message": "AI Translation API is running 🚀"}

@app.post("/translate")
def translate_text(req: TranslationRequest):
    prompt = f"Translate this text to {req.target_lang}: {req.text}"
    response = client.responses.create(model=DEPLOYMENT_NAME, input=prompt)
    translation = response.output[0].content[0].text.strip()

    return {"translated_text": translation, "status": "success"}

# ---------- RUN LOCALLY ----------
# Run locally: uvicorn src.deploy_app:app --reload
