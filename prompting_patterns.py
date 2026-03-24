from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask(prompt, temperature=0.3):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=500,
        )
    )
    return response.text


# ────────────────────────────────────────────────
# PATTERN 1 — ZERO-SHOT
# ────────────────────────────────────────────────
def zero_shot(review):
    prompt = f"""Classify this review as exactly one of: positive, negative, neutral.
Only reply with the single word classification.

Review: {review}
Classification:"""
    return ask(prompt)


# ────────────────────────────────────────────────
# PATTERN 2 — FEW-SHOT
# ────────────────────────────────────────────────
# Store examples separately — easy to add/remove
FEW_SHOT_EXAMPLES = [
    ("Loved it, works perfectly!",          "positive"),
    ("Terrible quality, broke in one day",  "negative"),
    ("It was okay, nothing special",        "neutral"),
    ("Best purchase I've made this year",   "positive"),
    ("Completely useless, waste of money",  "negative"),
]

def few_shot(review):
    examples = "\n".join(
        f'Review: "{inp}" → {out}'
        for inp, out in FEW_SHOT_EXAMPLES
    )
    prompt = f"""Classify sentiment as: positive, negative, or neutral.

Examples:
{examples}

Now classify:
Review: "{review}"
Classification:"""
    return ask(prompt)


# ────────────────────────────────────────────────
# PATTERN 3 — CHAIN OF THOUGHT
# ────────────────────────────────────────────────
def chain_of_thought(code):
    prompt = f"""Review this Python code step by step.

Think through each point:
1. What does this code do?
2. What bugs or errors could occur?
3. What style or naming issues exist?
4. What is the recommended fix?

Then give your final verdict.

Code:
{code}

Step-by-step review:"""
    return ask(prompt, temperature=0.5)


# ────────────────────────────────────────────────
# PATTERN 4 — COMBINED (zero + few + CoT)
# ────────────────────────────────────────────────

def combined_reviewer(code):
    prompt = f"""You are a Python code reviewer. Be concise and specific.

Examples of good reviews:
Code: x = int(input())
Review: Missing error handling — crashes on non-numeric input.
Fix: wrap in try/except ValueError

Code: def f(l): return [i*2 for i in l]
Review: Poor naming — 'f' and 'l' are not descriptive.
Fix: rename to double_items(numbers)

Now review this code using the same format.
Think through: what it does → bugs → style issues → fix.

Code:
{code}

Review:"""
    return ask(prompt, temperature=0.3)


# ────────────────────────────────────────────────
# TEST ALL PATTERNS
# ────────────────────────────────────────────────
if __name__ == "__main__":

    review = "Fast delivery but the packaging was damaged"
    code   = """
def get_user_age():
    a = int(input("Enter age: "))
    return a
"""

    print("=" * 50)
    print("ZERO-SHOT")
    print(zero_shot(review))

    print("\nFEW-SHOT")
    print(few_shot(review))

    print("\nCHAIN OF THOUGHT")
    print(chain_of_thought(code))

    print("\nCOMBINED REVIEWER")
    print(combined_reviewer(code))



    

