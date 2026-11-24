import asyncio

from agents import Agent, Runner

agent = Agent(name="conversation agent", 
              instructions="a user will ask you questions about the e commerce website. the refund policy is only in the first week. User can also ask history questions. So you are allowed to answer either history questions or question about refund policy. Anything else asked by the user should be repsonded with \"Sorry can't help you with that. Anything else i can help you with? \"",
              model="gpt-6.2-sol")

async def main() -> None:
    result = await Runner.run(agent, "When did Roman empire fall?")
    print(result.final_output)
    
if __name__ == "__main__":
    asyncio.run(main())