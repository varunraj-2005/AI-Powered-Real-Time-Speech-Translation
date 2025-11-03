# 🚀 Milestone 4 – Deployment and Embedding into OTT Platform

## 🕒 Duration
**Weeks 7–8**

## 🎯 Objective
Deploy the **real-time speech translation system** to a production-ready environment
and embed it within OTT (Over-The-Top) media platforms for seamless multilingual user experience.

---

## 🧱 Tasks Completed
- ✅ Packaged and containerised the full project for deployment.  
- ✅ Built a **FastAPI-based backend service** for speech translation.  
- ✅ Deployed the API on **Azure App Service / Azure Container Instances**.  
- ✅ Embedded the translation stream into an OTT player prototype (frontend or API integration).  

---

## 🧰 Tools & Technologies
- **FastAPI** – for API hosting  
- **Azure App Service / Azure Container Instances** – for cloud deployment  
- **Azure OpenAI & Speech SDK** – translation pipeline  
- **HTML5 Audio / JS player** – OTT integration  

---

## ⚙️ Deployment Workflow


---

## 🧩 Steps for Deployment
1. **Containerise** the app (optional):
   ```bash
   docker build -t ai-translation-app .
   docker run -p 8000:8000 ai-translation-app

az webapp up --name ai-translation-api --resource-group myResourceGroup --sku B1
https://ai-translation-api.azurewebsites.net/translate

curl -X POST "https://ai-translation-api.azurewebsites.net/translate" \
     -H "Content-Type: application/json" \
     -d '{"text": "Welcome to the match!", "target_lang": "hi"}'
{
  "translated_text": "मैच में आपका स्वागत है!",
  "status": "success"
}

