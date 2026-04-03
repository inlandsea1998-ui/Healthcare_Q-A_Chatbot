import streamlit as st
import google.genai as genai
import os
from datetime import datetime
import json

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Healthcare Q&A Chatbot",
    page_icon="🏥",
    layout="centered",
)

# ── Custom CSS ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display&display=swap');

/* Global */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Hide default Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 760px; }

/* ── Header ── */
.app-header {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    border-bottom: 1px solid #e8ede8;
    margin-bottom: 1.5rem;
}
.app-header h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 2.2rem;
    color: #1a3a2a;
    margin: 0 0 0.3rem;
    letter-spacing: -0.5px;
}
.app-header .subtitle {
    color: #6b8f71;
    font-size: 0.95rem;
    font-weight: 400;
    margin: 0;
}
.app-header .badge {
    display: inline-block;
    background: #e8f5e9;
    color: #2e7d32;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    margin-top: 0.6rem;
    letter-spacing: 0.5px;
}

/* ── Chat messages ── */
.chat-wrapper {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-bottom: 1rem;
}

.msg-row {
    display: flex;
    align-items: flex-end;
    gap: 0.6rem;
}
.msg-row.user { flex-direction: row-reverse; }

.avatar {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
}
.avatar.bot  { background: #1a3a2a; }
.avatar.user { background: #c8e6c9; }

.bubble {
    max-width: 82%;
    padding: 0.85rem 1.1rem;
    border-radius: 18px;
    font-size: 0.92rem;
    line-height: 1.6;
}
.bubble.bot {
    background: #f4f8f4;
    color: #1a3a2a;
    border-bottom-left-radius: 4px;
    border: 1px solid #dceadc;
}
.bubble.user {
    background: #1a3a2a;
    color: #f4f8f4;
    border-bottom-right-radius: 4px;
}

/* ── Disclaimer banner ── */
.disclaimer {
    background: #fff8e1;
    border-left: 3px solid #f9a825;
    padding: 0.65rem 1rem;
    border-radius: 0 8px 8px 0;
    font-size: 0.8rem;
    color: #5d4037;
    margin-bottom: 1.5rem;
}

/* ── Sidebar ── */
.sidebar-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.1rem;
    color: #1a3a2a;
    margin-bottom: 0.3rem;
}

/* ── Typing indicator ── */
.typing { color: #6b8f71; font-size: 0.85rem; font-style: italic; }

/* ── Input area override ── */
.stChatInputContainer { border-top: 1px solid #e8ede8 !important; }
</style>
""", unsafe_allow_html=True)

# ── API Key setup ───────────────────────────────────────────────────────────────
# Streamlit Cloud: set via Settings → Secrets as GEMINI_API_KEY = "..."
api_key = st.secrets.get("GEMINI_API_KEY")

genai.configure(api_key=api_key)

# ── System prompt ───────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """
You are a knowledgeable and empathetic Healthcare Q&A Assistant.
Your role is to help patients and users understand general health-related topics
in a clear, accessible, and compassionate manner.

## Your Responsibilities:
- Answer general healthcare questions about symptoms, conditions, medications, and wellness
- Explain medical terminology in simple, easy-to-understand language
- Provide information about when to seek professional medical attention
- Guide users on navigating healthcare services (e.g., what type of specialist to see)
- Support both English and Korean language queries

## Important Guidelines:
- ALWAYS remind users that your responses are for informational purposes only
- NEVER provide a definitive diagnosis or prescribe medication
- If a user describes a medical emergency (e.g., chest pain, difficulty breathing, stroke symptoms),
  IMMEDIATELY advise them to call emergency services (119 in Korea, 911 in the US)
- Be empathetic and patient — users may be anxious or confused about their health
- If asked about eye/vision health, provide especially detailed and careful responses

## Response Format:
- Keep responses concise but thorough (aim for 150-300 words)
- Use bullet points for lists of symptoms or steps
- End responses that involve symptoms with a recommendation to consult a healthcare provider
- Match the language of the user (respond in Korean if the user writes in Korean)

Remember: You bridge the gap between patients and the healthcare system by making
information accessible and reducing health anxiety through clear communication.
"""

# ── Session state ───────────────────────────────────────────────────────────────
if "chat_session" not in st.session_state:
    model = genai.GenerativeModel(
        model_name="gemini-2.5",
        system_instruction=SYSTEM_PROMPT,
    )
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.messages = []  # [{role, content}]
    st.session_state.session_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ── Sidebar ─────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p class="sidebar-title">🏥 Healthcare Chatbot</p>', unsafe_allow_html=True)
    st.caption(f"Session started: {st.session_state.session_start}")
    st.divider()

    if st.button("🔄 Reset conversation", use_container_width=True):
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=SYSTEM_PROMPT,
        )
        st.session_state.chat_session = model.start_chat(history=[])
        st.session_state.messages = []
        st.session_state.session_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.rerun()

    if st.button("💾 Export conversation", use_container_width=True):
        if st.session_state.messages:
            export = {
                "session_start": st.session_state.session_start,
                "model": "gemini-2.5-flash",
                "conversation": st.session_state.messages,
            }
            st.download_button(
                label="📥 Download JSON",
                data=json.dumps(export, ensure_ascii=False, indent=2),
                file_name=f"conversation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True,
            )
        else:
            st.info("No conversation to export yet.")

    st.divider()
    st.markdown("**Quick questions:**")
    quick = [
        "What are dry eye symptoms?",
        "건강검진 주기는?",
        "When to see a doctor for headaches?",
    ]
    for q in quick:
        if st.button(q, use_container_width=True, key=f"quick_{q}"):
            st.session_state._quick_input = q
            st.rerun()

    st.divider()
    st.caption("⚠️ For informational use only. Not a substitute for professional medical advice.")

# ── Main UI ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <h1>Healthcare Q&A</h1>
    <p class="subtitle">Ask any general health question — in English or Korean</p>
    <span class="badge">Powered by Google Gemini · Free Tier</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="disclaimer">
    ⚠️ This chatbot is for <strong>informational purposes only</strong> and does not constitute medical advice.
    In an emergency, call <strong>119</strong> (Korea) or <strong>911</strong> (US) immediately.
</div>
""", unsafe_allow_html=True)

# ── Render chat history ──────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    is_user = msg["role"] == "user"
    avatar_html = "👤" if is_user else "🏥"
    row_class = "user" if is_user else "bot"
    bubble_class = "user" if is_user else "bot"
    avatar_class = "user" if is_user else "bot"

    st.markdown(f"""
    <div class="msg-row {row_class}">
        <div class="avatar {avatar_class}">{avatar_html}</div>
        <div class="bubble {bubble_class}">{msg["content"]}</div>
    </div>
    """, unsafe_allow_html=True)

# ── Handle quick-input from sidebar ─────────────────────────────────────────────
if "_quick_input" in st.session_state:
    prompt = st.session_state._quick_input
    del st.session_state._quick_input

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner("🏥 Thinking..."):
        response = st.session_state.chat_session.send_message(prompt)
        reply = response.text
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()

# ── Chat input ───────────────────────────────────────────────────────────────────
prompt = st.chat_input("Ask a health question... / 건강 질문을 입력하세요...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("🏥 Thinking..."):
        response = st.session_state.chat_session.send_message(prompt)
        reply = response.text

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
