from google import genai
from google.genai import types
import os
import json
import re
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ── Schema we want back ───────────────────────────────
SCHEMA = """
{
  "topic": "the Python topic explained",
  "explanation": "plain English explanation in 2-3 sentences",
  "code_example": "a short working Python code snippet",
  "difficulty": "beginner | intermediate | advanced",
  "follow_up_question": "one question to test understanding"
}
"""

SYSTEM_PROMPT = f"""You are PyBot, a Python tutor for beginners.

IMPORTANT: You must ALWAYS respond with valid JSON only.
No extra text, no markdown fences, no explanation outside the JSON.

Respond using exactly this schema:
{SCHEMA}
"""

# ── Robust JSON parser ────────────────────────────────
def safe_parse(text):
    """Extract JSON even if model adds extra text or fences."""
    # Strip markdown fences
    text = re.sub(r'```json\s*|\s*```', '', text).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try finding first {...} block
        match = re.search(r'\{.*\}', text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass
        return {"error": "parse_failed", "raw": text}

# ── Pretty print the JSON response ───────────────────
def display(data):
    if "error" in data:
        print(f"\nParse error: {data.get('raw', '')[:100]}\n")
        return

    print(f"""
┌─────────────────────────────────────────┐
  Topic      : {data.get('topic', 'N/A')}
  Difficulty : {data.get('difficulty', 'N/A')}
├─────────────────────────────────────────┤
  {data.get('explanation', '')}

  Code:
  {data.get('code_example', '')}

  Question: {data.get('follow_up_question', '')}
└─────────────────────────────────────────┘""")

# ── Main chat loop ────────────────────────────────────
def chat():
    history = []
    print("PyBot (JSON mode) — type 'quit' to exit\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "quit":
            break

        history.append(types.Content(
            role="user",
            parts=[types.Part(text=user_input)]
        ))

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=history,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.3,      # lower = more reliable JSON
                    max_output_tokens=600,
                    response_mime_type="application/json",  # enforce JSON
                )
            )

            raw = response.text
            data = safe_parse(raw)

            history.append(types.Content(
                role="model",
                parts=[types.Part(text=raw)]
            ))

            display(data)

            # Also show raw JSON for learning purposes
            print(f"[Raw JSON preview]: {raw[:80]}...\n")

        except Exception as e:
            history.pop()
            print(f"Error: {e}\n")

if __name__ == "__main__":
    chat()

