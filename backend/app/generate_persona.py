import os
from dotenv import load_dotenv
import google.generativeai as genai
import requests

load_dotenv()

# Gemini
genai.configure(api_key=os.getenv("VITE_GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

# Qloo
VITE_QLOO_API_KEY = os.getenv("VITE_QLOO_API_KEY")
QLOO_ENTITY = "FCE8B172-4795-43E4-B222-3B550DC05FD9"  # Example: New York


def fetch_qloo_insights(entity_urn, location_query="New York"):
    url = "https://api.qloo.com/v2/insights/"
    headers = {"X-Api-Key": VITE_QLOO_API_KEY}
    params = {
        "filter.type": "urn:entity:place",
        "signal.interests.entities": entity_urn,
        "filter.location.query": location_query
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Qloo API request failed", "status": response.status_code}


def generate_profile(prompt):
    system_prompt = f"Create a detailed cultural and lifestyle profile and a story for: {prompt}"
    response = model.generate_content(system_prompt)
    text = response.text

    qloo = fetch_qloo_insights(QLOO_ENTITY)

    return {
        "persona_profile": text,
        "qloo_data": qloo,
        "narrative": text.split("\n\n")[-1]
    }