import os
import requests
import time
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()
API_ID = os.getenv('api_id')
API_HASH = os.getenv('api_hash')
EM_CONTACT = os.getenv('emergency_contact')
client = TelegramClient('anon', API_ID, API_HASH)

async def send_msg(contact, msg: str):
        await client.send_message(contact, msg)

@client.on(events.NewMessage)
async def incoming_message_handler(event):
        sender = await event.get_sender()
        if sender.contact == True:
                if incoming_message_handler.started == False:
                        if '/start' in event.raw_text:
                                incoming_message_handler.started = True
                                await send_msg(sender.username, "[Session started]")
                                await send_msg(sender.username, "Hi! Let's chat!")
                else:
                        if '/end' in event.raw_text:
                                incoming_message_handler.started = False
                                incoming_message_handler.context = "Hi! Let's chat!"
                                await send_msg(sender.username, "[Session ended]")
                        else:
                                response = requests.post(url = "http://localhost:11434/api/generate", 
                                                        json = {"model": "tinydolphin", 
                                                                "stream": False, 
                                                                "context":incoming_message_handler.context, 
                                                                "prompt": event.raw_text
                                                                },
                                                        headers = {'Content-Type': 'application/json',}
                                                        )
                                
                                await send_msg(sender.username, response.json['response'])

# AI vars
incoming_message_handler.started: bool = False
incoming_message_handler.context: str = "Hi! Let's chat!"

client.start()
client.run_until_disconnected()

data = {
    'model': 'tinydolphin',
    'prompt': 'Why is the sky blue?',
    'stream': False
}