# Sendir (publisher)


# nota mosquitto_sub -h test.mosquitto.org -t XXXXkynning til að sjá hvort eitthvað sendist

# --------------------- WIFI ---------------------

from network import WLAN, STA_IF
from time import sleep_ms

WIFI_SSID = ""
WIFI_LYKILORD = ""

wifi = WLAN(STA_IF)
if not wifi.isconnected():
    print(f"Tengist við {WIFI_SSID} ...")
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_LYKILORD)
    while not wifi.isconnected():
        pass
print(f"Tenging við {WIFI_SSID}, netupplýsingar:", wifi.ifconfig())
    
# ------------------------- MQTT ------------------------

from machine import unique_id
from ubinascii import hexlify
from umqtt.simple import MQTTClient

MQTT_BROKER = "test.mosquitto.org"
#CLIENT_ID = hexlify(unique_id())
#CLIENT_ID = str(unique_id())
CLIENT_ID = "Sendandi"

TOPIC = b"XXXXkynning" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna

mqtt_client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
mqtt_client.connect()

teljari = 0

while True:
    mqtt_client.publish(TOPIC, f"Hæ, ég heiti {CLIENT_ID}, talan mín er {teljari}".encode())
    teljari += 1
    sleep_ms(3000)




