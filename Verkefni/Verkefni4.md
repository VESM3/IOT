# Tímaverkefni 4

- Námsmat 15% af heildareinkunn
- Einstaklingsverkefni
- Raspberry Pi

---

### 1. Raspberry Pi (30%)

Fylgdu eftirfarandi [leiðbeiningum](https://github.com/VESM3/IOT/blob/main/Efni/rpi_mediapipe_uppsetning.md) til að:
1. Setja upp RPi stýrikerfi á Raspberry Pi.
1. Tengjst RPi með SSH.
1. Tengjast RPi með RPi Desktop viðmóti í fartölvu.
1. Setja upp söfn til að geta notað MediaPipe frá Google með RPi myndavél.

--- 

### 2. RPi myndavél (30%)

Tengdu myndavélina í samráði við kennara.

#### Taka mynd með ```rpicam```

Byrjaðu á að opna terminal í gluggaumhverfinu og keyrðu eftirfarandi:

```bash
rpicam-still -o ljosmynd.jpg --width 640 --height 480
```

Eftir smá stund opnast forskoðunargluggi og þegar hann hverfur getur þú opnað myndina með því að skrifa inn

```bash
open ljosmynd.jpg
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

# stillingar fyrir forskoðun og upplausn (640x480)
camera_config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(camera_config)

# ræsa forskoðun
picam2.start_preview(Preview.QT)

# taka myndina
picam2.start()
time.sleep(2)

# vista myndina
picam2.capture_file("python_mynd.jpg")

# slökkva á forskoðunarglugganum og loka myndavélinni
picam2.stop_preview()
picam2.close()
```

Þessi kóði sýnir forskoðunarglugga og tekur síðan mynd. Forskoðunarglugginn krefst þess að kóðinn sé keyrður í gluggaumhverfi. Vandamálið við þetta er að sjálfgefnu myndirnar eru í mikilli upplausn (allt að 4608*2592) og RPi ræður ekki vel við þá stærð nema upplausn sé minkuð. Til að létta á örgjörvanum er hægt að taka mynd án þess að vera með gluggaumhverfi með að keyra eftirfarandi kóða **í Terminal**:


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

#### Verkefnið:

1. Skrifaðu kóða sem tekur mynd á 5 sekúndna fresti og geymir 5 síðustu myndirnar sem teknar voru, þegar sjötta myndin er tekin á hún að skrifast yfir elstu myndina.
2. Sýndu hæfni þína í að skrifa kóða sem tekur mynd sem hefur einhverjar skemmtilegar stillingar (sjá [Picamera2 Library bókina](https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf)), frjáls útfærsla (upplausn, litir, skráartegund eða annað).

---

### 3. MediaPipe (40%) 

Vélarnám (e. Machine Learning) er sniðugt að nota til að greina hluti, andlit, liti og texta á ljósmyndum og myndbandsupptökum jafnvel í rauntíma. Við munum notast við [MediaPipe](https://developers.google.com/mediapipe) frá Google.

<details>
<summary>Kóðadæmi (object detection)</summary>
       
```python
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# 1. Vísað á staðbundið líkan sem þú hefur hlaðið niður á tölvuna
MODEL_PATH = "efficientdet_lite0.tflite"
base_options = python.BaseOptions(model_asset_path==MODEL_PATH)
options = vision.ObjectDetectorOptions(base_options=base_options, score_threshold=0.5)
detector = vision.ObjectDetector.create_from_options(options)

# 2. Myndin sem á að greina lesin inn
image = mp.Image.create_from_file('myndin_thin.jpg')

# 3. Greining keyrð á tölvunni þinni (engin netsending)
detection_result = detector.detect(image)

# 4. Niðurstöður prentaðar út
# detection_result er gagnahlutur (object) sem inniheldur niðurstöður þar á meðal detections (listi)
for detection in detection_result.detections:
    category = detection.categories[0]
    heiti = category.category_name
    likur = category.score
    print(f"Fann: {heiti} (Líkur: {likur:.2f})")

"""
# Uppbygging á stökum hlut innan detection_result.detections (listi)
Detection(
  bounding_box=BoundingBox(origin_x=120, origin_y=50, width=200, height=350),
  categories=[
    Category(index=0, score=0.88, category_name='person', display_name='')
  ],
  keypoints=[]
)
"""

```

</details>


#### Verkefnið:
Þú ætlar í þessu verkefni að nota RPi ásamt RPi myndavélina til að greina hluti (object detection) með notkun MediaPipe, [youtube](https://www.youtube.com/watch?v=-RUVM_cXn18&list=PLOU2XLYxmsILxbiyDRGC94XuT2dBXNY3n). 

1. Vertu með tvo ólíka hluti (A og B) til að greina á milli, prófaðu [veflausnina](https://google-ai-edge.github.io/mediapipe-samples-web/#/vision/object_detector) til að velja hentuga hluti til að vinna með.
1. Taktu ljósmynd með RPi myndavél af hlutunum og notaðu [object detection python kóða](https://developers.google.com/edge/mediapipe/solutions/vision/object_detector/python) til að greina hlut á ljósmynd. Birtu niðurstöður; nafn á hlut og score í terminal.
1. Notaðu lifandi streymi og birtu skilaboðin "Réttur hlutur" ef hlutur A birtist á skjá, annars "Rangur hlutur" ef hlutur B birtist á skjá.


Þú þarft að sækja eftirfarandi model skrá (notaðu virtual umhverfi):
  ```bash
        wget -O model.tflite https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite0/int8/1/efficientdet_lite0.tflite
  ```

---

## Námsmat og skil

- Skilaðu öllum kóðalausnum í Canvas.
- Yfirferð á sér stað í tíma.
- Passaðu að þú getir útskýrt kóðann sem þú skilar fyrir kennara.
