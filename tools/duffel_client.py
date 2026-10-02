import os
import requests


class DuffelClient:

    def __init__(self):

        self.base_url = os.getenv(
            "DUFFEL_BASE_URL"
        )

        self.api_key = os.getenv(
            "DUFFEL_API_KEY"
        )

        self.headers = {

            "Authorization":
                f"Bearer {self.api_key}",

            "Duffel-Version":
                "v2",

            "Content-Type":
                "application/json"
        }