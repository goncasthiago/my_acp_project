import asyncio
#import nest_asyncio
from acp_sdk.client import Client
from colorama import Fore 

#nest_asyncio.apply() 

async def run_doctor_workflow() -> None:
    async with Client(base_url="http://localhost:8000") as hospital:
        run1 = await hospital.run_sync(
            agent="doctor_agent", input="I'm based in Atlanta,GA. Are there any Cardiologists near me?"
        )
        #print(run1)
        content = run1.output[0].parts[0].content
        print(Fore.LIGHTMAGENTA_EX+ content + Fore.RESET)

asyncio.run(run_doctor_workflow())

