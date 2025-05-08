from dotenv import load_dotenv
import os

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = os.getenv("DEEPSEEK_API_URL")

if not DEEPSEEK_API_KEY or not DEEPSEEK_API_URL:
    raise ValueError("Missing DeepSeek API key or URL.")



DATABASE_URL = "sqlite:///./test.db"  # Replace with your database URL
SECRET_KEY = "your_secret_key"  # Replace with a secure key
ALGORITHM = "HS256"