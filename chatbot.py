from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """You are PyBot, a friendly Python tutor for beginners.
- Always include a short code example
- Be encouraging and patient
- End each reply with one follow-up question
- Only answer Python-related questions
"""

MAX_TURNS = 10

def build_message(role, text):
    """Build a proper Content object for the new SDK."""
    return types.Content(
        role=role,
        parts=[types.Part(text=text)]
    )

def trim_history(history):
    if len(history) > MAX_TURNS * 2:
        history = history[-(MAX_TURNS * 2):]
    return history

def chat():
    history = []
    print("PyBot ready! Type 'quit' to exit, 'memory' to inspect history.\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if user_input.lower() == "memory":
            print(f"\n--- History ({len(history)} messages) ---")
            for m in history:
                role = m.role.upper()
                text = m.parts[0].text[:80]
                print(f"  [{role}]: {text}...")
            print("---\n")
            continue

        # Add user message using proper types
        history.append(build_message("user", user_input))

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=history,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    temperature=0.7,
                    max_output_tokens=500,
                )
            )

            reply = response.text

            # Add model reply using proper types
            history.append(build_message("model", reply))

            history = trim_history(history)

            print(f"\nPyBot: {reply}")
            tokens = response.usage_metadata.total_token_count
            print(f"[tokens: {tokens} | turns in memory: {len(history)//2}]\n")

        except Exception as e:
            history.pop()  # remove failed user message
            print(f"Error: {e}\n")

if __name__ == "__main__":
    chat()
