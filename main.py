import os
import httpx
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()
API_ID = os.getenv('api_id')
API_HASH = os.getenv('api_hash')
EM_CONTACT = os.getenv('emergency_contact')
client = TelegramClient('anon', API_ID, API_HASH)

async def send_msg(contact, msg: str):
        await client.send_message(contact, msg)

async def post_req(url, data, header):
        async with httpx.AsyncClient() as reqclient:
                res = await reqclient.post(url=url, json=data, headers=header)
        return res

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
                                url = "http://localhost:11434/api/generate"
                                header = {'Content-Type': 'application/json'}
                                data = {"model": "tinydolphin", "stream": False, "prompt": event.raw_text}

                                try:
                                        response = await post_req(url, data, header)
                                        await send_msg(sender.username, response.json()['response'])
                                except:
                                        print("Error!")

# AI vars
incoming_message_handler.started: bool = False

client.start()
client.run_until_disconnected()