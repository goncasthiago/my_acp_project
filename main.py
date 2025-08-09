from colorama import Fore
import asyncio
from acp_sdk.client import Client
from acp_sdk.models import Message, MessagePart

#async def example():
#    async with Client(base_url="http://localhost:8000") as client:
#        run = await client.run_sync(
#            agent="echo",
#            input=[Message(parts=[MessagePart(content="Hello")])]
#        )
#        print(run.output)

async def run_sync() -> None:
    async with Client(base_url="http://localhost:8001") as client:
        run = await client.run_sync(
            agent="policy_agent", 
            input="What is the waiting period for rehabilitation?"
        )
        print(Fore.YELLOW + run.output[0].parts[0].content + Fore.RESET)

if __name__ == "__main__":
    asyncio.run(run_sync())