import os
from dotenv import load_dotenv
import google.auth
from google.auth.transport.requests import Request
from openai import OpenAI

load_dotenv()

# Programmatically get an access token
creds, project = google.auth.default()
auth_req = google.auth.transport.requests.Request()
creds.refresh(auth_req)

# Replace these placeholders with your actual values
PROJECT = os.getenv("PROJECT")
LOCATION = os.getenv("LOCATION")
MODEL_ID = os.getenv("MODEL_ID")

# Initialize the OpenAI client
client = OpenAI(
    base_url = f'https://{LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT}/locations/{LOCATION}/endpoints/openapi',
    api_key = creds.token
)

# Example usage of the client (modify as needed)
model_response = client.chat.completions.create(
  model = f"google/{MODEL_ID}",
  stream = True,
  messages = [{"role": "user", "content": "Write a story about a magic backpack." }]
)

print(model_response)
# client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
# model_response = client.chat.completions.create(
#   model = f"google/gemini-1.0-pro",
#   messages = [{"role": "user", "content": "Write a story about a magic backpack." }]
# )

# print(model_response)