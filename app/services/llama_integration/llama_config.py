import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_URL = os.getenv("LLAMA_API_URL")

# Model Configuration
MODEL_NAME = "llama3"

# Headers for the API
HEADERS = {
    "Content-Type": "application/json"
}
