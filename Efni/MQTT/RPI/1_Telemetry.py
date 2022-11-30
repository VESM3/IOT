# Telemetry: Hlutur sendir gildi með JSON sniðmáti til MQTT broker (Publish telemetry).
# Vefgrein: https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/single-board-computer-telemetry.md
# Kóði: https://github.com/microsoft/IoT-For-Beginners/blob/main/1-getting-started/lessons/4-connect-internet/code-telemetry/pi/nightlight/app.py

import paho.mqtt.client as mqtt

# til að stýra tíðni sendinga
import time
# gögn eru send með JSON sniðmáti (payload)
import json

# Use the same ID on telemetry, server and actuator
id = '<ID>'
# unique name for this MQTT client on the broker.
client_name = id + 'telemetry'

# MQTT topic the device will publish
client_telemetry_topic = id + '/telemetry'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org') 
mqtt_client.loop_start()

def main():

  while True:
    # notum til einföldunar hér harðkóðað gildi.
    light = 100
    # breytum gögnum í json streng  
    telemetry = json.dumps({'light' : light})
    # merkjum topic og sendum Json streng (gögn) 
    mqtt_client.publish(client_telemetry_topic, telemetry)
    # sendum á 5 sek. fresti
    time.sleep(5)

if __name__=="__main__":
   main()