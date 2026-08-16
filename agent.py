import json
from google.adk.agents import LlmAgent

def search_menu(query: str) -> dict:
    """Searches the coffee shop menu for items matching the customer's request."""
    with open("menu.json", "r") as f:
        menu = json.load(f)

    query_words = query.lower().split()

    results = [
        item for item in menu
        if any(
            word in (
                item["name"] + " " +
                item["description"] + " " +
                " ".join(item["tags"]) + " " +
                " ".join(item["allergens"])
            ).lower()
            for word in query_words
        )
    ]

    return {"results": results}

root_agent = LlmAgent(
    name="barista_agent",
    model="gemini-3.7-flash",
    description="A helpful coffee shop barista agent.",
    instruction="""You are a friendly AI barista.
Help customers choose items from the coffee shop menu.
IMPORTANT:
- Always use the search_menu tool when the customer asks about menu items, ingredients, tags, or allergens.
- Base your recommendations only on information returned by the tool.
- Never invent menu items or ingredients.
- If you cannot find a suitable item, say so honestly.
- Be friendly, concise, and helpful.""",
    tools=[search_menu],
)
