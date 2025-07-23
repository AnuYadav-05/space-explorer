import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

class GeminiClient:
    def __init__(self, api_key=None, model="gemini-2.5-flash-lite"):
        if api_key is None:
            api_key = os.getenv("apiKey-Gem")
        self.api_key = api_key
        self.model = model
        self.client = genai.Client(api_key=self.api_key)

    def ask(self, prompt):
        suffix = "The question might be related to space so please answer accordingly: "
        response = self.client.models.generate_content(
            model=self.model,
            contents=suffix + prompt
        )
        return response.text
