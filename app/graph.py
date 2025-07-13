from langgraph.graph import StateGraph
from typing import TypedDict, Any

from app.steps.generate_persona import generate_persona_node
from app.steps.query_qloo import query_qloo_node
from app.steps.generate_narrative import generate_narrative_node

# Define the schema for LangGraph state
class PersonaState(TypedDict):
    persona_input: str
    persona_profile: Any
    qloo_data: Any
    narrative: str

def create_graph():
    builder = StateGraph(PersonaState)  # Pass the schema here

    builder.add_node("generate_persona", generate_persona_node)
    builder.add_node("query_qloo", query_qloo_node)
    builder.add_node("generate_narrative", generate_narrative_node)

    builder.set_entry_point("generate_persona")
    builder.add_edge("generate_persona", "query_qloo")
    builder.add_edge("query_qloo", "generate_narrative")
    builder.set_finish_point("generate_narrative")

    return builder.compile()
