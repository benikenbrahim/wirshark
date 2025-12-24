import asyncio
from aiocoap import Context, Message, GET

async def main():
    context = await Context.create_client_context()

    while True:
        request = Message(
            code=GET,
            uri="coap://127.0.0.1:5683/sensors/temp"
        )

        response = await context.request(request).response
        print("Temperature CoAP :", response.payload.decode())

        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
