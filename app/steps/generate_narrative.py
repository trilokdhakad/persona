# Final GPT output


from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_narrative_node(state):
    persona = state.get("persona_profile")
    qloo = state.get("qloo_data")

    prompt = f"""
    Based on the following persona profile and taste data, generate a narrative that describes what a day in the life of this persona might look like:

    Persona: {persona}
    Qloo Recommendations: {qloo}

    Write a short, vivid paragraph.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"narrative": response.choices[0].message.content}
