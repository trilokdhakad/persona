from pydantic import BaseModel

class PersonaRequest(BaseModel):
    persona: str

class PersonaProfile(BaseModel):
    persona: str
    summary: str
    qloo_data: dict