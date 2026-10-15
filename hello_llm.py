import os
import sys
from dotenv import load_dotenv
from groq import Groq

# Ensure UTF-8 output on Windows terminals to prevent UnicodeEncodeError
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# 1. Load environment variables
load_dotenv()

# 2. Get the API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

# 3. Initialize the Groq client
client = Groq(api_key=api_key)

# 4. Make an LLM API call
# Note: Available models on Groq include 'openai/gpt-oss-120b', 'openai/gpt-oss-20b', 'qwen/qwen3.8-27b'
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Python tutor."
        },
        {
            "role": "user",
            "content": "Explain Python virtual environments in 3 points."
        }
    ],
    # temperature=0.7,
    # max_tokens=200
)

# 5. Print the generated response
print("LLM Response:")
print(response.choices[0].message.content)

# 6. Print token usage
print("\nToken Usage:")
print("Input tokens:", response.usage.prompt_tokens)
print("Output tokens:", response.usage.completion_tokens)
print("Total tokens:", response.usage.total_tokens)
