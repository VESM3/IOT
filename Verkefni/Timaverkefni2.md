## Tímaverkefni 2 (9%)

- Einstaklingsverkefni
- GPIO, PiCam, PIR

---

#### 1. Blikkandi ljós. (10%)
Láttu LED blikka á brauðbretti með python kóða. Notaðu T-Coppler með brauðbrettinu og [GPI Zero](https://gpiozero.readthedocs.io/en/stable/) python safnið með kóðalausn. 

---

#### 2. Blikkandi LED með fade. (10%)
Láttu LED peru fade in og út.

---

#### 3. Takki og LED. (10%)
Við að ýta á takka þá kemur birta af LED. 

---

#### 4. Pi V2 Camera. (10%)
1. Taktu mynd af þér með að nota terminal
   - **Varúð!** Slökktu fyrst á RPi þegar þú tengir myndavélina við Camera Serial Interface (CSI) á RPi. 
   - [How to connect a Picamera to a Pi ZERO (myndband)](https://www.youtube.com/watch?v=zFAX4pH1BPA) 
   - [Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2)
   - [Picamera Documentation](https://www.raspberrypi.com/documentation/accessories/camera.html#hardware-specification)

---

#### 5. Að taka ljósmynd með python. (20%)
1. Skrifaðu python kóða til að takta mynd með 1024x768 upplausn (eða hærri) af sjálfum þér með Pi V2 myndavélinni tengda við RPi og vistaðu á skjáborðinu. `camera.capture('/home/pi/Desktop/image.jpg')` 
   - [picamera library](https://picamera.readthedocs.io/en/release-1.13/)

---

#### 6 Að taka ljósmynd með takka. (20%)
1. Notaðu takka (þegar honum er sleppt) til að taka myndina.
1. Bættu við 3 sek. timer með takka til þess að taka myndina
   - [Button controlled camera](https://gpiozero.readthedocs.io/en/stable/recipes.html#button-controlled-camera)

---

#### 7. PIR hreyfiskynjarinn. (20%)
Kynntu þér PIR og notaðu hreyfisyknjara til að kveikja á LED. 

- [PIR (lastminute)](https://lastminuteengineers.com/pir-sensor-arduino-tutorial/)
   - PIR er tengt í 5V (er með innbyggðan 3.3V regulator) 
   - Víxlaðu GND og Vc staðsetningum (mismunandi eftir tegundum).
   - stilltu næmleika og timeout á PIR með að snúa báðum allaleið rangsælis.
   - taktu linsu af PIR til að þrengja IR svið. 
- [PIR (adafruit)](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/overview)
- [Motion sensor kóðalausn](https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor)

---

#### 8. PIR og Pi V2 Camera. 
1. Taktu mynd þegar PIR hreyfiskynjari fer í gang 
1. Sendu ljósmyndina á gmail netfang.
    - [How to Use the Raspberry Pi4 Camera and PIR Sensor to Send Emails](https://maker.pro/raspberry-pi/projects/how-to-use-the-raspberry-pi4-camera-and-pir-sensor-to-send-emails)
    - Búðu til Gmail reikning og leyfðu “Allow less secure apps” svo hægt er að taka við tölvpóst með python kóða.
    - Slepptu að nota buzzer
---

### Námsmat

- Yfirferð á sér stað í tíma. 
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
