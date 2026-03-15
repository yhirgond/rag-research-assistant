import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class LLMHandler:
    def __init__(self, model: str = "llama3-8b-8192",
                 max_tokens: int = 1024,
                 temperature: float = 0.2):
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"
