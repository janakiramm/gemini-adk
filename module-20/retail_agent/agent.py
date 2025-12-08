from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool


# Tool Definitions
def get_product_details(product_name: str) -> str:
    """Gathers details about a product in the catalog."""
    details = {
        "tablet": "A lightweight productivity tablet featuring a holographic display and adaptive interaction systems.",
        "power hub": "A compact wireless charging pad supporting multi-device fast recharge and smart connectivity.",
        "boots": "Durable outdoor boots engineered for rough terrain with enhanced ankle support and shock absorption.",
        "earbuds": "Premium wireless earbuds with spatial audio optimization and wind-resistant microphone clarity.",
        "home assistant": "A voice-activated smart home console with automation routines, environmental sensors, and media streaming.",
    }
    return details.get(product_name.lower(), "Product details not found.")


def get_pricing_information(product_name: str) -> str:
    """Provides pricing information for a product."""
    prices = {
        "tablet": "$799.00",
        "power hub": "$59.99",
        "boots": "$129.50",
        "earbuds": "$149.99",
        "home assistant": "$219.00",
    }
    return prices.get(product_name.lower(), "Price not found.")


def get_product_information(product_name: str) -> str:
    """Fetches backend data like SKU or inventory."""
    backend_info = {
        "tablet": "SKU: HGTB-110, Inventory: 320 units",
        "power hub": "SKU: WPHB-224, Inventory: 1500 units",
        "boots": "SKU: TRBT-441, Inventory: 610 units",
        "earbuds": "SKU: STED-803, Inventory: 1025 units",
        "home assistant": "SKU: ASHB-195, Inventory: 275 units",
    }
    return backend_info.get(product_name.lower(), "Backend information not found.")




# Define the Root Agent
root_agent = LlmAgent(
    name="RetailAgent",
    model="gemini-2.5-flash",
    description="An agent that provides details and prices for various products.",
    instruction="""
You are a helpful customer support agent specializing in product information.

You may only use the tools provided to you when the user asks about product
details, pricing, and backend inventory information.

Be concise, friendly, and helpful.
""",
    tools=[
#        get_product_details, #Uncomment this line after the eval
        get_pricing_information,
        get_product_information,
    ]
)