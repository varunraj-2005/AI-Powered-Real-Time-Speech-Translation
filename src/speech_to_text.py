import azure.cognitiveservices.speech as speechsdk

def speech_to_text():
    """Real-time speech-to-text conversion using Azure Speech SDK."""
    speech_key = "YOUR_AZURE_SPEECH_KEY"
    service_region = "YOUR_REGION"  # e.g., "eastus"

    # Configure speech recognizer
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language = "en-IN"

    # Use default microphone as audio input
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("🎤 Speak into your microphone...")

    while True:
        result = recognizer.recognize_once_async().get()
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print(f"🗣️ Recognized: {result.text}")
        elif result.reason == speechsdk.ResultReason.NoMatch:
            print("❌ No speech could be recognized.")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(f"⚠️ Speech Recognition canceled: {cancellation.reason}")
            if cancellation.reason == speechsdk.CancellationReason.Error:
                print(f"Error details: {cancellation.error_details}")
            break

if __name__ == "__main__":
    speech_to_text()
