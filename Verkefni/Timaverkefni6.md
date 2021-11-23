## Tímaverkefni 6 (9%)

- Einstaklingsverkefni
- Vefþjónustur

<!-- [Services for Things (myndbandskynning)](https://learn.adafruit.com/all-the-internet-of-things-episode-three-services/services-for-things) -->

---

### 6.1 IFTTT (If This Then That) (10%)
1. Búðu til aðgang og prófað einhverjar áhugverða IFTTT vefþjónustu sem er í boði. [How does IFTTT work?](https://help.ifttt.com/hc/en-us/articles/115010158167-How-does-IFTTT-work-) og [listi af þjónustum](https://ifttt.com/services) flokkað.
2. Búðu til eigið applet (free útgáfan) og sameinaðu tvær þjónustur að eigin vali. [Creating your own Applet](https://help.ifttt.com/hc/en-us/articles/360021401373-Creating-your-own-Applet)

---

### 6.2 IFTTT með Adafruit IO - Any new data (20%)
Notaðu takka á brauðbretti sem er tengt við RaspberryPi sem sendir skilaboð til Adafruit IO þegar ýtt er á hann. <br>
Notaðu IFTTT sem vaktar þetta `feed` hjá Adafruit IO og lætu þig vita (td. sms) þegar smellt er á takkann. <br>
Sjá [IFTTT AdafruitIO leiðbeiningar](https://learn.adafruit.com/using-ifttt-with-adafruit-io/ifttt-to-adafruit-io-setup), notaðu _Any new data_ trigger <br>

#### Athugaðu
- All Gmail triggers were removed from IFTTT
- [Zapier](https://zapier.com/) með AdafruitIO er annar valkostur í stað IFTTT

---

### 6.3 IFTTT með Adafruit IO - Monitor a feed (20%)
1. Tengdu [jarðvegsmælir](https://www.sigmaelectronica.net/wp-content/uploads/2018/04/sen0193-humedad-de-suelos.pdf) við ESP32 til að kanna rakastig "jarðvegs".
1. Notaðu IFTTT sem vaktar þetta `feed` hjá Adafruit IO og lætu þig vita (td. sms) þegar "jarðvegur" verður of þurr (notaðu gildi sem hentar tilraun).

<!--
- [Adafruit IO Time Tracking Cube með ESP32 og Zapier](https://github.com/adafruit/Adafruit_IO_Arduino/blob/master/examples/adafruitio_24_zapier/adafruitio_24_zapier.ino) og 
https://learn.adafruit.com/time-tracking-cube
-->

---

### 6.4 IFTTT WebHooks (20%) 
1. Mældu hita og raka með [DHT11](https://components101.com/sensors/dht11-temperature-sensor) tengt við RPi.<br>
1. Með Webhooks er hægt að senda og taka við `triggers` með HTML POST og GET requests, sjá nánar [What is a Webhook? - IFTTT](https://ifttt.com/explore/what-is-a-webhook). <br>
Notaðu Webhooks með IFTTT til að fá tilkynningu (push notification) þegar rakastigi er komið upp fyrir eitthvert ákv. gildi.<br>

**Bjargir:**
- [Push notification, motion detection](https://iot4beginners.com/ifttt-with-raspberry-pi/)
- [How to control RPi GPIO pins with IFTTT](https://www.circuitbasics.com/how-to-control-the-raspberry-pi-gpio-using-ifttt/)
- [Hackster.io og IFTTT](https://www.hackster.io/ifttt)

---

### 6.5 Vefþjónusta með RPi myndavél (30%) 
Notaðu [TenserFlow](https://www.tensorflow.org/lite/examples) eða [OpenCV](https://opencv.org/) með RPi myndavél fyrir greiningu á lit, hlut eða andlit.

<!--
**Til skoðunar**
- [RPI.zero: 4.2. Capturing to an OpenCV object](https://picamera.readthedocs.io/en/release-1.13/recipes2.html#capturing-to-an-opencv-object)
- [Train a fruit quality detector (color detection)](https://github.com/microsoft/IoT-For-Beginners/blob/main/4-manufacturing/lessons/1-train-fruit-detector/README.md)
- [Train a stock detector (object detection)](https://github.com/microsoft/IoT-For-Beginners/blob/main/5-retail/lessons/1-train-stock-detector/README.md#train-a-stock-detector)
-->

---

### Námsmat
- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnir og myndbönd af verklegum tilraunum.


   
