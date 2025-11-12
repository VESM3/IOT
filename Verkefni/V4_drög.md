# Tímaverkefni 4 

- Námsmat 17% af heildareinkunn
- Einstaklingsverkefni
- RPi, myndavél og vefþjónusta

### 1. RPi uppsetning (20%)

Byrjaðu á að setja SSD kortið í Pi og tengdu myndavélina í samráði við kennara. Næst tengirðu Pi við rafmagn.

:warning: Til að geta tengst RPi með SSH þá þarf fartölvan þín að vera tengd ```TskoliVESM``` þráðlausa netinu (lykilorð ```Fallegurhestur```) :warning:

Tengstu RPi með SSH með því að slá eftirfarandi inn í Terminal (PowerShell á Windows, Terminal á Apple):

```bash
ssh pi@hYXX
```

Lykilorðið er ```Verksm1dja``` (ath. 1 (einn) í stað i).

Þar sem Y er hópurinn sem þú ert í og XX númerið á SSD kortinu sem þú fékkst.

Uppfærðu svo stýrikerfið á Pi með því að gefa þessa skipun:

```bash
sudo apt update && sudo apt full-upgrade
```

Sæktu svo fulla útgáfu af python.

```bash
sudo apt install python3-full
```

#### RPi Connect

Næst þarf að virkja tvær þjónustur en það eru ```RPi Connect``` og ```VNC```.

```bash
sudo raspi-config
```

Veldu svo ```Interface Options```. Notaður örvatakkana til að færa þig upp/niður og síðan Tab takkann til að velja ```<Select>``` þar sem þú smellir að Enter.

![raspi-config-main](https://raw.githubusercontent.com/VESM3/IOT/refs/heads/main/Myndir/raspi_config_main.png)

Farðu svo í RPi Connect og veldu ```<Yes>``` og gerðu svo það sama fyrir ```VNC```

![raspi-config-interface](https://raw.githubusercontent.com/VESM3/IOT/refs/heads/main/Myndir/raspi_config_interface.png)

Að lokum velur þú svo ```<Finish>``` til að komast út úr ```raspi-config```

Virkjaðu næst RPi Connect með því að gefa eftirfarandi skipun:

```bash
rpi-connect on
```

Næst þarftu að skrá þig inn með því að gefa eftirfarandi skipu:

```bash
rpi-connect signin
```

Þá færðu slóð sem þú þarft að fara inn á með vafranum þínum.

```
Complete sign in by visiting https://connect.raspberrypi.com/verify/XXXX-XXXX
```

```bash
https://connect.raspberrypi.com/verify/XXXX-XXXX
```
Þar þarftu svo að búa þér til reikning (Raspberry Pi ID). Að lokum þarftu svo að gefa Pi-inum nafn og þá ættir þú að geta tengst honum með gluggaumhverfi með því að velja **Screen Sharing** úr **Connect via**.

Núna getur þú tengst bæði Terminal og gluggaumhverfi án þess að fartölvan þín sé tengd við TskoliVESM þráðlausa netið.

Til að tengjast þessu seinna getur þú farið inn á [þessa](https://connect.raspberrypi.com/) slóð.

### 2. RPi myndavél (40%)

#### Taka mynd með ```rpicam```

Byrjaðu á að opna terminal í gluggaumhverfinu og keyrðu eftirfarandi:

```bash
rpicam-still --output rpicam_mynd.jpg
```

Eftir smá stund opnast forskoðunargluggi og þegar hann hverfur getur þú opnað myndina með því að skrifa inn

```bash
open prufa.jpg
```

eða með því að opna skrárkerfið og tvísmella á myndina.

[Hér](https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-apps) má finna upplýsingar um ýmis ```rpicam``` forrit sem eru á RPi.

#### Taka mynd með python

Opnaðu Thonny á RPi og settu þennan kóða þar inn:

```python
from picamera2 import Picamera2, Preview
import time

# búa til tilvik af myndavélinni
picam2 = Picamera2()
# stillingar fyrir forskoðunina
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
# ræsa forskoðun
picam2.start_preview(Preview.QT)
# taka myndina
picam2.start()
time.sleep(2)
# vista myndina
picam2.capture_file("python_mynd.jpg")
# slökkva á forskoðunarglugganum
picam2.stop_preview()
```

Þessi kóði sýnir forskoðunarglugga og tekur síðan mynd. Forskoðunarglugginn krefst þess að kóðinn sé keyrður í gluggaumhverfi. Vandamálið við þetta er að sjálfgefnu myndirnar eru í mikilli upplausn (allt að 4608*2592) og RPi Zero 2 ræður ekki vel við þá stærð.

En taka þarf mynd án þess að vera með gluggaumhverfi má keyra eftirfarandi kóða **í Terminal** og af því að RPi Zero 2 er með lítið vinnsluminni og hægan örgjörva er þetta oftast besta leiðin:

```python
from picamera2 import Picamera2
import time
picam2 = Picamera2()
picam2.start()
picam2.capture_file("terminal_mynd.jpg")
```

#### Stillingar á myndatöku

Hægt er að stilla myndavélina á marga vegu t.d.:
```python
from picamera2 import Picamera2
import time
picam2 = Picamera2()
picam2.start()
with picam2.controls as controls:
        controls.Sharpness = 0.5
        controls.Saturation = 3.0
picam2.capture_file("terminal_mynd.jpg")
```

Sjá fleiri dæmi um mismunandi stillingar á myndavélinni í köflum 4, 5 og 6 í [Picamera2 Library bókinni](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf).

#### **Verkefnið**

Kynntu þér [Blue Dot](https://bluedot.readthedocs.io/en/latest/) og gerðu bluedot forrit sem hefur tvo takka, annar takkinn á að taka venjulega mynd en hinn takkinn á að taka mynd þar sem stillingum myndavélarinnar hefur verið breytt á einhvern skemmtilegan hátta (frjáls útfærsla).

### 3. RPi Myndgreingavefþjónusta (40%)

Myndgreiningavefþjónustur eru sniðugar til að greina hluti, andlit, liti og texta á ljósmyndum. Notaðu [Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/#overview) frá Microsoft Azure til að greina ljósmynd. 

1. Myndgreining með Computer Vision (fartölva)
   1. Skráðu þig inn á [Azure](https://azureforeducation.microsoft.com/devtools) með skólanetfanginu. Veldu svo _Access student benefits_ og _signup_.
   1. Gerðu viðeigandi stillingar hjá Azure [myndband](https://www.youtube.com/watch?v=1VB_QrHm_nY&ab_channel=JieJenn) til að geta notað Computer Vision. Hér eru frekari [leiðbeiningar](https://www.pluralsight.com/guides/computer-vision-with-microsoft-azure).
   1. Notaðu VSCode og python á fartölvunni, sjá [kóðadæmi](https://github.com/VESM3/IOT/blob/main/Efni/ComputerVisionDemo.py) til að greina ljósmynd (minna en 4MB).
1. Notaðu RPi, PiCamera2 (local ljósmynd) og Computer Vision saman og birtu niðurstöður á skjá. Sjá [kóðabúta](https://github.com/Azure-Samples/cognitive-services-quickstart-code/blob/master/python/ComputerVision/ImageAnalysisQuickstart.py) úr skránni. (ekki nota `pillow` safnið)

---

## Námsmat og skil

- Skilaðu öllum kóða á Innu
  - Passaðu að þú getir útskýrt kóðann sem þú skilar fyrir kennara.
- Yfirferð á sér stað í tíma. Einkunn fyrir hvern lið: 
    - 10 lausn er vel útfærð.
    - 7.5 lausn er smávægilega ábótavant (vantar smá upp á).
    - 5 lausn er ábótavant, helmingur er vel útfærður.
    - 2.5 lausn er stórlega ábótavant, en tíma- og kóðavinna lögð í lausn.
    - 0 lausn vantar eða óunnin.
