# 🧠 PersonaSwap

**PersonaSwap** is a solo-built, full-stack AI project that fuses the cultural intelligence of **Qloo's Taste AI™** with the generative power of **Google Gemini**, allowing users to explore how different personas think, feel, and consume culture.

---

## 🌟 What Is PersonaSwap?

> “What would an art critic from Berlin listen to?”  
> “How would a Tokyo street photographer describe their world?”

**PersonaSwap** is an AI-powered *persona simulator*. You input any persona — real or fictional — and it generates:

- 🎭 A **cultural identity summary**
- 🧠 A creative **narrative voice**
- 📡 **Real-world taste predictions** via Qloo (e.g., movies, music)

> Imagine simulating how anyone would live, love, or create — based on their taste.

---

## 💡 Why Is It Innovative?

🔗 **Fusion of LLMs + Real-World Taste Data**  
Go beyond basic text gen — we integrate **actual human behavior patterns** through Qloo.

🧠 **Empathic Persona Simulation**  
Understand how someone would interact with the world — their culture, values, choices.

🔁 **Swap Perspectives Instantly**  
Compare and contrast how different personas see the world.

---

## 🛠️ Tech Stack

| Layer        | Tool                    |
|-------------|--------------------------|
| LLM         | Google Gemini            |
| Taste Data  | Qloo Taste AI            |
| Backend     | FastAPI (Python)         |
| Frontend    | React.js                 |
| Search Ready| FAISS-ready              |
| Styling     | CSS (Tailwind dropped temporarily) |
| Storage     | Pickle-based file DB     |
| Environment | `venv`, `.env`           |

---

## 🚀 Core Features

- 🧠 Persona Cultural Summary (via Gemini)
- 📡 Real Taste Preferences (via Qloo)
- ✍️ Narrative Style Writer
- 🧬 Save + Compare Personas
- 🔄 Ready for Embedding (FAISS-compatible)
- 💾 Local persona persistence (`personas.pkl`)

---

## 🧪 Features In Progress

- 🔍 Semantic similarity search (FAISS)
- 🎨 Qloo result cards with real-time data
- 🔄 Persona Swap Mode (empathy view)
- 👥 Profile Comparisons
- 🌐 Public shareable persona profiles


---

📦 Environment Setup
1) Create a Python virtual environment
2) Add your API keys to a .env file inside backend
3) Inside virtual environment: pip install -r requirements.txt

---

## ✅ Run Instructions

### 🟢 Backend
 - cd backend
 - myenv\Scripts\activate
 - python run.py

### 🟢 Frontend
 - cd persona-frontend
 - myenv\Scripts\activate   (In another terminal)
 - npm run dev

