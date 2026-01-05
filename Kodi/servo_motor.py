from machine import Pin
from servo import Servo
from time import sleep_ms

kjalki = Servo(Pin(15))
bidtimi = 10
min = 15
max = 165

while True:
    for i in range(min, max):
        kjalki.write_angle(i)
        sleep_ms(bidtimi)
    for i in range(max, min, -1):
        kjalki.write_angle(i)
        sleep_ms(bidtimi)