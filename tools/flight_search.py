from tools.duffel_client import (
    DuffelClient
)

import requests


class FlightSearchTool:

    def __init__(self):

        self.client = DuffelClient()

    def search_flights(
        self,
        origin,
        destination,
        departure_date
    ):

        payload = {

            "data": {

                "slices": [

                    {
                        "origin":
                            origin,

                        "destination":
                            destination,

                        "departure_date":
                            departure_date
                    }
                ],

                "passengers": [
                    {
                        "type": "adult"
                    }
                ],

                "cabin_class":
                    "economy"
            }
        }

        response = requests.post(

            f"{self.client.base_url}/air/offer_requests",

            headers=self.client.headers,

            json=payload
        )

        print("Status:", response.status_code)
        print("Response:")
        print(response.text)

        response.raise_for_status()

        request_result = (
            response.json()
        )

        offer_request_id = (
            request_result["data"]["id"]
        )

        offers = requests.get(

            f"{self.client.base_url}/air/offers",

            headers=self.client.headers,

            params={
                "offer_request_id":
                    offer_request_id
            }
        )

        offers.raise_for_status()

        return offers.json()