from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

root_agent = LlmAgent(
    model=LiteLlm(model="groq/llama-3.3-70b-versatile"), 
    name="groq_agent",
    instruction="You are a helpful assistant powered by Llama 3",
    description="agent to demonstrate the use of non Gemini-models"
)
