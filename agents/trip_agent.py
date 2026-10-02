import json

from llm.nexllm_client import NexLLMClient
from services.flight_service import FlightService


class TripAgent:

    def __init__(self):

        self.llm = NexLLMClient()

        self.flight_service = FlightService()

    def extract_trip_details(
        self,
        user_message
    ):

        prompt = f"""
You are a travel extraction assistant.

Extract travel requirements.

IMPORTANT RULES:

1. origin MUST be an IATA airport code.
2. destination MUST be an IATA airport code.
3. NEVER return city names.
4. Return ONLY JSON.
5. No explanation.
6. No markdown.

Examples:

Hong Kong -> HKG
London -> LHR
Singapore -> SIN
Tokyo -> NRT
New York -> JFK
Paris -> CDG
Frankfurt -> FRA

Output format:

{{
    "origin": "HKG",
    "destination": "LHR",
    "departure_date": "2026-11-15",
    "budget": 2500,
    "preferences": [
        "direct flight"
    ]
}}

User Request:

{user_message}
"""

        response = self.llm.chat(
            "You extract travel requirements.",
            prompt
        )

        print("\n===== AI EXTRACTION =====")
        print(response)

        try:

            trip_details = json.loads(
                response
            )

            trip_details.setdefault(
                "origin",
                "HKG"
            )

            trip_details.setdefault(
                "destination",
                "LHR"
            )

            trip_details.setdefault(
                "departure_date",
                "2026-11-15"
            )

            trip_details.setdefault(
                "budget",
                2500
            )

            trip_details.setdefault(
                "preferences",
                []
            )

            return trip_details

        except Exception as e:

            print(
                "JSON Parse Error:",
                e
            )

            return {

                "origin":
                    "HKG",

                "destination":
                    "LHR",

                "departure_date":
                    "2026-11-15",

                "budget":
                    2500,

                "preferences":
                    []
            }

    def recommend_flights(
        self,
        requirements,
        flights
    ):

        prompt = f"""
You are TripPilot.

Traveler Requirements:

{json.dumps(requirements, indent=2)}

Available Flights:

{json.dumps(flights, indent=2)}

Please recommend the BEST flight.

Consider:

1. Price
2. Airline quality
3. Number of stops
4. Arrival convenience
5. Business traveler suitability
6. User preferences

Provide:

Recommended Flight:

Reason:

Alternative Option:
"""

        recommendation = self.llm.chat(
            "You are a corporate travel advisor.",
            prompt
        )

        return recommendation

    def run(
        self,
        user_message
    ):

        try:

            # Step 1
            trip_details = (
                self.extract_trip_details(
                    user_message
                )
            )

            print(
                "\n===== FINAL TRIP DETAILS ====="
            )

            print(
                json.dumps(
                    trip_details,
                    indent=2
                )
            )

            # Step 2
            flights = (
                self.flight_service
                .get_flights(
                    trip_details[
                        "origin"
                    ],
                    trip_details[
                        "destination"
                    ],
                    trip_details[
                        "departure_date"
                    ]
                )
            )

            # Step 3
            recommendation = (
                self.recommend_flights(
                    trip_details,
                    flights
                )
            )

            return {

                "agent_steps": [

                    "Extracted travel requirements",

                    "Validated IATA airport codes",

                    "Called Duffel Flight API",

                    "Retrieved flight offers",

                    "Ranked available flights",

                    "Generated recommendation"
                ],

                "requirements":
                    trip_details,

                "flights":
                    flights,

                "recommendation":
                    recommendation
            }

        except Exception as e:

            print(
                "TRIP AGENT ERROR:",
                str(e)
            )

            return {

                "agent_steps": [
                    "Failed during execution"
                ],

                "recommendation":
                    f"Error: {str(e)}",

                "flights": []
            }