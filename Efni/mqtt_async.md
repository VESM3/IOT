# mqtt_as 

- [Uppsetning](./mqtt_async.md#uppsetning)
- [Sending](./mqtt_async.md#sending)
    - [Með aðal while lykkjunni](./mqtt_async.md#sending-í-aðal-while-true-lykkjunni)
    - [Með falli](./mqtt_async.md#með-sérstöku-sendi-falli)
- [Móttaka](./mqtt_async.md#móttaka)
- [Tvíátta samskipti](./mqtt_async.md#tvíátta-samskipti)

## Uppsetning
<!--
### Aðferð I
Afrita [\_\_init\_\_.py](https://github.com/peterhinch/micropython-mqtt/blob/master/mqtt_as/__init__.py) í `/lib/mqtt_as/` möppuna á ESP (búa til möppurnar ef þarf).
-->

Keyra þessa skrá á ESP (það þarf ekki að vista hana á ESP):
```python
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect("TskoliVESM", "Fallegurhestur")
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
do_connect()

import mip
mip.install("github:peterhinch/micropython-mqtt")
```

Smella svo á "Refresh" í hamborgara menu fyrir MicroPython device.

## Sending

### Sending í aðal `while True` lykkjunni
```python
from mqtt_as import MQTTClient, config
import asyncio

# WIFI stillingar
config["ssid"] = "TskoliVESM"
config["wifi_pw"] = "Fallegurhestur"

# MQTT þjónninn
config["server"] = "test.mosquitto.org" # eða broker.emqx.io (þarf að vera það sama á sendir og móttakara)
TOPIC = "XXXXkynning" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna

async def main(client):
    # tengjast við þráðlausa netið
    await client.connect()
    teljari = 0
    while True:
        # Skilaboðin sem á að senda, nota string encode aðferð til að breyta í bytes objects.
        skilabod = f"Halló {teljari}".encode() # þarf encode ef senda á íslenska stafi
        print(f"sendi: {skilabod}" )
        # Skilaboðin send
        await client.publish(TOPIC, skilabod)
        # Sendi á tveggja sekúnda fresti
        await asyncio.sleep_ms(2000)
        teljari += 1

# Sýnir ýmsar upplýsingar eins og t.d. varðandi nettenginguna og minnisnotkun  
MQTTClient.DEBUG = True

# Búa til tilvik af MQTTClient og senda inn stillingarnar
client = MQTTClient(config)

# mqtt_as styður ekki context manager og því þarf að hafa try/finally í stað with
try:
    # Ræsa async main fallið og senda þangað tilvik af client-num
    asyncio.run(main(client))
finally:
    client.close()
```

### Með sérstöku sendi falli

```python
from mqtt_as import MQTTClient, config
import asyncio

# WIFI stillingar
config["ssid"] = "TskoliVESM"
config["wifi_pw"] = "Fallegurhestur"

# MQTT þjónninn
config["server"] = "test.mosquitto.org" # eða broker.emqx.io (þarf að vera það sama á sendir og móttakara)
TOPIC = "XXXXkynning" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna

async def sendir(client):
    teljari = 0
    while True:
        # Skilaboðin sem á að senda, þarf encode ef senda á íslenska stafi
        skilabod = f"Halló {teljari}".encode() 
        print(f"sendi: {skilabod}" )
        # Skilaboðin send
        await client.publish(TOPIC, skilabod)
        # Sendi á tveggja sekúnda fresti
        await asyncio.sleep_ms(2000)
        teljari += 1

async def main(client):
    # tengjast við þráðlausa netið
    await client.connect()
    # búa til task
    asyncio.create_task(sendir(client))
    while True:
        # Ekkert að gera hér
        await asyncio.sleep_ms(0)

# Sýnir ýmsar upplýsingar eins og t.d. varðandi nettenginguna og minnisnotkun  
MQTTClient.DEBUG = True

# Búa til tilvik af MQTTClient og senda inn stillingarnar
client = MQTTClient(config)

try:
    # Ræsa async main fallið og senda þangað tilvik af client-num
    asyncio.run(main(client))
finally:
    client.close()
```

## Móttaka

```python
from mqtt_as import MQTTClient, config
import asyncio

# WIFI stillingar
config["ssid"] = "TskoliVESM"
config["wifi_pw"] = "Fallegurhestur"

# MQTT þjónninn
config["server"] = "test.mosquitto.org" # eða broker.emqx.io (þarf að vera það sama á sendir og móttakara)
config["queue_len"] = 1
TOPIC = "XXXXkynning" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna
TOPIC_2 = "YYYYkynning"

# Fallið meðhöndlar skilaboð sem berast
async def mottakari(client):
    # skilaboðin berast í biðröð (e. queue) sem við sækjum þau úr
    async for topic, skilabod, _ in client.queue:
        print(topic.decode(), skilabod.decode())

# Fallið sér um að gerast ákrifandi að topic-um og viðhalda áskriftinni ef tenging tapast
async def askrift(client):
    while True:
        await client.up.wait()
        client.up.clear()
        # Topik-ið (eitt eða fleiri) sem á að gerast áskrifandi að
        await client.subscribe(TOPIC, 1) 
        # await client.subscribe(TOPIC_2, 1) 

async def main(client):
    # tengjast við þráðlausa netið
    await client.connect()
    # búa til task
    asyncio.create_task(askrift(client))
    asyncio.create_task(mottakari(client))
    while True:
        # Ekkert að gera hér
        await asyncio.sleep_ms(0)

# Sýnir ýmsar upplýsingar eins og t.d. varðandi nettenginguna og minnisnotkun  
MQTTClient.DEBUG = True

# Búa til tilvik af MQTTClient og senda inn stillingarnar
client = MQTTClient(config)

try:
    # Ræsa async main fallið og senda þangað tilvik af client-num
    asyncio.run(main(client))
finally:
    client.close()
```

## Tvíátta samskipti

```python
from mqtt_as import MQTTClient, config
import asyncio

# WIFI stillingar
config["ssid"] = "TskoliVESM"
config["wifi_pw"] = "Fallegurhestur"

# MQTT þjónninn
config["server"] = "test.mosquitto.org" # eða broker.emqx.io (þarf að vera það sama á sendir og móttakara)
config["queue_len"] = 1
TOPIC_SENDING = "XXXXkynning" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna
TOPIC_MOTTAKA = "YYYYkynning"

# Fallið meðhöndlar skilaboð sem berast
async def mottakari(client):
    # skilaboðin berast í biðröð (e. queue) sem við sækjum þau úr
    async for topic, skilabod, _ in client.queue:
        print("móttek: ", topic.decode(), skilabod.decode())

async def sendir(client):
    teljari = 0
    while True:
        # Skilaboðin sem á að senda, þarf encode ef senda á íslenska stafi
        skilabod = f"Halló {teljari}".encode() 
        print(f"sendi: {skilabod}" )
        # Skilaboðin send
        await client.publish(TOPIC_SENDING, skilabod)
        # Sendi á tveggja sekúnda fresti
        await asyncio.sleep_ms(2000)
        teljari += 1

# Fallið sér um að gerast ákrifandi að topic-um og viðhalda áskriftinni ef tenging tapast
async def askrift(client):
    while True:
        await client.up.wait()
        client.up.clear()
        # Topik-ið (eitt eða fleiri) sem á að gerast áskrifandi að
        await client.subscribe(TOPIC_MOTTAKA, 1) 
        # await client.subscribe(TOPIC_2, 1) 

async def main(client):
    # tengjast við þráðlausa netið
    await client.connect()
    # búa til task
    asyncio.create_task(askrift(client))
    asyncio.create_task(mottakari(client))
    asyncio.create_task(sendir(client))

    while True:
        # Ekkert að gera hér
        await asyncio.sleep_ms(0)

# Sýnir ýmsar upplýsingar eins og t.d. varðandi nettenginguna og minnisnotkun  
MQTTClient.DEBUG = True

# Búa til tilvik af MQTTClient og senda inn stillingarnar
client = MQTTClient(config)

try:
    # Ræsa async main fallið og senda þangað tilvik af client-num
    asyncio.run(main(client))
finally:
    client.close()
```
