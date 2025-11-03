# 🎯 Milestone 1 – Speech Recognition and Data Collection

## 🕐 Duration
**Weeks 1–2**

## 🎯 Objective
Collect live speech data and enable accurate speech recognition for multiple languages using Microsoft Azure Speech-to-Text.

---

## 🧱 Tasks Completed
- ✅ Set up **Azure Speech-to-Text** for real-time recognition.  
- ✅ Gathered **sample live commentary data** in English and Hindi.  
- ✅ Preprocessed collected speech data for accurate multi-language recognition.  
- ✅ Implemented initial testing script (`speech_to_text.py`).

---

## 🧰 Tools & Libraries
- `azure-cognitiveservices-speech`
- `pyaudio`
- `wave`
- `os`

---

## 📂 Code Reference
The following Python script captures live speech input and converts it to text in real-time using Azure’s Speech SDK:

```bash
python src/speech_to_text.py

For dependency installation:
pip install -r src/requirements.txt

---

## 📘 **3️⃣ evaluation.md**
```markdown
# 🧾 Evaluation Criteria – Milestone 1

## ✅ Evaluation Week: 2

### 🔹 Completion Metrics
- Successful setup and configuration of **Azure Speech-to-Text** service.
- Demonstration of **real-time speech recognition** from microphone input.
- Collection of **English and Hindi** sample audio datasets.
- Proper **data preprocessing** for multi-language support.

### 📊 Deliverables
1. Functional **speech recognition pipeline**.
2. Documented setup and configuration steps.
3. Speech data samples (if applicable).
4. Source code (`speech_to_text.py`) and dependency list (`requirements.txt`).
