# 🏥 Healthcare Q&A Chatbot
**Powered by Google Gemini API | Python & Jupyter Notebook & Streamlit**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini_2.5_Flash-blue.svg)
![Free Tier](https://img.shields.io/badge/API-100%25_Free-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 💡 Project Background

During my time working at a hospital international clinic and a mental health therapy center, I noticed a recurring challenge: **patients often struggled to access clear, timely information about their health concerns.** This communication gap — between what patients needed to know and what was readily available — frequently led to unnecessary anxiety or delayed care.

This project is my attempt to bridge that gap using AI. By combining my background in psychology (understanding user needs) and artificial intelligence (building intelligent systems), I developed a healthcare-focused chatbot that makes medical information more accessible and less intimidating.

---

## ✨ Features

- 💬 **Real-time chat interface (Streamlit)** — **🔗 [Live Demo](https://healthcareq-achatbot-buxe4lsbwqyhxrd92n9h7c.streamlit.app)**
  <img width="1919" height="962" alt="image" src="https://github.com/user-attachments/assets/82e43589-d5ae-46ff-b3ce-ff988b76573a" />

- 🏥 **Healthcare-specialized** — system prompt tuned for medical Q&A
- 🌐 **Bilingual support** — responds in English or Korean based on user input
- 🔒 **Safety guardrails** — never diagnoses; always recommends professional consultation
- 🚨 **Emergency detection** — identifies urgent symptoms and directs to emergency services
- 📋 **Conversation export** — saves full session history to JSON

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.8+ |
| AI Model | Gemini 2.5 Flash (Google AI) |
| Interface | Streamlit UI + Jupyter Notebook |
| Key Libraries | `google-generativeai`, `python-dotenv`, `streamlit` |

---

## 📁 Project Structure

```
healthcare-chatbot/
│
├── app.py # Streamlit app
├── healthcare_chatbot.ipynb   # Main notebook
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

---

## 🤖 Model Choice: Why Gemini 2.5 Flash?

|  Gemini 2.5 Flash 
|---|---|---|
| Cost | 💚 **Free** | Paid |
| Quality | Excellent for Q&A ✅ | More nuanced |
| Best for | This chatbot | Complex reasoning |

Gemini 2.5 Flash provides excellent response quality for a healthcare Q&A use case while being completely free under the Google AI Studio free tier.

---

## ⚠️ Disclaimer

This chatbot is for **informational purposes only** and does not constitute medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns. In case of a medical emergency, call **119** (Korea) or **911** (US) immediately.

---

## 🔮 Future Improvements

- [ ] Integrate symptom checker with triage logic
- [ ] Add support for image input (e.g., skin condition photos)
- [ ] Implement RAG with verified medical knowledge base

---

## 📄 License

This project is licensed under the MIT License.
