
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# 1. Load environment variables
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

# 2. Get the API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

# 3. Initialize the Groq client
client = Groq(api_key=api_key)

# 4. Make an LLM API call
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Python tutor."
        },
        {
            "role": "user",
            "content": (
                "Explain Python in detail. Cover its history, features, "
                "applications, advantages, and limitations."
            )
        }
    ],
    temperature=0.7,
    max_tokens=100
)

# 5. Print the generated response
print("LLM Response:")
print(response.choices[0].message.content)

# 6. Check why generation stopped
finish_reason = response.choices[0].finish_reason

print("\nFinish Reason:", finish_reason)

if finish_reason == "length":
    print("Token limit hit! The response stopped because "
          "the maximum output token limit was reached.")
elif finish_reason == "stop":
    print("The model finished its response normally.")
else:
    print("Generation stopped for another reason:", finish_reason)

# 7. Print token usage
print("\nToken Usage:")
print("Input tokens:", response.usage.prompt_tokens)
print("Output tokens:", response.usage.completion_tokens)
print("Total tokens:", response.usage.total_tokens)