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

# MAC address of Device 1
peer = b'4\x85\x18l=\xb0'  # breyttu addressu
espnow.add_peer(peer)

while True:
    # Wait for a message from Device 1
    _, message = espnow.recv()
    if message:
        print(message.decode())
        light_up((0, 0, 255))  # Blue color after receiving a message

        sleep(5)
        # Reply to Device 1
        espnow.send(peer, 'Hello Device 1')
        light_up((255, 255, 0))  # Yellow color after sending a reply

    sleep(5)

