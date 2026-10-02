from tools.flight_search import FlightSearchTool


class FlightService:

    def __init__(self):
        self.tool = FlightSearchTool()

    def get_flights(
        self,
        origin,
        destination,
        departure_date
    ):

        response = (
            self.tool.search_flights(
                origin,
                destination,
                departure_date
            )
        )

        flights = []

        for offer in response["data"][:5]:

            flights.append({

                "airline":
                    offer["owner"]["name"],

                "price":
                    offer["total_amount"],

                "currency":
                    offer["total_currency"]
            })

        return flights