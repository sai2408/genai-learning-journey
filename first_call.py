#Code - 1
'''
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env file!")
else:
    print("API key loaded!")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="Explain what an LLM is in 2 sentences."
    )

    print(response.text)
    print(f"\nTokens used: {response.usage_metadata.total_token_count}")
'''
#Code - 2
'''
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompts = [
    "What is recursion?",                          # vague
    "Explain recursion to a Python beginner "
    "in 3 bullet points with a code example."      # specific
]

for prompt in prompts:
    print(f"\nPROMPT: {prompt}")
    print("-" * 40)
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )
    print(response.text)
'''
#Code - 3
'''
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask(prompt, temperature=0.7, max_tokens=500):
    print("\n" + "="*50)
    print(f"PROMPT        : {prompt}")
    print(f"TEMPERATURE   : {temperature}")
    print(f"MAX TOKENS    : {max_tokens}")
    print("="*50)

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
        )
    )

    # ── Token info ──────────────────────────────────
    usage = response.usage_metadata
    prompt_tokens    = usage.prompt_token_count
    response_tokens  = usage.candidates_token_count
    total_tokens     = usage.total_token_count
    context_limit    = 100_000   # gemini-2.5-flash-lite limit
    context_used_pct = round((total_tokens / context_limit) * 100, 2)

    # ── Finish reason ────────────────────────────────
    finish_reason = response.candidates[0].finish_reason.name

    # ── Print dashboard ──────────────────────────────
    print(f"\nRESPONSE:\n{response.text}")
    print("\n--- STATS ---")
    print(f"Prompt tokens    : {prompt_tokens}")
    print(f"Response tokens  : {response_tokens}")
    print(f"Total tokens     : {total_tokens}")
    print(f"Context used     : {context_used_pct}% of {context_limit:,}")
    print(f"Finish reason    : {finish_reason}")

    # ── Context warning ──────────────────────────────
    if context_used_pct > 80:
        print("WARNING: Context window over 80% full!")
    elif finish_reason == "MAX_TOKENS":
        print("WARNING: Response was cut off — increase max_tokens!")
    else:
        print("Status: All good.")

    print("="*50)
    return response.text


# ── Try different temperatures ───────────────────────
print("\n>>> TEMPERATURE COMPARISON <<<")

ask("Give me a creative name for a Python chatbot", temperature=0.0)
ask("Give me a creative name for a Python chatbot", temperature=0.7)
ask("Give me a creative name for a Python chatbot", temperature=1.5)

# ── Try hitting max_tokens limit ─────────────────────
print("\n>>> MAX TOKENS TEST <<<")

ask("Explain how the internet works", max_tokens=20)   # will get cut off
ask("Explain how the internet works", max_tokens=300)  # will complete
'''
#Code - 4
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """You are PyBot, a friendly Python tutor for beginners.

1. IDENTITY: Expert Python teacher with 10 years experience.
2. TONE: Warm, patient, encouraging. Celebrate progress.
3. BEHAVIOR:
   - Always include a working code example
   - Explain each line of code briefly
   - End with one follow-up question
4. CONSTRAINTS:
   - Only answer Python-related questions
   - If asked about anything else, say: "I only know Python!"
   - Max 10 lines of code per response
5. FORMAT: Use bullet points. Wrap code in triple backticks.
"""

def ask(user_message):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=user_message,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            temperature=0.7,
            max_output_tokens=500,
        )
    )
    return response.text

# Test it
print(ask("What is a list comprehension?"))
print("---")
print(ask("What is the capital of France?"))  # should get redirected




