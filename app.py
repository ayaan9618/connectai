import os
import requests
import streamlit as st
from dotenv import load_dotenv
from data.users import FAKE_USERS

load_dotenv()

st.set_page_config(page_title="Connectoai", page_icon="🤖")


# Google AI Studio (Generative Language API)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "").strip()
GOOGLE_MODEL = os.getenv("GOOGLE_MODEL", "gemini-2.0-flash").strip()
GOOGLE_URL = os.getenv(
    "GOOGLE_URL",
    f"https://generativelanguage.googleapis.com/v1beta/models/{GOOGLE_MODEL}:generateContent"
).strip()

HEADERS = {
    "Content-Type": "application/json",
}

def call_google(messages, temperature: float = 0.7, max_output_tokens: int = 512) -> str:
    """Call Google Gemini generateContent; concatenate messages into a single user prompt for simplicity."""
    if not GOOGLE_API_KEY:
        for m in reversed(messages):
            if m.get("role") == "user":
                return m.get("content", "")
        return ""
    # Join conversation into one prompt (simple text use-case)
    parts = []
    for m in messages:
        role = m.get("role", "user")
        content = m.get("content", "")
        prefix = "User:" if role == "user" else "Assistant:"
        parts.append(f"{prefix} {content}")
    joined = "\n".join(parts) + "\nAssistant:"
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": joined}]}
        ],
        "generationConfig": {"temperature": temperature, "maxOutputTokens": max_output_tokens}
    }
    try:
        resp = requests.post(GOOGLE_URL, headers=HEADERS, params={"key": GOOGLE_API_KEY}, json=payload, timeout=60)
        if resp.status_code == 401:
            return "Google API 401 Unauthorized. Check GOOGLE_API_KEY."
        if resp.status_code == 403:
            return "Google API 403 Forbidden. Ensure the model is enabled for your project and billing if required."
        resp.raise_for_status()
        data = resp.json()
        candidates = data.get("candidates") or []
        if candidates and candidates[0].get("content", {}).get("parts"):
            parts_out = candidates[0]["content"]["parts"]
            texts = [p.get("text", "") for p in parts_out if isinstance(p, dict)]
            return "".join(texts).strip() or ""
        return (str(data)[:800] + "…") if data else ""
    except Exception as e:
        return f"[Google request failed] {e}"

# Simple matcher keywords
KEYWORDS = [
    "python","startup","blockchain","fintech","healthcare","ai","ml","robotics","space","quantum","music",
    "frontend","react","security","policy","ux","agritech","drones","data","viz","iot","edge","electronics",
    "education","learning","marketing","seo","fullstack","postgres","wildfire","materials","batteries",
    "manufacturing","automation","legal","contracts","satellites","rf","cad","3d","cloud","cost","farming",
    "hydroponics","django","apis","auth","bci","neuroscience","math","chemistry","catalysis"
]

def score_user(query: str, user: dict) -> int:
    q = query.lower()
    score = 0
    for kw in KEYWORDS + [i.lower() for i in user.get("interests", [])]:
        if kw and kw in q:
            score += 2
    for i in user.get("interests", []):
        if i.lower() in q:
            score += 3
    return score + (2 if user.get("online") else 0)

# Session state initialization
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Connectoai: A platform where users interact with an AI assistant, but connect you to people"}
    ]

if "suggested_users" not in st.session_state:
    st.session_state.suggested_users = set()

# Render message history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Context input (once per session)
if "context" not in st.session_state:
    st.session_state.context = st.text_input(
        "Set your current learning/exploration context (e.g., 'I'm learning Python')"
    )

# Greeting check helper
def is_greeting(text):
    greetings = ["hi", "hello", "hey", "yo", "greetings"]
    return text.strip().lower() in greetings

# When user sends input
if prompt := st.chat_input("Type your message"):
    # Handle simple greeting first
    if is_greeting(prompt):
        reply = "Hi there! How can I help you today?"
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Prepare messages including context for AI call
        messages_for_ai = st.session_state.messages[-12:]
        if st.session_state.context:
            contextual_message = {"role": "user", "content": f"My current exploration: {st.session_state.context}"}
            messages_for_ai = [contextual_message] + messages_for_ai

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                reply = call_google(messages_for_ai)
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

        # Prepare interest query fallback to ensure string type
        interest_query = (st.session_state.context or prompt) or ""



        # Filter to exclude users already suggested in this session to avoid repeats
        scored = sorted(
            (u for u in FAKE_USERS if u["name"] not in st.session_state.suggested_users),
            key=lambda u: score_user(interest_query, u),
            reverse=True
        )[:3]

        suggested_users = [u for u in scored if score_user(interest_query, u) > 0]

        if suggested_users:
            for u in suggested_users:
                st.session_state.suggested_users.add(u["name"])

            user_names = [u["name"] for u in suggested_users]
            interests_overlap = set()
            for u in suggested_users:
                interests_overlap.update([i.lower() for i in u.get("interests", [])])
            common_interests = [kw for kw in KEYWORDS if kw in interest_query.lower() and kw in interests_overlap]
            interest_text = ", ".join(common_interests[:2]) if common_interests else "similar topics"

           
            
          

            cols = st.columns(len(suggested_users))
            for c, u in zip(cols, suggested_users):
                with c:
                    st.markdown(f"### {u['name']}")
                    st.caption(u["current_activity"])
                    st.write(" ".join([f"`{tag}`" for tag in u.get("interests", [])[:3]]))
                    if st.button(f"Chat with {u['name']}", key=f"chat_{u['name']}"):
                        st.session_state.messages.append({
                            "role": "system",
                            "content": f"You started a study pod chat with {u['name']}."
                        })
                        st.success(f"Started chat with {u['name']}!")
