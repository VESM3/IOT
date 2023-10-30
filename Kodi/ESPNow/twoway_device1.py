from machine import Pin
from neopixel import NeoPixel
from network import WLAN, STA_IF
from espnow import ESPNow
from time import sleep

# NeoPixel initialization
neo = NeoPixel(Pin(48), 1)
def light_up(color):
    neo[0] = color
    neo.write()

# Initialize the wireless interface
sta = WLAN(STA_IF)
sta.active(True)

# Initialize ESP-NOW
espnow = ESPNow()
espnow.active(True)

# MAC address of Device 2
peer = b'4\x85\x18\xa6|\x9c'  # breyttu hér  MAC address
espnow.add_peer(peer)

while True:
    # Send a message to Device 2
    espnow.send(peer, 'Hello Device 2')
    light_up((255, 0, 0))  # Red color after sending

    sleep(5)
    # Wait for a reply
    _, message = espnow.recv()
    if message:
        print(message.decode())
        light_up((0, 255, 0))  # Green color after receiving reply

    sleep(5)

