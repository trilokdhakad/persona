from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .generate_persona import generate_profile
from .models import PersonaRequest, PersonaProfile
from .storage import save_persona, load_all_personas

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 Temporarily allow all origins during dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/persona")
def persona_endpoint(req: PersonaRequest):
    # MOCK Gemini + Qloo responses for now
    profile = {
        "persona": req.persona,
        "summary": f"Mock summary for persona: {req.persona}",
        "qloo_data": {
            "music": ["Kendrick Lamar", "Radiohead"],
            "movies": ["Inception", "Spirited Away"]
        }
    }
    save_persona(profile)
    return profile

@app.get("/personas")
def get_all_personas():
    return load_all_personas()
