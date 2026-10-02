import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class NexLLMClient:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "NEXLLM_API_KEY"
            ),
            base_url=os.getenv(
                "NEXLLM_BASE_URL"
            )
        )

        self.chat_model = os.getenv(
            "NEXLLM_CHAT_MODEL"
        )

    def chat(
        self,
        system_prompt,
        user_prompt
    ):

        response = (
            self.client.chat.completions.create(
                model=self.chat_model,

                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )