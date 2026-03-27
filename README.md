# 🏥 Healthcare Q&A Chatbot
**Powered by Anthropic Claude API | Python & Jupyter Notebook**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude_API-blueviolet.svg)
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
| AI Model | Claude (Anthropic API) |
| Interface | Jupyter Notebook |
| Key Libraries | `anthropic`, `python-dotenv` |

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

### 3. Set up your API key
Create a `.env` file in the project root:
```
ANTHROPIC_API_KEY=your_api_key_here
```
> Get your API key at [console.anthropic.com](https://console.anthropic.com)

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

