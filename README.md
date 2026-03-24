# 🤖 GenAI Learning Journey — Python + Google Gemini

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google-Gemini%20API-orange?logo=google&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-coming%20soon-yellowgreen)
![FastAPI](https://img.shields.io/badge/FastAPI-coming%20soon-009688?logo=fastapi&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-Vertex%20AI-coming%20soon-4285F4?logo=googlecloud&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

A hands-on learning repository documenting my journey from **Python basics → GenAI development** using Google Gemini, LangChain, FastAPI, GCP Vertex AI, and Vector Databases.

---

## 📌 About This Repo

This is my personal learning lab where I build real working code as I study each concept. Every file represents a milestone — from my very first API call to building structured AI chatbots with memory, prompting patterns, and beyond.

> **Goal:** Master the full GenAI development stack and build production-ready AI applications on Google Cloud.

---

## 🗂️ Repository Structure

```
genai-learning-journey/
│
├── basics/
│   ├── first_call.py           # First Gemini API call + token/temperature experiments
│   ├── prompting_patterns.py   # Zero-shot, Few-shot, Chain-of-Thought prompting
│   ├── structured_bot.py       # JSON-mode responses with schema enforcement
│   └── chatbot.py              # Multi-turn chatbot with conversation memory
│
├── pybot/
│   ├── pybot.py                # PyBot — Python tutor chatbot (in progress)
│   ├── memory.py               # Conversation memory module (in progress)
│   ├── mood.py                 # Mood/tone detection module (in progress)
│   └── persona.py              # Persona switching module (in progress)
│
└── README.md
```

---

## 🧠 What I've Built So Far

### ✅ `first_call.py` — Gemini API Fundamentals
- First API call using `google-genai` SDK
- Prompt quality comparison (vague vs specific)
- Temperature and `max_tokens` experiments
- Token usage dashboard with context window tracking
- Finish reason detection and warnings

### ✅ `prompting_patterns.py` — Prompt Engineering Techniques
| Pattern | Description |
|---|---|
| **Zero-shot** | Direct classification with no examples |
| **Few-shot** | Learning from labeled examples |
| **Chain-of-Thought** | Step-by-step reasoning before conclusion |
| **Combined** | All three patterns working together |

### ✅ `chatbot.py` — Multi-Turn Chatbot with Memory
- Persistent conversation history using `types.Content`
- Memory trimming (configurable max turns)
- `memory` command to inspect history in real time
- Token tracking per turn
- System prompt with identity, tone, and behavior rules

### ✅ `structured_bot.py` — JSON-Mode Structured Responses
- Enforces a strict JSON schema every response
- Robust parser handles markdown fences + malformed JSON
- Pretty-prints structured output with topic, explanation, code, difficulty, and follow-up question
- Uses `response_mime_type="application/json"` for reliability

---

## 🚀 Roadmap

### Phase 1 — Python + Gemini Basics ✅ (Current)
- [x] First API call
- [x] Prompt engineering patterns
- [x] Multi-turn chatbot with memory
- [x] Structured JSON output

### Phase 2 — Advanced Bot Features 🔄 (In Progress)
- [ ] Mood/tone detection (`mood.py`)
- [ ] Persona switching (`persona.py`)
- [ ] Enhanced memory management (`memory.py`)
- [ ] Full PyBot tutor (`pybot.py`)

### Phase 3 — Frameworks 📅 (Planned)
- [ ] LangChain — chains, agents, tools
- [ ] FastAPI — REST API wrapper for chatbots
- [ ] RAG (Retrieval-Augmented Generation)

### Phase 4 — Google Cloud Platform ☁️ (Planned)
- [ ] Vertex AI — deploying models on GCP
- [ ] Google ADK (Agent Development Kit)
- [ ] Vector Database integration (ChromaDB / Pinecone / Weaviate)
- [ ] Production deployment pipeline

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.10+
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

### Installation

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/genai-learning-journey.git
cd genai-learning-journey

# Install dependencies
pip install google-genai python-dotenv

# Create your .env file
echo "GEMINI_API_KEY=your_key_here" > .env
```

### Running the Examples

```bash
# First API call experiments
python basics/first_call.py

# Prompting patterns demo
python basics/prompting_patterns.py

# Interactive chatbot
python basics/chatbot.py

# Structured JSON bot
python basics/structured_bot.py
```

---

## 🛠️ Tech Stack

| Technology | Purpose | Status |
|---|---|---|
| Python 3.10+ | Core language | ✅ Active |
| Google Gemini API (`gemini-2.5-flash-lite`) | LLM backbone | ✅ Active |
| `google-genai` SDK | API client | ✅ Active |
| LangChain | Chains & Agents | 📅 Planned |
| FastAPI | REST API layer | 📅 Planned |
| Google ADK | Agent framework | 📅 Planned |
| GCP Vertex AI | Cloud deployment | 📅 Planned |
| Vector DB (ChromaDB/Pinecone) | RAG memory | 📅 Planned |

---

## 📚 Key Concepts Covered

- **LLM fundamentals** — tokens, context windows, temperature, finish reasons
- **Prompt engineering** — zero-shot, few-shot, chain-of-thought
- **Conversation memory** — multi-turn history management, trim strategies
- **Structured outputs** — JSON schema enforcement, robust parsing
- **System prompts** — identity, tone, behavior, and constraint design

---

## 🤝 Connect With Me

I'm documenting this entire journey publicly. Follow along!

- 💼 [LinkedIn]([https://www.linkedin.com/in/YOUR_PROFILE](https://www.linkedin.com/in/sai-vardhan-thimmisetty/))
- 🐙 [GitHub](https://github.com/sai2408)

---

## 📄 License

MIT License — feel free to learn from, fork, or build on this.

---

> *"The best way to learn AI development is to build things, break things, and share the journey."* 🚀
