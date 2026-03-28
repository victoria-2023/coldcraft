# ColdCraft ✦ AI Cold Email Generator

> Generate sharp, personalized cold emails in seconds using AI.
> Built with **FastAPI** · **Streamlit** · **Claude API (Anthropic)**

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green) ![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red)

---

## What It Does

Fill in 5 fields → get a human-sounding cold email with a compelling subject line, tailored to your recipient and tone. No templates. No fluff.

**Use cases:**
- Developers reaching out to startup founders for freelance work
- Founders doing sales outreach
- Anyone tired of writing cold emails from scratch

---

## Tech Stack

| Layer | Tech |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| AI | Anthropic Claude API |
| Deployment | Streamlit Cloud (frontend) + Railway/Render (backend) |

---

## Project Structure

```
coldcraft/
├── backend/
│   ├── main.py           # FastAPI app
│   ├── requirements.txt
│   └── Procfile          # For Railway/Render deployment
├── frontend/
│   ├── app.py            # Streamlit app
│   └── requirements.txt
├── .env.example
└── README.md
```

---

## Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/coldcraft.git
cd coldcraft
```

### 2. Set up the backend
```bash
cd backend
pip install -r requirements.txt

# Create .env file
echo "ANTHROPIC_API_KEY=your_key_here" > .env

# Run the API
uvicorn main:app --reload
# → Running at http://localhost:8000
```

### 3. Set up the frontend (new terminal)
```bash
cd frontend
pip install -r requirements.txt

# Run Streamlit
streamlit run app.py
# → Opens at http://localhost:8501
```

---

## Deployment

### Backend → Railway (free tier)
1. Push `backend/` folder to GitHub
2. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
3. Add environment variable: `ANTHROPIC_API_KEY=your_key`
4. Railway auto-detects the `Procfile` and deploys
5. Copy your Railway URL (e.g. `https://coldcraft-api.up.railway.app`)

### Frontend → Streamlit Cloud (free)
1. Push `frontend/` folder to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → New App
3. Select your repo and `frontend/app.py`
4. Add secret: `BACKEND_URL = "https://your-railway-url.up.railway.app"`
5. Deploy ✅

---

## Getting an Anthropic API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up / log in
3. Go to **API Keys** → Create new key
4. New accounts get free credits to start

---

## Built By

**Victoria Ude** — AI/ML Engineer & Full-Stack Developer
- 🌐 [Portfolio](https://official-web-portfolio.vercel.app/)
- 💼 [LinkedIn](https://www.linkedin.com/in/victoria-amarachi-ude)
- 🐙 [GitHub](https://github.com/victoria-2023)

Open to freelance contracts with early-stage startups. Let's build something.
