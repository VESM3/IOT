## Tímaverkefni 3 _drög_
- 15% af heildareinkunn.
- Viðfangsefni: Raspberry Pi, PiCam, PIR, vefþjónustur (IFTTT, myndgreining).

---

### 1. Raspberry Pi OS og GPIO (15%)
1. Fylgdu eftirfarandi [leiðbeiningum](https://github.com/VESM3/IOT/blob/main/Efni/h23_RPi_uppsetning.md#2-a%C3%B0-tengjast-raspberry-pi-me%C3%B0-ssh-%C3%BEarf-a%C3%B0-gera-fyrst)
1. Láttu LED blikka á brauðbretti með python kóða og `GPIO Zero` safninu. Nýttu þér kóðalausnir í [Basic Recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html). Hér er dæmi um  [pinout](https://gpiozero.readthedocs.io/en/stable/cli_tools.html#pinout).
1. Bættu við takka og útbúðu fall sem sér um að starta LED blikkinu. 

> Hvað ætli `pause()` skipunin geri? Hver er munurinn á `when_pressed`, `is_pressed` og `wait_for_press`? 

<!-- 
Notaðu [T-Coppler](https://www.adafruit.com/product/2028) með brauðbrettinu
-->

---

### 2. Myndvélin (20%)

1. **Slökktu** á RPi og jarðtengdu þig áður en þú tengir [Picamera V2](https://www.raspberrypi.com/documentation/accessories/camera.html). 
1. Skrifaðu python kóða til að takta mynd með 1024x768 upplausn af sjálfum þér með einhverjum effect með PiCam og vistaðu á skjáborðinu. 
   1. [libcamera](https://www.raspberrypi.com/documentation/computers/camera_software.html) 
   1. [picamera2](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf) 
1. Bættu við 3 sek. timer með takka til þess að taka sjálfsmyndina.


<!--
- [RPi Zero tengileiðbeiningar](https://www.youtube.com/watch?v=zFAX4pH1BPA).  
- RPi Zero virkar ekki með Picamera 2 eða libcamera söfnum. 
- ath. `raspistill` skipunin er úreld.
- `camera.capture('/home/pi/Desktop/image.jpg')`, 
- [Button controlled camera](https://gpiozero.readthedocs.io/en/stable/recipes.html#button-controlled-camera)
- [Picamera](https://picamera.readthedocs.io/en/release-1.13/recipes1.html#) safnið. 
-->

---

### 3. PIR hreyfiskynjari (15%) 

1. Kynntu þér [PIR](https://lastminuteengineers.com/pir-sensor-arduino-tutorial/) og notaðu hreyfiskynjarann til að kveikja á LED, [sýnidæmi](https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor).
1. Taktu ljósmynd þegar PIR hreyfiskynjari fer í gang.

PIR Stillingar:
- stilltu `sensitivity` og `time-delay`.
- stilltu jumper á `Single Trigger Mode`.
- taktu linsu af PIR til að þrengja IR svið. 
- HC-SR501 tekur um 30 til 60 sekúndur að byrja, falskar niðurstöður þangað til.

---

### 4. IFTTT (If This Then That) (20%) 
1. Búðu til [IFTTT](https://help.ifttt.com/hc/en-us/articles/115010158167-How-does-IFTTT-work-) aðgang og skoðaðu vefþjónustu sem er í boði. Búðu til eigið [IFTTT applet](https://help.ifttt.com/hc/en-us/articles/360021401373-Creating-your-own-Applet) (ókeypis útgáfu) og sameinaðu tvær þjónustur að eigin vali.
1. Með [Webhooks](https://ifttt.com/explore/what-is-a-webhook) er hægt að senda og taka við `triggers` með HTTP Requests (GET og POST). Notaðu Webhooks með IFTTT til að fá tilkynningu (push notification) þegar smellt er á takka sem er tengdur við RPI. [Sýnidæmi](https://pimylifeup.com/using-ifttt-with-the-raspberry-pi/).
1. Sendu tilkynningu og mynd með IFTT Webhooks þegar mynd er tekin.

> [DIY IFTTT projects on Hackster.io](https://www.hackster.io/ifttt) 

---

### 5. Myndgreiningavefþjónusta (30%)

Myndgreiningavefþjónustur eru sniðugar til að greina hluti, andlit, liti og texta á ljósmyndum. Notaðu [Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/#overview) frá Microsoft Azure til að greina ljósmynd. 

1. Myndgreining með Computer Vision (fartölva)
   1. Skráðu þig inn á [Azure](https://azureforeducation.microsoft.com/devtools) með skólanetfanginu. 
   1. Gerðu viðeigandi stillingar hjá Azure [myndband](https://www.youtube.com/watch?v=1VB_QrHm_nY&ab_channel=JieJenn) til að geta notað Computer Vision. Hér eru frekari [leiðbeiningar](https://www.pluralsight.com/guides/computer-vision-with-microsoft-azure).
   1. Notaðu VSCode og python á fartölvunni, sjá [kóðadæmi](https://github.com/VESM3/IOT/blob/main/Efni/ComputerVisionDemo.py) til að greina ljósmynd (minna en 4MB).
1. Notaðu RPi, PiCam (local ljósmynd) og Computer Vision saman og birtu niðurstöður á skjá. Sjá [kóðadæmi](https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py)
1. Bættu hreyfiskynjaranum við sem tekur mynd og lætur greina myndina, birtu niðustöður á skjá.
1. Notaðu myndgreininguna (JSON niðurstöður) til að kveikja á LED ef það líkist einhverju. 

<!--  1. [Call the Image Analysis API](https://learn.microsoft.com/en-us/azure/cognitive-services/computer-vision/how-to/call-analyze-image?source=recommendations&tabs=python#submit-data-to-the-service) og 
-->

**Bjargir**

1. [Computer Vision documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/)
1. [Computer Vision SDK for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python-preview)

> _Aðrar áhugaverðar [vefþjónustur:]( https://azure.microsoft.com/en-us/products/cognitive-services/#api) Language og Speech_

---

### Námsmat og skil

- Skilaðu á Innu kóðalausnum.
- Yfirferð á sér stað í tíma. 
- Einkunn fyrir hvern lið: 
    - 4/4 lausn er vel útfærð.
    - 3/4 lausn er smávægilega ábótavant (vantar smá upp á).
    - 2/4 lausn er ábótavant, helmingur er vel útfærður.
    - 1/4 lausn er stórlega ábótavant, tíma og kóðavinna lögð í lausn.
    - 0/4 lausn vantar eða óunnin.

  
