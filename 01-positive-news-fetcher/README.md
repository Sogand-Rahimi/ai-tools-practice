# AI Positive News Fetcher

An interactive Python CLI tool that uses OpenAI's API with Web Search capabilities to fetch up-to-date positive news on any topic and save the results locally.

---

## Key Features

* **Real-Time Web Search:** Uses OpenAI's `web_search` tool to fetch live, current news.
* **Interactive CLI:** Prompts the user for topics and optional local file export.
* **Secure Authentication:** Utilizes environment variables (`OPENAI_API_KEY`) to keep credentials safe.

---

## How to Run

1. Set your OpenAI API key in your terminal environment:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"  # Mac/Linux
   set OPENAI_API_KEY="your-api-key-here"     # Windows Command Prompt
   $env:OPENAI_API_KEY="your-api-key-here"    # Windows PowerShell
