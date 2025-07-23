import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NasaNeoClient:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.getenv("NASA_API_KEY")
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov/neo/rest/v1/feed"

    def get_neo_feed(self, start_date=None, end_date=None):
        params = {"api_key": self.api_key}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        response = requests.get(self.base_url, params=params)
        return response.json()
