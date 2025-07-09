import os
import asyncio
from google import genai
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

import warnings
warnings.filterwarnings("ignore")

MCP_SERVER_URL = "http://127.0.0.1:8000/mcp/"
client = genai.Client()

async def main():
    async with streamablehttp_client(MCP_SERVER_URL) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            prompt = "Who is the Intern in the company?"
            response = await client.aio.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[session],  # Pass the MCP session as a tool
                ),
            )
            print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
