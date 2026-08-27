# Tímaverkefni 3 
- Námsmat 15% af heildareinkunn
- Einstaklingsverkefni
- Viðfangsefni: NTP, MQTT

---

### 1. Að fá rauntíma frá NTP (Network Time Protocol) vefþjóni með ESP32  (**30%**)

1. Kynntu þér NTP og hvernig það er notað í MicroPython með því að skoða þessa [grein](https://bhave.sh/micropython-ntp/).
1. Skoðaðu einnig hvernig unnið er með tíma (leggja saman, draga frá o.fl) í microPython með því að skoða [þetta](https://docs.micropython.org/en/latest/library/time.html). MicroPython inniheldur ekki `datatime` klasasafnið.
     ```python
      # aðferð til að varpa tíma (tuple) yfir í breytur.
      _, _, _, klst, minutur, sekundur, _, _ = time.localtime()
     print(f"{klst:02}:{minutur:02}:{sekundur:02}")
     ```
1. Í áfanganum notum við okkar eigið þráðlaust net í kennslustofunni. Tengdu ESP-inn við þráðlausa internetið:
     ```python
     SSID = "TskoliVESM"
     LYKILORD = "Fallegurhestur"

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
     ```
<!-- Bættu við smá `sleep` til að gefa ESP32 smá tíma til að tengjast wifi. -->

#### Verkefnið
1. Náðu í réttan tíma með NTP (Keyrðu `main.py` í ESP32 og ýttu á reset). 
1. Láttu augun blikka á ákveðnum tíma og dagsetningu með NTP (notaðu tímasetningu nálægt þér í rauntíma).


<br>

> [!Note]
> - Ef þú færð `OSError: [Errno 116] ETIMEDOUT` eða `OSError: [Errno 118] EHOSTUNREACH` hinkraðu þá í smá stund og prófaðu aftur.
> - Notaðu hotspot í síma ef skólanet virkar ekki.
> - **Ekki** nota pinna; GPIO0, GPIO3, GPIO19, GPIO20, GPIO45, GPIO46. 

---

### 2. MQTT, einstefnusamskipti (**30%**)

Kynntu þér allt um [MQTT](https://mqtt.org) og [mqtt_as](https://github.com/peterhinch/micropython-mqtt) safnið.

Settu mqtt_as safnið inn á ESP_ana þína með því að keyra eftirfarandi kóða á þeim:

```python
# Notaðu do_connect fallið hér fyrir ofan.
    
do_connect()

import mip
mip.install("github:peterhinch/micropython-mqtt")
```


Sýnidæmi (sendir Hallo ásamt teljara):

<details>
<summary>Sendir</summary>

```python
from mqtt_as import MQTTClient, config
import asyncio

# WIFI stillingar
config["ssid"] = "TskoliVESM"
config["wifi_pw"] = "Fallegurhestur"

# MQTT þjónninn
config["server"] = "test.mosquitto.org" # eða broker.emqx.io (þarf að vera það sama á sendir og móttakara)

# TOPICS
TOPIC = "XXXXkynning" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna

async def sendir(client):
    teljari = 0
    while True:
        # Skilaboðin sem á að senda verða bytes, til þess þarf encode, sérstaklega ef senda á íslenska stafi
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
        # Hér kæmi kóði sem á ekki að keyra async
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
</details>

<details>
<summary>Móttakari</summary>

```python
from mqtt_as import MQTTClient, config
import asyncio

# WIFI stillingar
config["ssid"] = "TskoliVESM"
config["wifi_pw"] = "Fallegurhestur"

# MQTT þjónninn
config["server"] = "test.mosquitto.org" # eða broker.emqx.io (þarf að vera það sama á sendir og móttakara)
config["queue_len"] = 1

# TOPICS
TOPIC = "XXXXkynning" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna
#TOPIC_2 = "YYYYkynning"

# Fallið meðhöndlar skilaboð sem berast
async def mottakari(client):
    # skilaboðin berast í biðröð (e. queue) sem við sækjum þau svo úr
    async for topic, skilabod, _ in client.queue:
        hallo, tala = skilabod.decode().split()
        # ef nota á töluna þarf að setja hana í int fallið
        tala = int(tala)
        print(f"TOPIC: {topic.decode()}, texti: {hallo}, tala: {tala}")

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
        # Hér kæmi kóði sem á ekki að keyra async, t.d. lesa frá stilliviðnámi
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
</details>

> [!Note]
> - Mundu að allt er sent sem strengur þannig að í mótttökunni þarftu að breyta yfir í `int`.
> - [ADC2](https://github.com/VESM3/IOT/wiki/ESP32) pinnar fyrir analog virka ekki þegar við erum að nota wifi.

#### Að hafa tvo Thonny glugga opna samtímis
Í Thonny skaltu fara í Tools->Options->General og taka hakið úr *Allow only single Thonny instance*, **lokaðu svo Thonny**. Þá getur þú opnað tvo Thonny glugga. Á Mac þarf að opna glugga nr. 2 með því að fara í terminal og skrifa eftirfarandi: `open -n -a Thonny.app`


#### Verkefnið
1. Tengdu [stilliviðnám](https://cdn-learn.adafruit.com/guides/images/000/002/179/medium800/562-00.jpg) við stakan ESP32 (sendir) til að stjórna lit í augunum á fígúru (móttakari). Þú skiptir um lit með að snúa breytiviðnáminu. Ath. stilliviðnám vinnur með [hliðræn](https://github.com/VESM1VS/AFANGI/blob/main/Kennsluefni/analog.md#lesi%C3%B0-fr%C3%A1-pinna) gildi.

---

### 3. MQTT, tvístefnusamskipti (**40%**)

Skoðaðu vel og keyrðu eftirfarandi sýnikóða þar sem:
1. ESP-A publish-ar _Hallo X_ (þar sem X er stighækkandi tala) á topic-ið XXXX_A_til_B sem ESP-B er áskrifandi að.
1. ESP-B publish-ar _Bless X_ á topic-ið XXXX_B_til_A sem ESP-A er áskrifandi að.

<details>
<summary>ESP-A</summary>

```python
from mqtt_as import MQTTClient, config
import asyncio

# WIFI stillingar
config["ssid"] = "TskoliVESM"
config["wifi_pw"] = "Fallegurhestur"

# MQTT þjónninn
config["server"] = "test.mosquitto.org" # eða broker.emqx.io (þarf að vera það sama á sendir og móttakara)
config["queue_len"] = 1

# TOPICS
TOPIC_SENDING = "XXXX_A_til_B" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna
TOPIC_MOTTAKA = "XXXX_B_til_A"

# Fallið meðhöndlar skilaboð sem berast
async def mottakari(client):
    # skilaboðin berast í biðröð (e. queue) sem við sækjum þau úr
    async for topic, skilabod, _ in client.queue:
        print("móttek frá B: ", topic.decode(), skilabod.decode())

async def sendir(client):
    teljari = 0
    while True:
        # Skilaboðin sem á að senda, þarf encode ef senda á íslenska stafi
        skilabod = f"Halló {teljari}".encode() 
        print(f"sendi til B: {skilabod}" )
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
</details>

<details>
<summary>ESP-B</summary>
<br>

```python
from mqtt_as import MQTTClient, config
import asyncio

# WIFI stillingar
config["ssid"] = "TskoliVESM"
config["wifi_pw"] = "Fallegurhestur"

# MQTT þjónninn
config["server"] = "test.mosquitto.org" # eða broker.emqx.io (þarf að vera það sama á sendir og móttakara)
config["queue_len"] = 1

# TOPICS
TOPIC_SENDING = "XXXX_B_til_A" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna
TOPIC_MOTTAKA = "XXXX_A_til_B"

# Fallið meðhöndlar skilaboð sem berast
async def mottakari(client):
    # skilaboðin berast í biðröð (e. queue) sem við sækjum þau úr
    async for topic, skilabod, _ in client.queue:
        print("móttek frá A: ", topic.decode(), skilabod.decode())

async def sendir(client):
    teljari = 0
    while True:
        # Skilaboðin sem á að senda, þarf encode ef senda á íslenska stafi
        skilabod = f"Bless {teljari}".encode() 
        print(f"sendi til A: {skilabod}" )
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

</details>

#### Verkefnið

Gerðu eftirfarandi:

1. Byrjun: Kveiktu á báðum NeoPixel í augum á fígúrunni með að nota NTP.
1. Láttu augu breyta um lit á 1 sek. fresti.
1. Sendu litastöðu til baka með [JSON](https://www.w3schools.com/python/python_json.asp) sniðmát frá fígúru til ESP32 (stakur) á 1 sek. fresti.
1. Láttu LED<sub>1</sub> á ESP32 (stakur) vera með sömu litastöðu og sama takt og augun á fígúru. Birtu líka JSON í shell/REPL svæðið í Thonny.
1. Endir: Slökktu á öllum NeoPixel á báðum EPS32 þegar 10 sekúndur hafa liðið frá upphafi. 

<sub>1</sub> LED er innbyggða NeoPixel peran á ESP32 (pinni 48).

<br>

 ![flæðirit](https://github.com/VESM3/IOT/blob/main/Myndir/H26_V3_3.svg)

---

## Námsmat og skil

- Skilaðu öllum kóða í Canvas. Passaðu að þú getir útskýrt kóðann sem þú skilar fyrir kennara.
- Yfirferð á sér stað í tíma. Einkunn fyrir hvern lið: 
    - 10 lausn er vel útfærð.
    - 7.5 lausn er smávægilega ábótavant (vantar smá upp á).
    - 5 lausn er ábótavant, helmingur er vel útfærður.
    - 2.5 lausn er stórlega ábótavant, en tíma- og kóðavinna lögð í lausn.
    - 0 lausn vantar eða óunnin.
