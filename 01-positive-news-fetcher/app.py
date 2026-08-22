import datetime
import os
from openai import OpenAI


def get_news(topic="positive news"):
    """Fetch real-time news for a given topic using OpenAI API and web search."""
    # Automatically reads OPENAI_API_KEY from environment variables
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5",
        tools=[{"type": "web_search"}],
        input=f"What is a positive news story about {topic} today?",
    )

    return response.output_text


def save_news(topic, news):
    """Save the retrieved news summary to a timestamped text file."""
    date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{topic.replace(' ', '_')}_{date}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(news)

    print(f"\nNews saved to {filename}")


def main():
    print("=== AI Positive News Fetcher ===")
    topic = input(
        "Enter a topic for positive news (or press Enter for default): "
    )

    if not topic.strip():
        topic = "positive news"

    news = get_news(topic)

    print("\n--- Latest News ---\n")
    print(news)

    save = input("\nDo you want to save this news to a file? (y/n): ")
    if save.lower() == "y":
        save_news(topic, news)


if __name__ == "__main__":
    main()
