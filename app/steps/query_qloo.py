# Qloo API wrapper

import os
import httpx

QLOO_API_KEY = os.getenv("QLOO_API_KEY")

def query_qloo_node(state):
    # Ideally you'd extract relevant tags from persona_profile
    # For now, use hardcoded example or parse JSON if needed
    entities = ["FCE8B172-4795-43E4-B222-3B550DC05FD9"]  # Replace with real entity IDs from Qloo
    headers = {"X-Api-Key": QLOO_API_KEY}

    url = f"https://api.qloo.com/v2/insights/?filter.type=urn:entity:place&signal.interests.entities={entities[0]}&filter.location.query=New%20York"
    
    with httpx.Client() as client:
        r = client.get(url, headers=headers)
        data = r.json()
    
    return {"qloo_data": data}
