"""
IoT Hitamælir - MQTT Dashboard
================================

LEIÐBEININGAR - Hvernig á að keyra:
----------------------------------

1. Opnaðu tvö terminal glugga

2. Í fyrsta terminal glugganum:
   $ source venv/bin/activate
   $ python app.py

3. Í öðrum terminal glugganum:
   $ source venv/bin/activate
   $ python mqtt_publisher.py

4. Notaðu LiveServer í VSCode, Opnaðu vafra og farðu á:
   http://localhost:8080

5. Þú munt sjá hitamælingar birtast á línuritinu í rauntíma!

ATHUGASEMD:
-----------
- Gögn eru send í gegnum MQTT miðlara (broker.hivemq.com)
- Hitamælingar eru sendar á 2 sekúndna fresti
- Grafið uppfærist á 1 sekúndna fresti
- Geymir síðustu 20 mælingar í minni

"""

import time
import json
import paho.mqtt.client as mqtt
from nicegui import ui, app

# MQTT Configuration
MQTT_BROKER = "broker.hivemq.com"  # Public MQTT broker
MQTT_PORT = 1883
MQTT_TOPIC = "iot/temperature/sensor001"

# Store temperature data
temperature_data = []

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Tengdur við MQTT miðlara með niðurstöðukóða {rc}")
    client.subscribe(MQTT_TOPIC)
    print(f"Áskrifandi að efni: {MQTT_TOPIC}")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        temperature = payload.get('temperature')
        if temperature is not None:
            print(f"Móttók hita: {temperature}°C")
            temperature_data.append({
                'time': time.time() * 1000,
                'value': temperature
            })
            # Keep only last 20 readings
            if len(temperature_data) > 20:
                temperature_data.pop(0)
    except Exception as e:
        print(f"Villa við vinnslu skilaboða: {e}")

# Initialize MQTT client
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to broker
try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()
except Exception as e:
    print(f"Mistókst að tengjast MQTT miðlara: {e}")

@ui.page('/')
def root():
    ui.label('🌡️ IoT Hitamælir').classes('text-3xl font-bold mb-4')
    ui.label(f'MQTT Rás: {MQTT_TOPIC}').classes('text-sm text-gray-600 mb-2')
    
    chart = ui.echart({
        'title': {'text': 'Hiti (°C)', 'left': 'center'},
        'xAxis': {
            'type': 'time',
            'axisLabel': {'hideOverlap': True}
        },
        'yAxis': {
            'type': 'value',
            'name': '°C',
            'min': 'dataMin',
            'max': 'dataMax'
        },
        'series': [{
            'type': 'line',
            'data': [],
            'smooth': True,
            'lineStyle': {'width': 2},
            'itemStyle': {'color': '#5470c6'}
        }],
        'tooltip': {
            'trigger': 'axis',
            'formatter': '{b}<br/>Hiti: {c} °C'
        },
        'grid': {'left': '10%', 'right': '10%', 'bottom': '15%'}
    }).classes('w-full h-96')
    
    def update_chart():
        if temperature_data:
            chart_data = [[d['time'], d['value']] for d in temperature_data]
            chart.options['series'][0]['data'] = chart_data
            chart.update()
    
    # Update chart every second
    ui.timer(1.0, update_chart)
    
    ui.label('Bíð eftir MQTT gögnum...').classes('text-sm text-gray-500 mt-2')

ui.run()
