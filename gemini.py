from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

class OpenRouterModel:
    def generate_content(self, prompt):
        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-20b:free",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an AI Career Mentor. Give clear, professional and beginner-friendly answers."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1000
            )

            class Result:
                text = response.choices[0].message.content

            return Result()

        except Exception as e:
            raise Exception(f"OpenRouter Error: {e}")

model = OpenRouterModel()