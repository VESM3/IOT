## Tímaverkefni 4 (15%)

- PiCam
- Vefþjónustur [Services for Things](https://learn.adafruit.com/all-the-internet-of-things-episode-three-services/services-for-things)

---

### 1. PiCam V2. (10%)

[Raspberry Pi camera](https://www.raspberrypi.com/documentation/accessories/camera.html#camera-modules) Module v2 getur tekið 8 Megapixel og myndband með 1640x1232p upplausn. Við munum nota [picamera](https://picamera.readthedocs.io/en/release-1.13/) safnið. <br>
_RPi Zero virkar **ekki** með nýja `libcamera`, sjá nánar [Camera software](https://www.raspberrypi.com/documentation/computers/camera_software.html#introducing-the-raspberry-pi-cameras)_

#### Að tengja Picam við RPi:
1. Slökktu fyrst á RPi þegar þú tengir myndavélina við Camera Serial Interface (CSI) á RPi. 
1. Tengdu PiCamera við RPi. [How to connect a Picamera to a Pi ZERO (myndband)](https://www.youtube.com/watch?v=zFAX4pH1BPA)_.

#### Fylgdu [Getting started with the Camera Module](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2)
1. Taktu mynd af þér með að nota terminal.
1. Skrifaðu python kóða til að takta mynd með 1024x768 upplausn af sjálfum þér með Pi V2 myndavélinni tengda við RPi og vistaðu á skjáborðinu. `camera.capture('/home/pi/Desktop/image.jpg')`. 
1. Taktu upp stutt myndband með PiCam. Sjá [Video to file](https://picamera.readthedocs.io/en/release-1.10/recipes1.html#recording-video-to-a-file).

<br>

> _Ítarefni:  Að streyma "live" myndbönd: [sýnidæmi með VLC](https://www.tomshardware.com/how-to/stream-live-video-raspberry-pi) og [sýnidæmi með Flask](https://github.com/miguelgrinberg/flask-video-streaming)_

---

### 2. Að taka ljósmynd með takka. (10%)
1. Notaðu takka (þegar honum er sleppt) til að taka myndina.
3. Bættu við 3 sek. timer með takka til þess að taka myndina, [Button controlled camera](https://gpiozero.readthedocs.io/en/stable/recipes.html#button-controlled-camera)

---

### 3. PIR hreyfiskynjarinn. (20%)
1. Kynntu þér PIR og notaðu hreyfiskynjara til kveikja á LED. 
   - [PIR (lastminute)](https://lastminuteengineers.com/pir-sensor-arduino-tutorial/)
      - PIR er tengt í 5V (er með innbyggðan 3.3V regulator) 
      - taktu linsu af PIR til að þrengja IR svið. 
      - Skoðaðu vel GND og Vc staðsetningar (mismunandi eftir tegundum)
      - stilltu næmleika og timeout á PIR eftir þörfum.
   - [Motion sensor kóðalausn](https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor)
1. Taktu mynd þegar PIR hreyfiskynjari fer í gang. 

<br>

> _Ítarefni: Sendu ljósmyndina á gmail netfang. [How to Use the Raspberry Pi4 Camera and PIR Sensor to Send Emails](https://maker.pro/raspberry-pi/projects/how-to-use-the-raspberry-pi4-camera-and-pir-sensor-to-send-emails). Búðu til Gmail reikning og leyfðu “Allow less secure apps” svo hægt er að taka við tölvpóst með python kóða._
    
---

### 4. IFTTT (If This Then That) (10%)
1. Búðu til aðgang og prófað einhverjar áhugverða IFTTT vefþjónustu sem er í boði. [How does IFTTT work?](https://help.ifttt.com/hc/en-us/articles/115010158167-How-does-IFTTT-work-) og [listi af þjónustum](https://ifttt.com/services) flokkað.
2. Búðu til eigið applet (free útgáfan) og sameinaðu tvær þjónustur að eigin vali. [Creating your own Applet](https://help.ifttt.com/hc/en-us/articles/360021401373-Creating-your-own-Applet)

---

### 5. IFTTT WebHooks (20%) 
Með Webhooks er hægt að senda og taka við `triggers` með HTML POST og GET requests, sjá nánar [What is a Webhook? - IFTTT](https://ifttt.com/explore/what-is-a-webhook)

1. Notaðu takka með RPi. Notaðu Webhooks með IFTTT til að fá tilkynningu (push notification) þegar það hefur verið smellt á takkann, sjá td. [How to control RPi GPIO pins with IFTTT](https://www.circuitbasics.com/how-to-control-the-raspberry-pi-gpio-using-ifttt/).<br>

**Aðrar bjargir:**
- [Push notification, motion detection](https://iot4beginners.com/ifttt-with-raspberry-pi/)
- [Hackster.io og IFTTT](https://www.hackster.io/ifttt)

---

### 6. Myndgreining með vefþjónustu (30%) _drög_

[Myndgreiningavefþjónustur](https://nordicapis.com/7-best-image-recognition-apis/) eru sniðugar til að greina hluti, andlit, liti og texta á ljósmyndum. 
Skoðaðu og notaðu [Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/#overview) frá Microsoft Azure til að greina hluti á ljósmynd. Notaðu fyrst fartölvuna og svo RPi með PiCam.

1. Myndgreining með Computer Vision (fartölva)
   1. Búðu til aðgang hjá Azure via _`Github Student Developer Pack`_ (gætir þurft að skrá þig út á Azure) 
   1. Gerðu viðeigandi stillingar hjá Azure til að geta notað Computer Vision. 
   1. Notaðu VSCode og python á fartölvunni, ([kóðadæmi](https://github.com/VESM3/IOT/blob/main/Efni/ComputerVisionDemo.py)) til að greina ljósmynd (minna en 4MB).
1. Notaðu RPi, PiCam og Computer Vision saman og birtu niðurstöður. 

**Bjargir**
- [Computer Vision with Microsoft Azure](https://www.pluralsight.com/guides/computer-vision-with-microsoft-azure)
- [Computer Vision documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/)
- [Computer Vision SDK for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python-preview)
- [myndbönd](https://www.youtube.com/hashtag/azureinpython)


#### Aðrar áhugaverðar [vefþjónustur]( https://azure.microsoft.com/en-us/products/cognitive-services/#api) 
- Language: Q&A bot, translator, túlka texta.
- Speech: Siri, translation osfrv.

---

## Námsmat
- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnir og myndbönd af verklegum tilraunum.


   
