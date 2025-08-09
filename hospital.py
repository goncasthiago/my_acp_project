from acp_sdk.client import Client
import asyncio
from colorama import Fore 

async def run_hospital_workflow() -> None:
    async with Client(base_url="http://localhost:8001") as insurer, Client(base_url="http://localhost:8000") as hospital:
        run1 = await hospital.run_sync(
            agent="health_agent", input="Do I need rehabilitation after a shoulder reconstruction?"
        )
        content = run1.output[0].parts[0].content
        print(Fore.LIGHTMAGENTA_EX+ content + Fore.RESET)

        run2 = await insurer.run_sync(
            agent="policy_agent", input=f"Context: {content} What is the waiting period for rehabilitation?"
        )
        print(Fore.YELLOW + run2.output[0].parts[0].content + Fore.RESET)
asyncio.run(run_hospital_workflow())

#log
#uv run hospital.py
#Yes, rehabilitation is needed after a shoulder reconstruction.
#The waiting period for rehabilitation after a shoulder reconstruction is generally 2 months. However, if the shoulder reconstruction is for a pre-existing condition, there will be a waiting period of 12 months. Please consult with your insurer or medical provider to confirm the specific circumstances related to your condition and your insurance policy.