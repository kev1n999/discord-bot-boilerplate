import os 
from dotenv import load_dotenv 
from client.client import DiscordClient 

load_dotenv()

if __name__ == "__main__":
    client = DiscordClient(os.getenv("BOT_TOKEN"))
    client.run_bot()