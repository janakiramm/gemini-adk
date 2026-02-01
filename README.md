# Gemini and ADK Tutorial Series

Code samples and Jupyter notebooks for the [Gemini and ADK video tutorial series](https://www.youtube.com/watch?v=vPXRYYD9omk&list=PLF3s2WICJlqP03Ovndv-dnO7OfFYnmi3Y) on YouTube.

## Overview

This repository provides hands-on examples covering Google's Gemini API and Agent Development Kit (ADK). The content progresses from foundational API usage through advanced agentic patterns, making it suitable for developers at various experience levels.

## Prerequisites

- Python 3.9+
- Google Cloud account with Gemini API access
- API keys for Gemini (and optionally OpenAI, Groq for multi-LLM modules)

## Repository Structure

### Part 1: Gemini API Fundamentals

| Module | Topic | Contents |
|--------|-------|----------|
| **module-2** | API Access Methods | Native Gemini API, OpenAI compatibility layer, Vertex AI integration |
| **module-3** | Prompting | Basic prompts, prompt engineering techniques, thinking/reasoning |
| **module-4** | Structured Outputs | JSON responses, JSON Schema, Pydantic models |
| **module-5** | RAG & Search | Retrieval-augmented generation, search integration |
| **module-6** | Function Calling | Manual invocation, automated calling, Flight API example |

### Part 2: Agent Development Kit (ADK)

| Module | Topic | Contents |
|--------|-------|----------|
| **module-13** | ADK Basics | Getting started with ADK, weather/time agent example |
| **module-14** | Multi-LLM Support | Using Groq and OpenAI models with ADK |
| **module-15** | Session Management | In-memory sessions, database-backed sessions |
| **module-16** | Memory | Agent memory and context persistence |
| **module-17** | Tools | Custom tools, agent-as-tool pattern |
| **module-18** | MCP Integration | Model Context Protocol with ADK |
| **module-19** | Callbacks & Responses | Event callbacks, response handling |
| **module-20** | Complete Agent | Full retail agent implementation |

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/janakiramm/gemini-adk.git
   cd gemini-adk
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies for a specific module:
   ```bash
   cd module-2
   pip install -r requirements.txt
   ```

4. Configure your API key:
   ```bash
   export GOOGLE_API_KEY="your-api-key"
   ```

5. Launch Jupyter and open the notebooks:
   ```bash
   jupyter notebook
   ```

## Video Series

Watch the complete tutorial series on YouTube:  
[Gemini and ADK Playlist](https://www.youtube.com/watch?v=vPXRYYD9omk&list=PLF3s2WICJlqP03Ovndv-dnO7OfFYnmi3Y)

## Resources

- [Google Gemini API Documentation](https://ai.google.dev/docs)
- [Agent Development Kit (ADK) Documentation](https://google.github.io/adk-docs/)
- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)

## License

This project is provided for educational purposes as companion material to the video series.

## Author

[Janakiram MSV](https:www.janakiram.com)
