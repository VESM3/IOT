# Tímaverkefni 1

- Námsmat 17% af heildareinkunn
- Einstaklingsverkefni

---

### 1. Samsettning á fígúru (**50%**)

Eftirfarandi þarf að gera:

- [ ] skrúfa [röra festingu](https://github.com/VESM3/IOT/blob/main/Myndir/samsettning/festing.jpg) á borðbplötu.
- [ ] setja  [pvc rör](https://github.com/VESM3/IOT/blob/main/Myndir/samsettning/pvc_ror.jpg) (20 cm langt) í festingu.
- [ ] Setja  [kross](https://github.com/VESM3/IOT/blob/main/Myndir/samsettning/kross.jpg) á hinn endann f á rörinu. 
- [ ] festa [MG996R](https://github.com/VESM3/IOT/blob/main/Myndir/samsettning/Servo-MG996.jpg) servo mótor með 4 skrúfum og fylgihlutum (poki) við [MG996 servo festingu](https://github.com/VESM3/IOT/blob/main/Myndir/samsettning/mount_servo.jpg).
- [ ] setja augu með leds í hauskúpu ([sjá mynd fyrir lóðun](https://github.com/VESM3/IOT/blob/main/Myndir/augu.png)) og tengja víra við mini brauðbretti í hauskúpu ([tengimynd](https://github.com/VESM3/IOT/blob/main/Myndir/augu_breadboard.png)).
- [ ] festa [MG90S servo](https://github.com/VESM3/IOT/blob/main/Myndir/samsettning/MG90S.webp) við kjálk með skrúfu.
- [ ] festa [servo Hub-Shaft](https://github.com/VESM3/IOT/blob/main/Myndir/samsettning/shaft_servo.jpg) með að skrúfa það við botninn á hauskúpu og svo eina skrúfu í MG996.
- [ ] festa brauðbretti (líma) með esp32 og staðsetja aflgjafa á borðplötu.
- [ ] tengja ESP32 sem er á stóru brauðbretti á borðplötu við mini brauðbrettið í hauskúpu. 
- [ ] ganga frá öllum vírum snyrtilega.


---

### 2. NeoPixel (**25%**)

Náðu í nýjustu **uppfærðu** útgáfuna af ESP-32 [leiðbeiningar](https://github.com/VESM1VS/AFANGI/blob/main/Kennsluefni/ESP_Uppsetning.md) og keyrðu halló heimur (blikk) í MicroPython.
Notaðu NeoPixel fyrir bæði augun og láttu þær blikka í mismunandi takti með mismunandi litbrigðum og birtustigi. Notaðu Timer.

**Kóðasýnidæmi:**

<details>
<summary>NeoPixel</summary>
<br>

```python

from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

neo = NeoPixel(Pin(42), 2)   #  2 x Leds

# slökktu á báðum leds
neo.fill([0, 0, 0])

# Allar NeoPixel perurnar lýsa rauðu ljósi í eina sekúndu með fill aðferð.
neo.fill([255, 0, 0])
neo.write()
sleep_ms(1000)

# LED nr 2 er lýst með grænum lit
neo[1] = [0, 255, 0]
neo.write()

```

</details>
<details>
  <summary>Timer</summary>

```python
from machine import Pin, Timer
from time import sleep_ms
from neopixel import NeoPixel

neo = NeoPixel(Pin(45), 8)

neo.fill([0, 0, 0])
neo.write()

RAUTT = [255, 0, 0]
BLATT = [0, 0, 255
SLOKKT = [0, 0, 0]

syna_rautt = True

def blikka_null_og_einn(t):
    global syna_rautt
    if syna_rautt: # if syna_rautt == True
        neo[0] = RAUTT
        neo[1] = BLATT
        neo.write()
    else:
        neo[0] = BLATT
        neo[1] = RAUTT
        neo.write()
    syna_rautt = not syna_rautt

tim = Timer(0)
tim.init(period=1000, mode=Timer.PERIODIC, callback=blikka_null_og_einn)

```
</details>

**Til upprifjunar:** [Stafræn gildi](https://github.com/VESM1VS/AFANGI/blob/main/Kennsluefni/digital.md) og [Hliðræn gildi](https://github.com/VESM1VS/AFANGI/blob/main/Kennsluefni/analog.md)

> **Note**
> **Ekki** nota pinna; GPIO0, GPIO3, GPIO19, GPIO20, GPIO45, GPIO46. 

<!-- [`ticks_ms`](https://github.com/VESM2VT/ESP32/blob/main/kodi/ticks.md) og [sýnidæmi](https://wokwi.com/projects/390068539029210113). -->

---

### 3. Servo (**25%**)
Settu upp [þessa](https://raw.githubusercontent.com/VESM3/IOT/refs/heads/main/Myndir/servo_kjalki.png) rás á brauðbretti og MG996R servo. 

:warning: Þegar unnið er með mótora er best að nota utanaðkomandi spennugjafa fyrir þá af því að mótorar geta dregið meiri straum en ESP ræður við. Þú færð spennugjafa hjá kennara. Servo þarf 5V.

Fyrir servo mótorinn þarftu að sækja [þetta](https://github.com/pvanallen/esp32-getstarted/blob/master/examples/servo.py) klasasafn. Sjá nánar [hér](https://github.com/pvanallen/esp32-getstarted/blob/master/docs/servo.md) kóðadæmi og að uppphafstilla min og max á servo.

#### Verkefnið
1. Losaðu kjálkann með MG90S micro servo frá hauskúpunni og stilltu rétt breiddarsvið (min og max) ef þú þarft. Finndu út upphafstöðu í gráðum þegar hann er með lokaðan munn.
1. Settu kjálkann aftur í. Láttu servo opna og loka munn einsog hægt er 5 gráður í einu, þetta á að endurtaka sig að eilífu.

---

## Námsmat og skil

- Skilaðu öllum kóða á Innu
  - Passaðu að þú getir útskýrt kóðann sem þú skilar fyrir kennara.
- Yfirferð á sér stað í tíma. Einkunn fyrir hvern lið: 
    - 10 lausn er vel útfærð.
    - 7.5 lausn er smávægilega ábótavant.
    - 5 lausn er ábótavant, helmingur er vel útfærður.
    - 2.5 lausn er stórlega ábótavant.
    - 0 lausn vantar eða óunnin.



