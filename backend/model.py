from google import genai
import asyncio
from mcp_client import mcp_client
from dotenv import load_dotenv
import logging
from datetime import datetime

load_dotenv()

model = genai.Client()

def get_logger(response):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_filename = f"logs/app_log_{timestamp}.log"

    logging.basicConfig(
        filename=log_filename, 
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    logging.info(f"Model Invoked: {response}", exc_info=True)

async def invoke_model(user_query: str):
    async with mcp_client:
        response = await model.aio.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"You are a Employee Portal Manager, you ONLY answer questions related to the portal. Any question not related to the portal is responded with a generic fallback response `IDIOT, I'm not supposed to answer that!`. Now answer the question: {user_query}",
            config=genai.types.GenerateContentConfig(
                temperature=0,
                tools=[mcp_client.session]
            ),
        )

        get_logger(response)

        return response.text

if __name__ == "__main__":
    print(asyncio.run(invoke_model("What is Nishant's height?")))