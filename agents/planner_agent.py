from llm.nexllm_client import (
    NexLLMClient
)

from tools.flight_search import (
    FlightSearchTool
)


class FlightRecommendationAgent:

    def __init__(self):

        self.llm = NexLLMClient()

    def recommend(
        self,
        origin,
        destination,
        date
    ):

        flight_search_tool = FlightSearchTool()
        flights = flight_search_tool.search_flights(
            origin,
            destination,
            date
        )

        result = self.llm.chat(
            "You are a corporate travel advisor.",
            f"""

            Available flights:

            {flights}

            Recommend the best option.
            """
        )

        return result