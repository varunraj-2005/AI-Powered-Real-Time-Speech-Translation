"""
Real-Time Speech-to-Speech Translation Pipeline – Milestone 3
Requires: Azure Speech SDK + Azure OpenAI
"""

import os
import time
import azure.cognitiveservices.speech as speechsdk
from openai import AzureOpenAI

# ---------- CONFIGURATION ----------
SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY", "YOUR_AZURE_SPEECH_KEY")
SERVICE_REGION = os.getenv("AZURE_SERVICE_REGION", "YOUR_REGION")
OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY", "YOUR_OPENAI_KEY")
OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "YOUR_ENDPOINT")
DEPLOYMENT_NAME = "gpt-4o-mini"   # replace with your deployment name

# ---------- INITIALISE CLIENTS ----------
speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)
speech_config.speech_recognition_language = "en-IN"
translation_client = AzureOpenAI(api_key=OPENAI_KEY,
                                 api_version="2024-08-01-preview",
                                 azure_endpoint=OPENAI_ENDPOINT)

# ---------- TRANSLATION FUNCTION ----------
def translate_text(text, target_lang="fr"):
    prompt = f"Translate the following English text to {target_lang}: {text}"
    response = translation_client.responses.create(model=DEPLOYMENT_NAME, input=prompt)
    return response.output[0].content[0].text.strip()

# ---------- TEXT-TO-SPEECH FUNCTION ----------
def speak_text(text, lang_code="fr-FR"):
    tts_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION)
    tts_config.speech_synthesis_language = lang_code
    tts_audio = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=tts_config, audio_config=tts_audio)
    synthesizer.speak_text_async(text)

# ---------- MAIN LOOP ----------
def run_pipeline():
    print("🎧 Speak something in English — translating and speaking back...")
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    while True:
        print("\n🎤 Listening...")
        result = recognizer.recognize_once_async().get()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            original = result.text
            print(f"🗣️ Recognised: {original}")

            translated = translate_text(original, target_lang="es")  # Spanish
            print(f"🌐 Translated: {translated}")

            speak_text(translated, lang_code="es-ES")
            time.sleep(0.5)
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("❌ No speech detected.")
        elif result.reason == speechsdk.ResultReason.Canceled:
            print("⚠️ Translation cancelled.")
            break

if __name__ == "__main__":
    run_pipeline()
