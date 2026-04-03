# 🏥 Healthcare Q&A Chatbot
**Powered by Google Gemini API | Python & Jupyter Notebook**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini_1.5_Flash-blue.svg)
![Free Tier](https://img.shields.io/badge/API-100%25_Free-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 💡 Project Background

During my time working at a hospital international clinic and a mental health therapy center, I noticed a recurring challenge: **patients often struggled to access clear, timely information about their health concerns.** This communication gap — between what patients needed to know and what was readily available — frequently led to unnecessary anxiety or delayed care.

This project is my attempt to bridge that gap using AI. By combining my background in psychology (understanding user needs) and artificial intelligence (building intelligent systems), I developed a healthcare-focused chatbot that makes medical information more accessible and less intimidating.

---

## ✨ Features

- 💬 **Multi-turn conversation** — remembers context throughout the session
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
| AI Model | Gemini 1.5 Flash (Google AI) |
| Interface | Jupyter Notebook |
| Key Libraries | `google-generativeai`, `python-dotenv` |

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/healthcare-chatbot.git
cd healthcare-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get your FREE API key

This project uses the **Google Gemini API**, which offers a generous free tier — **no credit card required**.

1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Sign in with your Google account
3. Click **"Get API key"** → **"Create API key"**
4. Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

> **Free Tier Limits (Gemini 1.5 Flash):**
> - 15 requests per minute
> - 1,500 requests per day
> - 1 million tokens per minute
>
> This is more than enough for personal projects, demos, and portfolio use.

### 4. Launch the notebook
```bash
jupyter notebook healthcare_chatbot.ipynb
```

---

## 💻 Usage

### Interactive Chat
Run **Section 5** of the notebook for a live chat session.

```
👤 You: What are the symptoms of dry eye syndrome?

🏥 Assistant: Dry eye syndrome occurs when your eyes don't produce
enough tears or the right quality of tears...
```

### Available Commands
| Command | Action |
|---------|--------|
| `quit` / `exit` / `종료` | End the session |
| `reset` | Start a new conversation |
| `history` | View full chat history |
| `export` | Save conversation to JSON |

### Demo Mode
Run **Section 6** to see example Q&A without interactive input — great for testing.

---

## 📁 Project Structure

```
healthcare-chatbot/
│
├── healthcare_chatbot.ipynb   # Main notebook
├── requirements.txt           # Dependencies
├── .env                       # API key (not committed)
├── .gitignore                 # Excludes .env and outputs
└── README.md                  # This file
```

---

## 🤖 Model Choice: Why Gemini 1.5 Flash?

| | Gemini 1.5 Flash | Gemini 1.5 Pro |
|---|---|---|
| Cost | 💚 **Free** | Paid |
| Speed | ⚡ Very fast | Moderate |
| Context window | 1M tokens | 1M tokens |
| Quality | Excellent for Q&A ✅ | More nuanced |
| Best for | This chatbot | Complex reasoning |

Gemini 1.5 Flash provides excellent response quality for a healthcare Q&A use case while being completely free under the Google AI Studio free tier.

> 💡 **Want to upgrade?** Change the `model` parameter in Section 4 to `gemini-1.5-pro` for more nuanced responses.

---

## ⚠️ Disclaimer

This chatbot is for **informational purposes only** and does not constitute medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns. In case of a medical emergency, call **119** (Korea) or **911** (US) immediately.

---

## 🔮 Future Improvements

- [ ] Add vision/eye health specialization module (inspired by J&J Vision Care)
- [ ] Integrate symptom checker with triage logic
- [ ] Build web UI using Streamlit or Flask
- [ ] Add support for image input (e.g., skin condition photos)
- [ ] Implement RAG with verified medical knowledge base

---

## 📄 License

This project is licensed under the MIT License.
