## Tímaverkefni 2 (9%)

- PiCam
- PIR 

---

#### 1. Pi V2 Camera. (20%)
1. Taktu mynd af þér með að nota terminal
   - **Varúð!** Slökktu fyrst á RPi þegar þú tengir myndavélina við Camera Serial Interface (CSI) á RPi. 
   - Tengdu PiCamera við RPi skv. [How to connect a Picamera to a Pi ZERO (myndband)](https://www.youtube.com/watch?v=zFAX4pH1BPA) 
   - Fylgdu [Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2)
   - [Picamera Documentation](https://www.raspberrypi.com/documentation/accessories/camera.html#hardware-specification)
1. Skrifaðu python kóða til að takta mynd með 1024x768 upplausn af sjálfum þér með Pi V2 myndavélinni tengda við RPi og vistaðu á skjáborðinu. `camera.capture('/home/pi/Desktop/image.jpg')` 
   - [picamera library](https://picamera.readthedocs.io/en/release-1.13/)
1. Ath. RPi Zero virkar ekki vel með [libcamera](https://www.raspberrypi.com/documentation/accessories/camera.html).

---

#### 2 Að taka ljósmynd með takka. (20%)
1. Notaðu takka (þegar honum er sleppt) til að taka myndina.
1. Bættu við 3 sek. timer með takka til þess að taka myndina
   - [Button controlled camera](https://gpiozero.readthedocs.io/en/stable/recipes.html#button-controlled-camera)

---

#### 3. PIR hreyfiskynjarinn. (20%)
Kynntu þér PIR og notaðu hreyfisyknjara til að kveikja á LED. 

- [PIR (lastminute)](https://lastminuteengineers.com/pir-sensor-arduino-tutorial/)
   - PIR er tengt í 5V (er með innbyggðan 3.3V regulator) 
   - Víxlaðu GND og Vc staðsetningum (mismunandi eftir tegundum).
   - stilltu næmleika og timeout á PIR með að snúa báðum allaleið rangsælis.
   - taktu linsu af PIR til að þrengja IR svið. 
- [PIR (adafruit)](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/overview)
- [Motion sensor kóðalausn](https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor)

---

#### 4. PIR og Pi V2 Camera. (20%)

1. Taktu mynd þegar PIR hreyfiskynjari fer í gang  
1. Sendu ljósmyndina á gmail netfang.
    - [How to Use the Raspberry Pi4 Camera and PIR Sensor to Send Emails](https://maker.pro/raspberry-pi/projects/how-to-use-the-raspberry-pi4-camera-and-pir-sensor-to-send-emails)
    - Búðu til Gmail reikning og leyfðu “Allow less secure apps” svo hægt er að taka við tölvpóst með python kóða.
    - Slepptu að nota buzzer
    
---

#### 5. Myndbandsupptaka (20%)

Með PiCam og RPi er hægt að taka upp og streyma myndbönd. Taktu upp stutt myndband með PiCam. Sjá t.d. [Video to file](https://picamera.readthedocs.io/en/release-1.10/recipes1.html#recording-video-to-a-file).

<!--
1. Settu upp myndbandsstreymi, hýstu á vefsíðu með ESP32 eða notaðu VLC. [sýnidæmi 1](https://github.com/miguelgrinberg/flask-video-streaming), [sýnidæmi 2](https://www.tomshardware.com/how-to/stream-live-video-raspberry-pi)
-->
---

### Námsmat og skil.

- Yfirferð á sér stað í tíma. 
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnum.

---

<!--
#### Remote Camera með Bluedot. 
RasberryPI tekur mynd þegar smellt er á Blue Dot í snjallsíma. Fylgdu tutorial: [Bluetooth and BlueDot using remote camera !](https://bluedot.readthedocs.io/en/latest/recipes.html#remote-camera)
-->

