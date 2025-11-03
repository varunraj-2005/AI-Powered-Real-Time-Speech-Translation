# 🧩 Milestone 2 – Translation Model Development and Training

## 🕒 Duration
**Weeks 3–4**

## 🎯 Objective
Develop and train machine learning models for **real-time speech-to-speech translation** using **Azure OpenAI Service** to convert recognised speech into 12 + languages.

---

## 🧱 Tasks Completed
- ✅ Selected and configured **Azure OpenAI Translation API** (GPT or custom model).  
- ✅ Implemented text translation pipeline from recognised speech text.  
- ✅ Trained and evaluated translation accuracy using BLEU score and latency metrics.  
- ✅ Integrated translation stage with Milestone 1 speech-recognition output.

---

## 🧰 Tools & Libraries
- `openai` (Azure OpenAI SDK)  
- `googletrans` *(optional backup)*  
- `azure-cognitiveservices-speech` *(for continuity)*  
- `pandas`, `numpy` *(for data handling)*  

---

## ⚙️ Integration Flow
1. Speech recognised by `speech_to_text.py`  
2. Text passed to `translate_model.py`  
3. Translation generated in selected target language  
4. Output displayed or stored for future TTS conversion  

---

## 📂 Code Reference
To translate recognised text:
```bash
python src/translate_model.py
