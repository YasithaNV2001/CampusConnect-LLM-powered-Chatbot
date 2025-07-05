# CampusConnect – LLM-powered Academic Assistant Chatbot

## 🧠 Project Overview

CampusConnect is an AI-powered academic assistant chatbot designed to help university students get quick, intelligent responses related to their academic life. It leverages OpenAI's GPT models to provide contextual responses. This project was implemented using Python, Streamlit, and OpenAI APIs.

## 🚀 Features

* Interactive chatbot powered by GPT (OpenAI API)
* Academic-focused conversational assistant
* Streamlit-based frontend UI

## 🏗️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **AI Model**: OpenAI GPT-3.5 Turbo / GPT-4
* **Deployment**: Streamlit Cloud (final)

## 📝 Deployment Attempts

### 1. ⚠️ Azure App Service (FAILED)

Initially, I attempted to deploy this chatbot on **Azure App Service** under the free tier using Python runtime. Although the build and GitHub Action workflows succeeded, the app **failed to load properly in the browser**, showing:

```
:( Application Error
If you are the application administrator, you can access the diagnostic resources.
```

Common troubleshooting included:

* Missing `OPENAI_API_KEY` environment variable
* Incorrect file path/module imports
* `streamlit_app.py` not accessible from the root for Azure
* `os` module not imported (NameError)

Despite attempts to fix these, the app continued showing a blank error page.

### 2. ✅ Streamlit Cloud (SUCCESS)

Finally, the project was successfully deployed using **Streamlit Cloud** with the following steps:

* Chat history added using `st.session_state`
* Submit button added to handle queries instead of auto-triggering
* `.env` file used for API key (handled as Streamlit secret)
* Clean folder structure: `app/streamlit_app.py`, `app/chatbot_backend.py`

Live App: [https://campusconnect-llm-powered-chatbot.streamlit.app](https://campusconnect-llm-powered-chatbot.streamlit.app)

## 📂 Folder Structure

```
campusconnect-llm-chatbot/
├── app/
│   ├── streamlit_app.py        # Main Streamlit UI
│   ├── chatbot_backend.py      # Logic for OpenAI chat
├── requirements.txt
├── .env                        # Contains OPENAI_API_KEY
├── README.md
```

## 📦 Requirements

```txt
openai>=1.0.0
streamlit
python-dotenv
```

## 📌 Lessons Learned

* Azure App Service requires proper entry point configuration and environment variables
* Streamlit Cloud is much simpler for rapid deployment of Python apps
* Always test local `.env` usage with fallback or error handling

---

🔗 GitHub: [github.com/YasithaNV2001/CampusConnect-LLM-powered-Chatbot](https://github.com/YasithaNV2001/CampusConnect-LLM-powered-Chatbot)
