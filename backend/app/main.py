from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .generate_persona import generate_profile
from pydantic import BaseModel

app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class PersonaRequest(BaseModel):
    persona: str

@app.post("/persona")
def persona_endpoint(req: PersonaRequest):
    return generate_profile(req.persona)