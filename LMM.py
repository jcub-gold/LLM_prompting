import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

load_dotenv()

class Gemini:
    def __init__(self, model):
        self.model = genai.GenerativeModel(model)
        self.api_key = os.getenv("GOOGLE_API_KEY")

    def generate_response(self, prompt):
        genai.configure(api_key=self.api_key)
        response = self.model.generate_content(prompt)
        return response.text

class GPT:
    def __init__(self, model):
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key = self.api_key)

    def generate_response(self, prompt):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}])
        return response.choices[0].message.content

