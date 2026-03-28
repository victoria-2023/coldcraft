import streamlit as st
import requests
import os

st.set_page_config(
    page_title="ColdCraft — AI Cold Email Generator",
    page_icon="✦",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

* { font-family: 'Inter', sans-serif; }

header[data-testid="stHeader"],
div[data-testid="stToolbar"],
div[data-testid="stDecoration"],
.stDeployButton { display: none !important; }
footer { visibility: hidden; }

.stApp, .main, [data-testid="stAppViewContainer"] {
    background-color: #f8fafc !important;
}
[data-testid="stAppViewContainer"] > .main {
    padding-top: 48px !important;
}

h1 {
    font-size: 2.6rem !important;
    font-weight: 700 !important;
    color: #0f172a !important;
    letter-spacing: -0.03em !important;
    line-height: 1.1 !important;
}

.badge {
    display: inline-block;
    background: #f0fdf4;
    border: 1px solid #86efac;
    border-radius: 100px;
    padding: 5px 14px;
    font-size: 11px;
    color: #16a34a;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    margin-bottom: 14px;
}

.subtitle {
    color: #64748b;
    font-size: 16px;
    margin-bottom: 36px;
    font-weight: 400;
    line-height: 1.6;
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    background-color: #ffffff !important;
    border: 1.5px solid #e2e8f0 !important;
    color: #0f172a !important;
    border-radius: 10px !important;
    font-size: 14px !important;
    padding: 12px 14px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border-color: #16a34a !important;
    box-shadow: 0 0 0 3px rgba(22,163,74,0.1) !important;
}

div[data-testid="stSelectbox"] > div > div {
    background-color: #ffffff !important;
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 10px !important;
    color: #0f172a !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
}

label {
    color: #475569 !important;
    font-size: 11px !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
}

div[data-testid="stButton"] button {
    background-color: #0f172a !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 14px 28px !important;
    font-size: 15px !important;
    width: 100% !important;
    letter-spacing: 0.01em !important;
    box-shadow: 0 4px 12px rgba(15,23,42,0.15) !important;
    transition: all 0.2s !important;
}
div[data-testid="stButton"] button:hover {
    background-color: #1e293b !important;
    box-shadow: 0 6px 16px rgba(15,23,42,0.2) !important;
    transform: translateY(-1px) !important;
}

.result-wrapper {
    background: #ffffff;
    border: 1.5px solid #e2e8f0;
    border-radius: 16px;
    overflow: hidden;
    margin-top: 8px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.06);
}

.result-header {
    background: #f8fafc;
    border-bottom: 1px solid #e2e8f0;
    padding: 14px 24px;
    display: flex;
    align-items: center;
    gap: 7px;
}

.dot { width:11px; height:11px; border-radius:50%; display:inline-block; }
.dot-red { background:#ff5f57; }
.dot-yellow { background:#febc2e; }
.dot-green { background:#28c840; }

.subject-line {
    padding: 14px 24px;
    border-bottom: 1px solid #f1f5f9;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    color: #94a3b8;
    background: #ffffff;
}
.subject-line span { color: #0f172a; font-weight: 500; }

.email-body {
    padding: 28px 24px;
    font-size: 15px;
    line-height: 1.85;
    color: #1e293b;
    white-space: pre-wrap;
    background: #ffffff;
    font-weight: 400;
}

.section-label {
    font-size: 11px !important;
    font-weight: 600 !important;
    color: #16a34a !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    margin-bottom: 10px !important;
    display: block;
}

.tip-box {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-radius: 12px;
    padding: 16px 20px;
    font-size: 13px;
    color: #166534;
    margin-top: 20px;
    line-height: 1.65;
}
.tip-box b { font-weight: 600; }

.copy-hint {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    margin-top: 10px;
    font-family: 'DM Mono', monospace;
}

.footer {
    text-align: center;
    color: #cbd5e1;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    margin-top: 52px;
    padding-bottom: 32px;
}
.footer a { color: #94a3b8; text-decoration: none; }
.footer a:hover { color: #16a34a; }
</style>
""", unsafe_allow_html=True)

# ── Header ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="badge">✦ AI-Powered · Built by Victoria Ude</div>', unsafe_allow_html=True)
st.title("Cold emails that actually land.")
st.markdown("<p class='subtitle'>Describe your target and what you offer — get a sharp, personalized cold email in seconds.</p>", unsafe_allow_html=True)

# ── Form ────────────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    sender_name = st.text_input("Your Name", placeholder="e.g. Victoria Ude")
with col2:
    sender_role = st.text_input("Your Role / Service", placeholder="e.g. AI/ML Engineer")

recipient = st.text_input("Recipient — Who Are You Emailing?", placeholder="e.g. Founder of a fintech startup building budgeting tools")
problem = st.text_area("What Problem Do You Solve For Them?", placeholder="e.g. I can integrate AI features like smart transaction categorization using Claude API.", height=100)
credential = st.text_input("Your Best Credential or Proof Point", placeholder="e.g. Built an AI-powered RFP writer for GreenPowerPlus using GPT/Claude")
tone = st.selectbox("Tone", ["Professional & direct", "Friendly & conversational", "Bold & confident", "Concise & punchy"])

st.markdown("<br/>", unsafe_allow_html=True)
generate = st.button("⚡ Generate Cold Email")

# ── Generation ──────────────────────────────────────────────────────────────────
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:8000")

if generate:
    if not sender_name or not recipient or not problem:
        st.warning("Please fill in your name, recipient, and the problem you solve.")
    else:
        with st.spinner("Crafting your email..."):
            try:
                response = requests.post(
                    f"{BACKEND_URL}/generate-email",
                    json={
                        "sender_name": sender_name,
                        "sender_role": sender_role,
                        "recipient": recipient,
                        "problem": problem,
                        "credential": credential,
                        "tone": tone,
                    },
                    timeout=30,
                )
                response.raise_for_status()
                data = response.json()

                subject = data.get("subject", "")
                body = data.get("body", "")

                st.markdown("<br/>", unsafe_allow_html=True)
                st.markdown('<span class="section-label">✦ Your Cold Email</span>', unsafe_allow_html=True)
                st.markdown(f"""
                <div class="result-wrapper">
                    <div class="result-header">
                        <span class="dot dot-red"></span>
                        <span class="dot dot-yellow"></span>
                        <span class="dot dot-green"></span>
                    </div>
                    <div class="subject-line">Subject: <span>{subject}</span></div>
                    <div class="email-body">{body}</div>
                </div>
                <p class="copy-hint">Select the text above to copy</p>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="tip-box">
                    <b>💡 LinkedIn tip:</b> Screenshot this app and post it with a caption like
                    <em>"Built an AI cold email generator using FastAPI + Streamlit + Claude API."</em>
                    Tag your stack — founders and CTOs are watching.
                </div>
                """, unsafe_allow_html=True)

            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to the backend. Make sure the FastAPI server is running.")
            except Exception as e:
                st.error(f"Something went wrong: {e}")

# ── Footer ──────────────────────────────────────────────────────────────────────
st.markdown("<br/><br/>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Built by <a href='https://official-web-portfolio.vercel.app/' target='_blank'>Victoria Ude</a> · AI/ML Engineer & Full-Stack Developer</div>", unsafe_allow_html=True)