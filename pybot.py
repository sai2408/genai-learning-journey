from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-2.5-flash-lite"

SYSTEM_PROMPT = """You are PyBot, a friendly Python tutor for beginners.

- Be warm, patient and encouraging
- Always include a short code example
- Explain each line of code simply
- End every reply with one follow-up question
- Only answer Python related questions
- If asked anything else say: "I only know Python!"
"""

def build_message(role, text):
    return types.Content(
        role=role,
        parts=[types.Part(text=text)]
    )

def trim_history(history, max_turns=10):
    if len(history) > max_turns * 2:
        history = history[-(max_turns * 2):]
    return history

def ask(history):
    response = client.models.generate_content(
        model=MODEL,
        contents=history,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.7,
            max_output_tokens=500,
        )
    )
    return (
        response.text,
        response.usage_metadata.total_token_count,
        response.candidates[0].finish_reason.name,
    )

def chat():
    history = []
    print("\n╔══════════════════════════════╗")
    print("║  PyBot — Your Python Tutor   ║")
    print("║  Type 'quit' to exit         ║")
    print("║  Type 'memory' to inspect    ║")
    print("║  Type 'clear' to reset       ║")
    print("╚══════════════════════════════╝\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("\nPyBot: Great work today! Keep coding! Goodbye!\n")
            break

        if user_input.lower() == "clear":
            history = []
            print("\n  [Memory cleared — fresh start]\n")
            continue

        if user_input.lower() == "memory":
            print(f"\n  --- Memory ({len(history)//2} turns) ---")
            for msg in history:
                role = msg.role.upper()
                text = msg.parts[0].text[:60].replace('\n', ' ')
                print(f"  [{role}]: {text}...")
            print()
            continue

        history.append(build_message("user", user_input))

        try:
            reply, tokens, finish_reason = ask(history)
            history.append(build_message("model", reply))
            history = trim_history(history)

            print(f"\nPyBot: {reply}")
            print(f"  [tokens: {tokens} | turns: {len(history)//2}]\n")

            if finish_reason == "MAX_TOKENS":
                print("  [Warning: response was cut off]\n")

        except Exception as e:
            history.pop()
            print(f"\n  Error: {e}\n")

if __name__ == "__main__":
    chat()
