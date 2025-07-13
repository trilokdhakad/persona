# FastAPI app

from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Request
from app.graph import create_graph

app = FastAPI()
graph = create_graph()

@app.post("/persona")
async def generate_persona(request: Request):
    data = await request.json()
    persona_input = data.get("persona", "")
    
    result = graph.invoke({"persona_input": persona_input})
    return result
