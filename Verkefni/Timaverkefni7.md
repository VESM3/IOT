## Tímaverkefni 7 (9%)

- Einstaklingsverkefni
- Vefþjónustur

<!-- [Services for Things (myndbandskynning)](https://learn.adafruit.com/all-the-internet-of-things-episode-three-services/services-for-things) -->

---

### 7.1 IFTTT (If This Then That) (10%)
1. Búðu til aðgang og prófað einhverjar áhugverða IFTTT vefþjónustu sem er í boði. [How does IFTTT work?](https://help.ifttt.com/hc/en-us/articles/115010158167-How-does-IFTTT-work-) og [listi af þjónustum](https://ifttt.com/services) flokkað.
2. Búðu til eigið applet (free útgáfan) og sameinaðu tvær þjónustur að eigin vali. [Creating your own Applet](https://help.ifttt.com/hc/en-us/articles/360021401373-Creating-your-own-Applet)

---

### 7.2 IFTTT með Adafruit IO - Any new data (20%)
Notaðu takka á brauðbretti sem er tengt við RaspberryPi sem sendir skilaboð til Adafruit IO þegar ýtt er á hann. <br>
Notaðu IFTTT sem vaktar þetta `feed` hjá Adafruit IO og lætu þig vita (td. gmail eða sms) þegar smellt er á takkann. <br>
Sjá [IFTTT AdafruitIO leiðbeiningar](https://learn.adafruit.com/using-ifttt-with-adafruit-io/ifttt-to-adafruit-io-setup), notaðu _Any new data_ trigger <br>

- [Zapier](https://zapier.com/) með AdafruitIO er annar valkostur í stað IFTTT

---

### 7.3 IFTTT með Adafruit IO - Monitor a feed (20%)
1. Tengdu [jarðvegsmælir](https://www.sigmaelectronica.net/wp-content/uploads/2018/04/sen0193-humedad-de-suelos.pdf) við ESP32 til að kanna rakastig "jarðvegs".
1. Notaðu IFTTT sem vaktar þetta `feed` hjá Adafruit IO og lætu þig vita (td. gmail) þegar "jarðvegur" verður of þurr (notaðu gildi sem hentar tilraun).

<!--
- [Adafruit IO Time Tracking Cube með ESP32 og Zapier](https://github.com/adafruit/Adafruit_IO_Arduino/blob/master/examples/adafruitio_24_zapier/adafruitio_24_zapier.ino) og 
https://learn.adafruit.com/time-tracking-cube
-->

---

### 7.4 IFTTT WebHooks (20%) 
Með Webhooks er hægt að senda og taka við `triggers` með HTML POST og GET requests, sjá nánar [What is a Webhook? - IFTTT](https://ifttt.com/explore/what-is-a-webhook)

1. Notaðu takka með RPi. Notaðu Webhooks með IFTTT til að fá tilkynningu (push notification) þegar það hefur verið smellt á takkann, sjá td. [How to control RPi GPIO pins with IFTTT](https://www.circuitbasics.com/how-to-control-the-raspberry-pi-gpio-using-ifttt/). Leystu þetta án þess að nota Adafruit<br>

**Aðrar bjargir:**
- [Push notification, motion detection](https://iot4beginners.com/ifttt-with-raspberry-pi/)
- [Hackster.io og IFTTT](https://www.hackster.io/ifttt)

---

### 7.5 Myndgreining (30%) 


[Myndgreiningavefþjónustur](https://nordicapis.com/7-best-image-recognition-apis/) eru sniðugar til að greina hluti, andlit, liti og texta á ljósmyndum.
Notaðu [Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/#overview) frá Microsoft Azure (notaðu Github Student Developer Pack) til að greina hluti á ljósmynd. 

1. Myndgreining með Computer Vision
   1. notaðu VSCode og python á fartölvunni.
   1. notaðu Computer Vision vefþjónustuna til að greina ljósmynd (minna en 4MB).
   1. birtu niðurstöðurnar frá myndgreiningunni.
1. Notaðu RPi, PiCam og Computer Vision saman og birtu niðurstöður.

**Bjargir**
- [Computer Vision with Microsoft Azure](https://www.pluralsight.com/guides/computer-vision-with-microsoft-azure)
- [Computer Vision documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/)
- [Computer Vision SDK for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python-preview)
- [myndbönd](https://www.youtube.com/hashtag/azureinpython)

---

### Námsmat
- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnir og myndbönd af verklegum tilraunum.


   
