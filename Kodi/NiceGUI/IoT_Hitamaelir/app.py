# IoT Hitamælir - MQTT Dashboard
# ræst með pyton app.py (getur tekið smá stund að fara í gang)
# í browser farið á IP_A_RPi:8080

import asyncio
from aiomqtt import Client
from random import randint
import time
import json
from nicegui import ui, app


# Gögn móttekin með MQTT í lista
gognin = []

MQTT_BROKER = "IP_TALAN_A_RPI"
MQTT_TOPIC = "TOPIC-IÐ"

async def mottaka():
    async with Client(MQTT_BROKER) as client:
        while True:
            await client.subscribe("abc")
            async for message in client.messages:
                #print(f"móttekið: {message.payload}")
                # mótteknum gögn breytt úr json í dict og sett í listann
                gognin.append(json.loads(message.payload))
                # geymum bara síðustu 20 
                if len(gognin) > 20:
                    gognin.pop(0)

@ui.page('/')
def root():
    ui.label('🌡️ IoT Hitamælir').classes('text-3xl font-bold mb-4')
    ui.label(f'MQTT Rás: {MQTT_TOPIC}').classes('text-sm text-gray-600 mb-2')
    
    chart = ui.echart({
        'title': {'text': 'Tala A - Tala B', 'left': 'center'},
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
                },{
                'type': 'line',
                'data': [],
                'smooth': True,
                'lineStyle': {'width': 2},
                'itemStyle': {'color': "#ce262c"}
                }],
        'tooltip': {
            'trigger': 'axis',
            'formatter': '{b}<br/>Hiti: {c} °C'
        },
        'grid': {'left': '10%', 'right': '10%', 'bottom': '15%'}
    }).classes('w-full h-96')
    
    def uppfaera_gogn_a_vefsidu():
        if gognin is not None:
            lina_a = []
            lina_b = []
            for i, g in enumerate(gognin):
                lina_a.append([i, g['tala_a']])
                lina_b.append([i, g['tala_b']])
            chart.options['series'][0]['data'] = lina_a
            chart.options['series'][1]['data'] = lina_b
            chart.update()
    
    # Vefsíða uppfærð á 1 sek. fresti
    ui.timer(1.0, uppfaera_gogn_a_vefsidu)
    
    ui.label('Bíð eftir MQTT gögnum...').classes('text-sm text-gray-500 mt-2')

# NiceGUI ræsir móttökufallið async
app.on_startup(mottaka)

# ræsa vefsíðu
ui.run()
