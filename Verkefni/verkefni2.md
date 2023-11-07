## Tímaverkefni 2 

- Námsmat 15% af heildareinkunn.
- ESP-NOW, Wifi, Vefþjónn.
  
---

### 1. ESP-NOW. (20%)
Kynntu þér [ESPnow](https://docs.micropython.org/en/latest/library/espnow.html)  með því að lesa þessa [grein](https://dronebotworkshop.com/esp-now/) (lestu að kaflanum "MAC Address Sketch"). Hafðu eftirfarandi í huga meðan þú lest greinina:
- Hvernig er ESPnow ólíkt "venjulegu" WIFI eins og t.d. á fartölvunni þinni?
- Hversu stóra pakka (í bætum) er hægt að senda með ESPnow?
- Hversu mörg tæki er hægt að láta tala saman með ESPnow?
- Hvað er MAC vistfang (e. address)?

#### Hafa tvo Thonny glugga opna í einu
Í Thonny skaltu fara í Tools->Options og taka hakið úr *Allow only single Thonny instance*. Þá getur þú opnað tvo Thonny glugga. Á Mac þarf að opna glugga nr. 2 með því að fara í terminal og skrifa eftirfarandi: `open -n -a Thonny.app`

#### Finna MAC addressu á ESP32
Til að geta átt samskipti milli ESP-anna þarftu að finna MAC addressuna á þeim báðum. Farðu í REPL (Shell) hluta Thonny og sláðu inn eftirfarandi:
```python
import machine
machine.unique_id()
# strengurinn sem birtist er á forminu b'4\x85\x18n\x03\xf0'
```
Þá birtist MAC addressa ESP. Skráðu MAC addressu strengina hjá þér.

#### Hello World eða 123 halló?
Settu eftirfarandi kóða á annan ESP-inn þinn. Þessi kóði er fyrir sendingu á gögnum.
```python
# Kóðinn á ESP-inn sem sendir skilaboð
from network import WLAN, STA_IF
from espnow import ESPNow
from time import sleep_ms

# Virkja þráðlausa netið
sta = WLAN(STA_IF)
sta.active(True)

# Configure the ESP-NOW protocol and enable it
sendir = ESPNow()
sendir.active(True)

# Add a node (peer) that needs to communicate
hinn_esp_inn = b'4\x85\x18m\xc3\xd0'   # MAC address-an á hinum ESP-inum (móttakaranum)
sendir.add_peer(hinn_esp_inn)

teljari = 0

while True:
    # skilaboðin eru alltaf send sem strengur (eða bytestring) 
    skilabod = f"{teljari} halló"
    # Send a message
    sendir.send(hinn_esp_inn, skilabod, True) # skilabod breytist í bytestring við sendingu
    # hækkum teljara
    teljari += 1
    # endurtökum ferlið á 0,5 sek fresti
    sleep_ms(500)
  
```
Hér er svo kóðinn fyrir ESP-inn sem tekur á móti gögnunum.

```python
# Kóðinn fyrir ESP-inn sem móttekur skilaboðin
from network import WLAN, STA_IF
from espnow import ESPNow

# Virkja þráðlausa netið
sta = WLAN(STA_IF)
sta.active(True)

# Configure the ESP-NOW protocol and enable it
mottakari = ESPNow()
mottakari.active(True)

# Add a node (peer) that needs to communicate
hinn_esp_inn = b'4\x85\x18n\x03\xf0'   # MAC address-an á hinum ESP-inum (sendananum)
mottakari.add_peer(hinn_esp_inn)

while True:
    # Receive message
    sendandi, skilabod = mottakari.recv()
    if skilabod: # ef einhver skilaboð bárust (bytestring)
        # breytum bytestring í string (decode message)
        skilabod = skilabod.decode()  
        # skilaboðin eru á forminu "tala texti" 
        tala, texti = skilabod.split()
        # þurfum því að gera ráðstafanir til að geta notað töluna sem tölu
        tala = int(tala)
        print(f"{sendandi} sendi {tala} {texti}" )
```

**Verkefnið:**

1. Breyttu kóðanum hér fyrir ofan þannig að sendandinn sendir tvær handahófsvaldar (e. random) heiltölur á bilinu 1 til 100. Móttakarinn tekur svo við þeim, birtir báðar tölurnar, leggur þær saman og birtir niðurstöðuna.

2. Kynntu þér hvernig DHT11 (hita og rakamælir) virkar með því að skoða [kafla 24](https://github.com/VESM3/IOT/blob/main/Efni/Python_Tutorial_framleidandi.pdf). Tengdu svo DHT11 við sendi ESP-inn og sendu svo mælingarnar yfir á hinn. Birtu mælingarnar á tölvuskjá.

> [Sensor Data Sharing with ESP-NOW in MicroPython (asyncio)](https://www.donskytech.com/sensor-data-sharing-with-esp-now-in-micropython/)  _ítarefni_ <br> 
> [innbyggður hitamælir í ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s3/api-reference/peripherals/temp_sensor.html) _ítarefni (ekki nota)_

<!--
Þú finnur **dht** klasann [hér](https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_ESP32_S3/blob/main/Python/Python_Libraries/dht.py).
-->

---

### 2. ESP-NOW: two-way samskipti. (20%)

1. Tengdu ESP32 (mælir) við [LDR](https://www.donskytech.com/micropython-read-ldr-or-photoresistor/) sem svo sendir mælingarnar með ESPnow til annan ESP32 sem birtir gildin á tölvuskjá.
1. Ef birtumæling frá ESP32 (mælir) fer fyrir neðan ákveðin mörk (myrkur) í mælingu þá sendir ESP32 (controller) skilaboð um að kveikja á rautt LED hjá viðkomandi ESP32 (mælir). 


:warning: Ekki er hægt að nota pinna 11 - 18 með [ADC](https://github.com/VESM2VT/ESP32/blob/main/kennsluefni/analog.md#lesið-frá-pinna), pinnarnir virka þó fyrir alla aðra virkni (Pin inn og út og PWM).

> [Kóðadæmi](https://github.com/VESM3/IOT/tree/main/Kodi/ESPNow) með samskipti í báðar áttir með tvo ESP32. <br>
> [Callback Methods](https://docs.micropython.org/en/latest/library/espnow.html#callback-methods)

---

### 3. ESP32 sem vefþjónn. (30%)  

Athugaðu að í áfanganum notum við okkar eigið þráðlausa net með þessum upplýsingum:
```python
     SSID = "TskoliVESM"
     LYKILORD = "Fallegurhestur"
```

#### ESP32-S3 WROOM hefur 3 mismunandi WiFi e. operating modes: 
- station mode
- AP mode 
- AP + station mode.

#### Station mode
Hagar sé sem WiFi client, á samskipti við önnur tæki sem eru tengd router via [WiFi](https://docs.micropython.org/en/latest/esp32/quickref.html#wlan) nettengingu. Sjá nánar `28.1 Station mode ` í [kafla 28](https://github.com/VESM3/IOT/blob/main/Efni/Python_Tutorial_framleidandi.pdf) og [WLAN class](https://docs.micropython.org/en/latest/library/network.WLAN.html).

 - Ýttu á reset á ESP32 til að fá IP töluna.

#### AP mode
ESP32-S3 er notað sem hotspot. Það býr til hotspot netkerfi aðskildu frá internetinu.
Sjá nánar `28.2 AP mode` í [kafla 28](https://github.com/VESM3/IOT/blob/main/Efni/Python_Tutorial_framleidandi.pdf).

- breyttu AP heiti (ssidAP) svo það verða ekki krosstengingar á milli ESP32 tækja.
- síminn þinn eða tölva þarf að vera á sama wifi og ESP32.

#### AP + Station mode
ESP32 getur notað AP mode og Station mode samtímis. Önnur WiFi tæki geta valið að tengjast ESP32 með router eða hotspot. Sjá nánar `28.3 AP + Station mode ` í [kafla 28](https://github.com/VESM3/IOT/blob/main/Efni/Python_Tutorial_framleidandi.pdf)


#### Verkefnið:

1. Búðu til einfaldan ESP32 vefþjón í `AP mode` sem hýsir vefsíðu þar sem hægt er að kveikja og slökkva á Led á ESP32 með snjallsíma. Notaðu [Microdot](https://microdot.readthedocs.io/en/latest/). Sjá nánar [How to create a MicroPython Web Server the easy way!](https://www.donskytech.com/how-to-create-a-micropython-web-server-the-easy-way/).
1. Tengdlu DHT11 við ESP32 (micropython) og láttu hann vera vefþjón í `Station mode` sem hýsir vefsíðu og sýnir raka- og hitagildi frá dht11 skynjaranum. Láttu vefsíðuna endurræsa sig á 5 sekúndna fresti (auto page refresh) með setInterval() í JavaScript, [sýnidæmi](https://lastminuteengineers.com/esp32-dht11-dht22-web-server-tutorial/).

<!--
- [Create A Simple ESP32 Web Server (C++)](https://lastminuteengineers.com/creating-esp32-web-server-arduino-ide/)
-->

---

### 4. Ljósstýring (30%) 

1. Settu upp tvo birtumæla (LDR) með sitthvorn ESP32 sem sendir gögn frá sér á 5 sekúndna fresti með ESP-NOW til þriðja ESP32inn sem birtir gildin á tölvuskjá. 
1. Settu upp þriðja ESP32inn sem vefþjón (tengdur tilbúnu Wifi) sem birtir gildin á vefsíðu.
1. Notandi á að geta kveikt og slökkt á LED hjá völdum ESP32 (birtumæli) með takka í vefappi. 

> [ESPNow and Wifi Operation](https://docs.micropython.org/en/latest/library/espnow.html#espnow-and-wifi-operation) <br>
> [Integrating ESP-NOW with MicroPython and WiFi](https://www.donskytech.com/esp-now-micropython-wifi-mqtt/)

<!-- [espnow-wifi-mqtt](https://www.donskytech.com/category/micropython/) -->

<!--
C++
- ESP32 getur haft Access point (AP) og station (STA) samtímis. þessi stilling (dual mode) kallast `WIFI_AP_STA` sjá [sýnidæmi](https://linuxhint.com/esp32-both-access-station-points/#:~:text=The%20above%20two%20modes%20access,network%20to%20which%20ESP32%20connects). 
- [Communication between two ESP32 via WiFi](https://www.aranacorp.com/en/communication-between-two-esp32-via-wifi/)
-->


<!--
### 5. Sleepmode (10%) _Vantar að laga að micropython_
**sleep mode hefur áhrif á wifi** sjá: [ESPNOW og wifi](https://docs.micropython.org/en/latest/library/espnow.html#espnow-and-wifi-operation)

Ef þú ætlar að nota t.d. batterí með ESP32 þá skiptir hvert mA máli. Settu ESP32 í deep sleep mode, en láttu ESP32 vakna á 5 sekúndna fresti til að kveikja á eða slökkva á LED til skiptis, haltu einnig utan um fjölda skipta sem kveikt er á LED með teljara og birtu í Serial Monitor. Settu svo ESP32 aftur í deep sleep.

- [Insight Into ESP32 Sleep Modes & Their Power Consumption](https://lastminuteengineers.com/esp32-sleep-modes-power-consumption/)
- [ESP32 Deep Sleep & Its Wake-up Sources](https://lastminuteengineers.com/esp32-deep-sleep-wakeup-sources/)

> _Ítarefni - Interrupts:_ [Arduino Interrupts Tutorial](https://roboticsbackend.com/arduino-interrupts/) og [Configuring & Handling ESP32 GPIO Interrupts In Arduino IDE](https://lastminuteengineers.com/handling-esp32-gpio-interrupts-tutorial/) 
-->

---

### Námsmat og skil

- Skilaðu á Innu kóðalausnum.
- Yfirferð á sér stað í tíma. Einkunn fyrir hvern lið: 
    - 4/4 lausn er vel útfærð.
    - 3/4 lausn er smávægilega ábótavant (vantar smá upp á).
    - 2/4 lausn er ábótavant, helmingur er vel útfærður.
    - 1/4 lausn er stórlega ábótavant, en tíma- og kóðavinna lögð í lausn.
    - 0/4 lausn vantar eða óunnin.

---
