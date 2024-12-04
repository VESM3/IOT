## RPi Myndavélar

Rpi myndavélar (týpur):
[Software](https://www.raspberrypi.com/documentation/computers/camera_software.html)

- [RPi Camera Module 2](https://www.raspberrypi.com/products/camera-module-v2/)
   - 18 stykki (skólaeign) 
   - 8 megapixel
   - kom 2016
- [RPi Camera Module 3](https://www.raspberrypi.com/products/camera-module-3/)
   - tvær útgáfur:
      - standard (4.300 kr) 10 cm fókus, 75 gráður
      - wide (6.000 kr)  5 cm fókus, 120 gráður
   - með auto-focus og fókusfjarlægð er kóðanleg
   - with or without an infrared filter
   - 12 megapixel
   - kom 2023
- [RPi AI camera](https://www.raspberrypi.com/products/ai-camera/)
   - 11.500 kr á [PiHut](https://thepihut.com/products/raspberry-pi-ai-camera)
   - virkar á rpi 4, 5 og zero 2
   - byggt á [Sony IMX500 Intelligent Vision Sensor](https://developer.sony.com/imx500)

> [V2 vs V3 samanburður](https://dphacks.com/2023/01/18/raspberry-pi-camera-module-3-comparison/) <br>
> [Raspberry Pi Camera Compatibility RpiCam](https://orionrobots.co.uk/2024/06/04/raspberry-pi-camera-compatibility.html)

---


### 1. Raspberry Pi OS og takki með GPIO (15%)
1. Fylgdu eftirfarandi [leiðbeiningum](https://github.com/VESM3/IOT/blob/main/Efni/h23_RPi_uppsetning.md#2-a%C3%B0-tengjast-raspberry-pi-me%C3%B0-ssh-%C3%BEarf-a%C3%B0-gera-fyrst)
1. Láttu LED blikka á brauðbretti með python kóða og `GPIO Zero` safninu. Nýttu þér kóðalausnir í [Basic Recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html). Hér er dæmi um  [pinout](https://gpiozero.readthedocs.io/en/stable/cli_tools.html#pinout).
1. Bættu við takka og útbúðu fall sem sér um að starta LED blikkinu. 

> Hvað ætli `pause()` skipunin geri? Hver er munurinn á `when_pressed`, `is_pressed` og `wait_for_press`? 

---

### 2. Rpi myndavél 

#### RPi4 með Bullsey OS
1. **Slökktu** á RPi4 og jarðtengdu þig áður en þú tengir [Picamera V2](https://www.raspberrypi.com/documentation/accessories/camera.html). 
1. Skrifaðu python kóða til að takta mynd með 1024x768 upplausn af sjálfum þér með PiCam og vistaðu myndina. Sjá nánar [libcamera](https://www.raspberrypi.com/documentation/computers/camera_software.html) og [picamera2](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf).
1. Bættu við 3 sek. timer með takka til þess að taka sjálfsmyndina.
   
> Í `sudo raspi-config` í Interface Options þarf að  `disable Legacy Camera`
> Það er ekki hægt að nota Picamera safnið (gamalt) með Bullsey stýrikerfinu (eða nýrra).

#### RPi Zero með Buster OS (ef RPi4 virkar alls ekki)
1. hostname: V23vesmX, aðgangur: `pi`, lykilorð: `verksmidja3`
1. **Slökktu** á RPi og jarðtengdu þig áður en þú tengir [Picamera V2](https://www.raspberrypi.com/documentation/accessories/camera.html).
1. [RPi Zero tengileiðbeiningar](https://www.youtube.com/watch?v=zFAX4pH1BPA).  
1. Skrifaðu python kóða til að takta mynd með 1024x768 upplausn af sjálfum þér með einhverjum effect með PiCam og vistaðu á skjáborðinu. `camera.capture('/home/pi/Desktop/image.jpg')`, sjá [tutorial](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2).
1. Notaðu [Picamera](https://picamera.readthedocs.io/en/release-1.13/recipes1.html#) safnið og bættu við 3 sek. timer með takka til þess að taka myndina, sjá nánar [Button controlled camera](https://gpiozero.readthedocs.io/en/stable/recipes.html#button-controlled-camera)

> RPi Zero virkar ekki með libcamera eða Picamera2. 

---

### 3. PIR hreyfiskynjari 

1. Kynntu þér [PIR](https://lastminuteengineers.com/pir-sensor-arduino-tutorial/) og notaðu hreyfiskynjarann til að kveikja á LED, [sýnidæmi](https://gpiozero.readthedocs.io/en/stable/recipes.html#motion-sensor).
1. Taktu ljósmynd þegar PIR hreyfiskynjari fer í gang.

PIR Stillingar:
- stilltu `sensitivity` og `time-delay`.
- stilltu jumper á `Single Trigger Mode`.
- taktu linsu af PIR til að þrengja IR svið. 
- HC-SR501 tekur um 30 til 60 sekúndur að byrja, falskar niðurstöður þangað til.

---

### 4. IFTTT (If This Then That) 
1. Búðu til [IFTTT](https://help.ifttt.com/hc/en-us/articles/115010158167-How-does-IFTTT-work-) aðgang og skoðaðu vefþjónustu sem er í boði. Búðu til eigið [IFTTT applet](https://help.ifttt.com/hc/en-us/articles/360021401373-Creating-your-own-Applet) (ókeypis útgáfu) og sameinaðu tvær þjónustur að eigin vali.
1. Með [Webhooks](https://ifttt.com/explore/what-is-a-webhook) er hægt að senda og taka við `triggers` með HTTP Requests (GET og POST). Notaðu Webhooks með IFTTT til að fá tilkynningu (push notification) þegar smellt er á takka sem er tengdur við RPI. [Sýnidæmi](https://pimylifeup.com/using-ifttt-with-the-raspberry-pi/).
1. Sendu tilkynningu með IFTT Webhooks þegar mynd er tekin með hreyfiskynjara.

> [DIY IFTTT projects on Hackster.io](https://www.hackster.io/ifttt) 
> Pass að  taka út `{ }` fyrir key og event.

---

### 5. Myndgreiningavefþjónusta 

Myndgreiningavefþjónustur eru sniðugar til að greina hluti, andlit, liti og texta á ljósmyndum. Notaðu [Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/#overview) frá Microsoft Azure til að greina ljósmynd. 

1. Myndgreining með Computer Vision (fartölva)
   1. Skráðu þig inn á [Azure](https://azureforeducation.microsoft.com/devtools) með skólanetfanginu. Veldu svo _Access student benefits_ og _signup_.
   1. Gerðu viðeigandi stillingar hjá Azure [myndband](https://www.youtube.com/watch?v=1VB_QrHm_nY&ab_channel=JieJenn) til að geta notað Computer Vision. Hér eru frekari [leiðbeiningar](https://www.pluralsight.com/guides/computer-vision-with-microsoft-azure).
   1. Notaðu VSCode og python á fartölvunni, sjá [kóðadæmi](https://github.com/VESM3/IOT/blob/main/Efni/ComputerVisionDemo.py) til að greina ljósmynd (minna en 4MB).
1. Notaðu RPi, PiCam (local ljósmynd) og Computer Vision saman og birtu niðurstöður á skjá. Sjá [kóðabúta](https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py) úr skránni. (ekki nota `pillow` safnið)
1. Bættu hreyfiskynjaranum við sem tekur mynd og lætur greina myndina, birtu niðustöður á skjá.
1. Notaðu myndgreininguna (JSON niðurstöður) til að kveikja á LED ef það líkist einhverju. 

<!--  1. [Call the Image Analysis API](https://learn.microsoft.com/en-us/azure/cognitive-services/computer-vision/how-to/call-analyze-image?source=recommendations&tabs=python#submit-data-to-the-service) og 
-->

**Bjargir**

1. [Computer Vision documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/)
1. [Computer Vision SDK for Python](https://docs.microsoft.com/en-us/python/api/overview/azure/cognitiveservices-vision-computervision-readme?view=azure-python-preview)

> _Aðrar áhugaverðar [vefþjónustur:]( https://azure.microsoft.com/en-us/products/cognitive-services/#api) Language og Speech_


  
