# GPT-4 prompt

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_persona_node(state):
    persona_input = state.get("persona_input")
    
    prompt = f"""
    Create a cultural taste profile for this persona: "{persona_input}".
    List preferences in:
    - Music
    - Movies
    - Fashion
    - Food
    - Travel
    Return a JSON object.
    """
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"persona_profile": response.choices[0].message.content}
