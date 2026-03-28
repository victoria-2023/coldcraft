from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import anthropic
import traceback
import os
import json

# Load .env FIRST before anything else
load_dotenv()

api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY is not set. Please add it to your .env file.")

client = anthropic.Anthropic(api_key=api_key)

app = FastAPI(title="ColdCraft API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class EmailRequest(BaseModel):
    sender_name: str
    sender_role: str
    recipient: str
    problem: str
    credential: str
    tone: str


@app.get("/")
def root():
    return {"status": "ColdCraft API is running"}


@app.post("/generate-email")
def generate_email(req: EmailRequest):
    prompt = f"""You are an expert cold email copywriter. Write a cold email with the following details:

Sender: {req.sender_name} ({req.sender_role or 'Freelancer/Developer'})
Recipient: {req.recipient}
Problem the sender solves for them: {req.problem}
Sender's best credential/proof: {req.credential or 'Relevant project experience'}
Tone: {req.tone}

Write a cold email that:
- Has a compelling, specific subject line (not generic)
- Opens with a hook that shows you understand their world
- Clearly states the value proposition in 1-2 sentences
- Mentions the credential naturally as social proof
- Has a soft, low-friction CTA (e.g. "open to a 15-min chat?")
- Is under 150 words total (concise wins)
- Feels human, not AI-generated
- Always sign off with "Best regards," not "Best,"

Respond ONLY in this JSON format (no markdown, no backticks):
{{
  "subject": "subject line here",
  "body": "full email body here with proper line breaks using \\n"
}}"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        raw = message.content[0].text.strip()
        print("RAW RESPONSE:", raw)
        clean = raw.replace("```json", "").replace("```", "").strip()
        parsed = json.loads(clean)
        return parsed
    except json.JSONDecodeError as e:
        print("JSON PARSE ERROR:", e)
        raise HTTPException(status_code=500, detail=f"Failed to parse AI response: {e}")
    except anthropic.AuthenticationError:
        raise HTTPException(status_code=500, detail="Invalid API key. Check your .env file.")
    except anthropic.APIConnectionError:
        raise HTTPException(status_code=500, detail="Cannot reach Anthropic API. Check your internet.")
    except Exception as e:
        print("UNEXPECTED ERROR:", type(e).__name__, str(e))
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {str(e)}")