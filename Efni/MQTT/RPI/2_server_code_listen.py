# Receive telemetry from the MQTT broker
# Vefgrein: https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/README.md#receive-telemetry-from-the-mqtt-broker
# Kóði: https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/code-server/server/app.py

import paho.mqtt.client as mqtt  
import time
import json

# Use the same ID on telemetry, server and actuator
id = '<ID>'

# unique name for this MQTT client on the broker.
client_name = id + 'test_server'
client_telemetry_topic = id + '/telemetry'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org') 
mqtt_client.loop_start()

# When a telemetry message is received, the handle_telemetry function is called, 
# printing the message received to the console.
def handle_telemetry(client, userdata, message):
    # breytum Json streng (gögn) í dictionary
    payload = json.loads(message.payload.decode())
    # prentum í console gögnin.
    print("Message received:", payload)

# Hlustum eftir ákveðnu topic.
mqtt_client.subscribe(client_telemetry_topic)
# The MQTT client is listening to messages on a background thread and runs all the time the main application is running.
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)

