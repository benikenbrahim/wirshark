import asyncio
import random
from aiocoap import resource, Context, Message

class TempResource(resource.Resource):
    async def render_get(self, request):
        temp = round(random.uniform(20, 30), 2)
        return Message(payload=str(temp).encode())

async def main():
    root = resource.Site()
    root.add_resource(['sensors', 'temp'], TempResource())

    # FIX Windows : bind explicite
    await Context.create_server_context(
        root,
        bind=("127.0.0.1", 5683)
    )

    print("Serveur CoAP (capteur) actif sur 127.0.0.1:5683")
    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
