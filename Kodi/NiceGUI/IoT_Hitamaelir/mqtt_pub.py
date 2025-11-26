import asyncio
from aiomqtt import Client
from random import randint
import json

MQTT_BROKER = "IP_TALAN_A_RPI"
MQTT_TOPIC = "TOPIC-IÐ"

async def senda():
    async with Client(MQTT_BROKER) as client:
        while True:
            gogn = {"tala_a": randint(1, 100), "tala_b": randint(50, 60) }
            gogn = json.dumps(gogn)
            await client.publish(MQTT_TOPIC, payload=gogn)
            await asyncio.sleep(2)

async def main():
    asyncio.create_task(senda())

    while True:
        await asyncio.sleep(0.1)

asyncio.run(main())
