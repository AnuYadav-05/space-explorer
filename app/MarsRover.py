import os
import requests
from dotenv import load_dotenv

load_dotenv()

class MarsRoverClient:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.getenv("NASA_API_KEY")
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers"

    def get_photos(self, rover="curiosity", sol=1000, camera=None):
        url = f"{self.base_url}/{rover}/photos"
        params = {"sol": sol, "api_key": self.api_key}
        if camera:
            params["camera"] = camera
        response = requests.get(url, params=params)
        return response.json()
