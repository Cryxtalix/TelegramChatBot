import httpx
import asyncio

async def post_req(url, data, header):
    async with httpx.AsyncClient() as reqclient:
        res = await reqclient.post(url=url, json=data, headers=header)
    return res

async def main():
    url = "http://localhost:11434/api/generate"
    header = {'Content-Type': 'application/json'}
    data = {"model": "tinydolphin", "stream": False, "prompt": "Hello, how are you?"}

    response = await post_req(url, data, header)
    print(response.json()['response'])

# Run the event loop
asyncio.run(main())