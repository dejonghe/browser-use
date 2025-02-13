from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
from pydantic import SecretStr
import os
from dotenv import load_dotenv
load_dotenv()
import asyncio
from helpers import *

api_key = os.getenv("GEMINI_API_KEY")
chrome_instance_path = os.getenv("CHROME_INSTANCE_PATH")
chrome_profile = os.getenv("CHROME_PROFILE")

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Chrome executable
        chrome_instance_path=chrome_instance_path,  # linux
        extra_chromium_args=[f"--profile-directory='{chrome_profile}'"] # needed to go to chrome://version in the profile I wanted to find the right profile dir path (it's not the pretty name you set in chrome)
    )
)

async def main(task):
    agent = Agent(
        task=task,
        llm=llm,
        browser=browser,
    )
    result = await agent.run()
    print(result)

@time_it
def start_task_execution(task):
    loop = asyncio.new_event_loop()  # Create a new event loop
    asyncio.set_event_loop(loop)  # Set it as the current event loop
    loop.run_until_complete(main(task))  # Run the coroutine

if __name__ == "__main__":
    user_task = input("Enter the task you want to perform: ")  # Take task input from the user
    start_task_execution(user_task)