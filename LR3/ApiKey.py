import os
from dotenv import load_dotenv

def getApiKey():
    load_dotenv()
    apiKey = os.getenv("OPENWEATHERMAP_API_KEY")
    return apiKey
