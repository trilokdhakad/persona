# 🧠 PersonaSwap

**PersonaSwap** is a solo-built project that fuses the cultural intelligence of **Qloo's Taste AI™** with the generative capabilities of **Google Gemini**, allowing users to explore how different personas would think, feel, and act based on their unique cultural preferences.

---

## 🌟 What Is PersonaSwap?

> “What would an art critic from Berlin like to watch, eat, or listen to?”  
> “How would a Tokyo street photographer describe their world?”

**PersonaSwap** is an AI-powered taste persona generator. You describe any fictional or real persona, and the app:

- Generates a **cultural profile & narrative** using **Gemini**
- Enriches it with **real-world taste insights** using **Qloo**
- Displays a complete lifestyle snapshot (music, dining, film, travel, etc.)

---

## 💡 Why Is It Innovative?

🔗 **Fusion of LLM + Taste AI**  
> Not just text generation — actual human behavior predictions from real-world data

🎭 **Persona Simulation**  
> Go beyond ChatGPT — simulate how a person would live, feel, and experience culture

🌍 **Universal Use Cases**  
> Useful for marketers, storytellers, creators, sociologists, and personalization tech

---

## 🛠️ Tech Stack

| Layer        | Tool                    |
|-------------|--------------------------|
| LLM         | Google Gemini (via API)  |
| Taste Data  | Qloo Taste AI API        |
| Backend     | FastAPI (Python)         |
| Frontend    | React.js                 |
| Environment | `venv`, `.env`           |

---

## 🚀 Features

- 🎨 Persona Profile Generator (Gemini)
- 📡 Real-world Taste Preferences (Qloo)
- ✍️ Auto Narrative Generator
- 🧬 Ready for Embedding & Similarity Search (FAISS-ready)
- 🧪 Easily extendable with persona history & comparison


---

📌 Next Ideas
- 🎯 Save and compare personas
- 🧠 FAISS similarity embedding
- 🎨 Visualize Qloo results (images, cards)
- 🔄 Persona swap + empathy mode

---

📦 Environment Setup
1) Create a Python virtual environment
2) Add your API keys to a .env file inside backend
3) Inside virtual environment: pip install -r requirements.txt

---

## ✅ Run Instructions

### 🟢 Backend
cd backend
myenv\Scripts\activate
python run.py

### 🟢 Frontend
cd persona-frontend
myenv\Scripts\activate   (In another terminal)
npm run dev

