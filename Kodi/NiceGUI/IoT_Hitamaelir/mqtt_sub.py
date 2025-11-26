import asyncio
from aiomqtt import Client
from random import randint

MQTT_BROKER = "IP_TALAN_A_RPI"
MQTT_TOPIC = "TOPIC-IÐ"

async def mottaka():
    async with Client(MQTT_BROKER) as client:
        while True:
            await client.subscribe(MQTT_TOPIC)
            async for message in client.messages:
                print(message.payload)

async def main():
    asyncio.create_task(mottaka())

    while True:
        await asyncio.sleep(0.1)

asyncio.run(main())
