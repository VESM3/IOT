# Subscribe to commands
# Vefgrein: https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/single-board-computer-commands.md
# Kóði: https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/code-commands/pi/nightlight/app.py

import paho.mqtt.client as mqtt
import json

# Til að geta unnið með datapinna á RPi og LED
from gpiozero import LED
led = LED(17)

# Use the same ID on telemetry, server and actuator
id = '<ID>'
# unique name for this MQTT client on the broker.
client_name = id + 'actuator'

# MQTT topic the device will subscribe
server_command_topic = id + '/commands'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org') 
mqtt_client.loop_start()

def handle_command(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    if payload['led_on']:
        led.on()
    else:
        led.off()

# hlustar eftir skipun
mqtt_client.subscribe(server_command_topic)
# The on_message handler is called for all topics subscribed to.
mqtt_client.on_message = handle_command

