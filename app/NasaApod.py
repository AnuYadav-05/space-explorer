import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NasaAPODClient:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.getenv("NASA_API_KEY")
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/planetary/apod"

    def get_apod(self, date=None):
        params = {"api_key": self.api_key}
        if date:
            params["date"] = date
        response = requests.get(self.base_url, params=params)
        return response.json()
