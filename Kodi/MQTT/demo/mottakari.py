# Móttakari (Subscriber)

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
CLIENT_ID = "Mottakari"

TOPIC = b"XXXXkynning" # Settu fyrstu fjóra stafinu úr kennitölunni þinni stað í X-anna

def fekk_skilabod(topic, skilabod):
    print(f"TOPIC: {topic.decode()}, skilaboð: {skilabod.decode()}")

mqtt_client = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
mqtt_client.set_callback(fekk_skilabod)
mqtt_client.connect()
mqtt_client.subscribe(TOPIC)

while True:
    mqtt_client.check_msg()
    sleep_ms(1000)





