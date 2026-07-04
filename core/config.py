import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CALLMISSED_API_KEY")
BASE_URL = "https://api.callmissed.com/v1"