

## RPi myndavél 

#### Taka mynd með ```rpicam```

Byrjaðu á að opna terminal í gluggaumhverfinu og keyrðu eftirfarandi:

```bash
rpicam-still --output rpicam_mynd.jpg
```

Eftir smá stund opnast forskoðunargluggi og þegar hann hverfur getur þú opnað myndina með því að skrifa inn

```bash
open rpicam_mynd.jpg
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
