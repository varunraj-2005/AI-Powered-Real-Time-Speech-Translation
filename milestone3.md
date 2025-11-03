# ⚙️ Milestone 3 – Real-Time Speech-to-Speech Integration

## 🕒 Duration
**Weeks 5 – 6**

## 🎯 Objective
Implement a **real-time speech-to-speech translation pipeline** that connects the
speech-recognition (Milestone 1) and translation (Milestone 2) modules, producing
translated audio output in the target language with minimal latency.

---

## 🧱 Tasks Completed
- ✅ Combined `speech_to_text.py` + `translate_model.py` into one real-time pipeline.  
- ✅ Integrated Azure **Text-to-Speech (TTS)** for spoken output.  
- ✅ Achieved near real-time streaming between modules.  
- ✅ Validated end-to-end latency and translation quality.

---

## 🧰 Tools & Libraries
- `azure-cognitiveservices-speech` (for STT + TTS)  
- `openai` (for Azure OpenAI translation)  
- `time`, `asyncio`, `pyaudio`

---

## 🔄 Workflow
