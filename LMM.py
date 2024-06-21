import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

load_dotenv()

class Gemini:
    def __init__(self, **kwargs):
        self.api_key = os.getenv("GOOGLE_API_KEY")

        allowed_attributes = {'model': 'gemini-pro'}
        
        for key, value in kwargs.items():
            if key in allowed_attributes:
                setattr(self, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
            
        for key in allowed_attributes:
            if not hasattr(self, key):
                setattr(self, key, allowed_attributes[key])

    def generate_response(self, **kwargs):
        model = genai.GenerativeModel(self.model)
        genai.configure(api_key=self.api_key)

        allowed_attributes = {'prompt': ''}
        
        for key, value in kwargs.items():
            if key in allowed_attributes:
                setattr(self, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
            
        for key in allowed_attributes:
            if not hasattr(self, key):
                setattr(self, key, allowed_attributes[key])

        response = model.generate_content(self.prompt)
        return response.text

    def get_model(self):
        return self.model

class GPT:
    def __init__(self, **kwargs):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key = self.api_key)
        
        allowed_attributes = {'model': 'gpt-3.5-turbo'}
        
        for key, value in kwargs.items():
            if key in allowed_attributes:
                setattr(self, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
            
        for key in allowed_attributes:
            if not hasattr(self, key):
                setattr(self, key, allowed_attributes[key])

    def generate_response(self, **kwargs):
        allowed_attributes = {'prompt': ''}
        
        for key, value in kwargs.items():
            if key in allowed_attributes:
                setattr(self, key, value)
            else:
                raise AttributeError(f"Invalid attribute: {key}")
            
        for key in allowed_attributes:
            if not hasattr(self, key):
                setattr(self, key, allowed_attributes[key])
                
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": self.prompt}])
        return response.choices[0].message.content

