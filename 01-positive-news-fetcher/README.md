Markdown
# AI Positive News Fetcher

An interactive Python CLI tool that uses OpenAI's API with Web Search capabilities to fetch up-to-date positive news on any topic and save the results locally.

---

## Key Features

* **Real-Time Web Search:** Uses OpenAI's `web_search` tool to fetch live, current news.
* **Interactive CLI:** Prompts the user for topics and optional local file export.
* **Secure Authentication:** Utilizes environment variables (`OPENAI_API_KEY`) to keep credentials safe.

---

## Prerequisites & Installation

Make sure you have Python 3.8 or higher installed along with the required dependencies:

```bash
pip install openai
How to Run
Set your OpenAI API key in your terminal environment:

Bash
export OPENAI_API_KEY="your-api-key-here"  # Mac/Linux
set OPENAI_API_KEY="your-api-key-here"     # Windows Command Prompt
$env:OPENAI_API_KEY="your-api-key-here"    # Windows PowerShell
Run the script:

Bash
python main.py
Follow the on-screen prompts to enter a news topic and choose whether to save the results to a file.


<FollowUp label="Would you like to review or complete the README for any other project in your repo?" query="Can you help me complete the README for another project in my repository?"/>
