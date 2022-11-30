# Send commands to the MQTT broker
# Vefgrein: https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/README.md#send-commands-to-the-mqtt-broker
# Kóði: https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/code-commands/server/app.py

import paho.mqtt.client as mqtt  
import time
import json

# Use the same ID on telemetry, server and actuator
id = '<ID>'
# unique name for this MQTT client on the broker.
client_name = id + 'server'
client_telemetry_topic = id + '/telemetry'

# define which topic to send commands to
server_command_topic = id + '/commands'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org') 
mqtt_client.loop_start()

def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)
    # do something with payload from telemetry
    # value of led_on is set to true or false depending on if the light is less than 300 or not. 
    command = { 'led_on' : payload['light'] < 300 }
    # debugg, console
    print("Sending message:", command)
    # breytum í Json streng og sendum skipun til Broker, með topic heitið server_command_topic 
    client.publish(server_command_topic, json.dumps(command))

mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)

