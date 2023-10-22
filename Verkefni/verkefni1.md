
## Tímaverkefni 1 

- Námsmat 15% af heildareinkunn
- Einstaklingsverkefni
- Áætlaður tími: 3 x (4 x 50 mín)
- ESP32-S3, I2C, SPI, OLED, NTP, RFID 

---

#### 1. Uppsetning á umhverfi fyrir ESP32 (10%)
Fylgdu eftir [þessum](https://github.com/VESM2VT/ESP32/blob/main/verkefni/Timaverkefni0.md) leiðbeiningum. 

- [Pinnamynd ESP32-S3](https://github.com/Freenove/Freenove_ESP32_S3_WROOM_Board/blob/main/ESP32S3_Pinout.png)

:warning: ESP32 vinnur á 3.3V en ekki 5V. :warning:

> **Note**
> **Ekki** nota pinna; GPIO0, GPIO3, GPIO19, GPIO20, GPIO45, GPIO46. 

<!-- 
> [ESP32](https://lastminuteengineers.com/getting-started-with-esp32/) (önnur týpa) ásamt [ESP32 Pinout útskýringum](https://lastminuteengineers.com/esp32-pinout-reference/).
> ESP32 notast við 3.3V logic levels fyrir samskipti. Það er ekki hægt að vinna með íhluti sem krefjast 5V logic.
-->

---

#### 2. OLED (20%)

Lestu um [I2C](https://www.circuitbasics.com/basics-of-the-i2c-communication-protocol/) samskipti og kynntu þér [OLED](https://www.donskytech.com/micropython-interfacing-with-ssd1306-oled-display/).

OLED | Pinni
--- | ---
S | GPIO 13 - SDA/SDI (serial data line)
S | GPIO 14 - SCL/SCK (serial clock)
G | GND 
V | Vcc (3.3V)

:warning: Ekki tengja OLED við 5V.

**Verkefnið**:
1. Birtu nafnið þitt.
1. Bættu við teljara sem telur upp í 10 fyrir neðan nafnið þitt.
1. Þegar teljari er kominn upp í 10, þá birtist teikning eða bitmap og nafnið þitt og teljari hverfa af skjá.

> annar [tutorial](https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/)

<!--
 _notar breytur_
- [ssd1306 library](https://pypi.org/project/micropython-ssd1306/) _nýja safnið (vísað í grein)_
- [ssd1306](https://github.com/VESM3/IOT/blob/main/Kodi/ssd1306.py) micropython safnið frá Adafruit. _read only núna_
- [Adafruit_GFX](https://randomnerdtutorials.com/micropython-ssd1306-oled-scroll-shapes-esp32-esp8266/)  Display Scroll Functions and Draw Shapes _**deprecated**_ <br> 
-->

---

#### 3. Að fá dagsetningu og rauntíma frá NTP (Network Time Protocol) vefþjóni með ESP32 (20%)

1. Kynntu þér [hér](https://docs.micropython.org/en/latest/esp32/quickref.html#wlan) hvernig þú getur tengt ESP-inn þinn við þráðlausa netið. Athugaðu að í áfanganum notum við okkar eigið þráðlausa net með þessum upplýsingum:
     ```python
     SSID = "TskoliVESM"
     LYKILORD = "Fallegurhestur"
     ```
     - ⚠️ Að tengjast við WIFI getur tekið örskamma stund. Hafðu smá `sleep` (t.d. 5 sek.) á eftir `connect` línunni í kóðanum hjá þér.
1. Kynntu þér svo NTP og hvernig það er notað í Micropython með því að skoða þessa [grein](https://bhave.sh/micropython-ntp/).
1. Skoðaðu einnig hvernig unnið er með tíma (leggja saman, draga frá o.fl) í micropython með því að skoða [þetta](https://docs.micropython.org/en/latest/library/time.html). Micropython inniheldur ekki `datetime` klasasafnið.

**Verkefnið**
1. Tengdu ESP-inn við internetið, sæktu réttan tíma með NTP
2. Birtu á OLED skjánum klukkuna (ath. bara klukkuna (kk:mm:ss), ekki dagsetninguna) og láttu hana uppfærast einu sinni á sekúndu.

Aðstoð:
 - Skoðaðu [Timers](https://docs.micropython.org/en/latest/esp32/quickref.html#timers) í Micropython til að uppfæra klukkuna á ákveðnum fresti.
 - Ef þú færð villuna `OSError: [Errno 116] ETIMEDOUT` eða `OSError: [Errno 118] EHOSTUNREACH` hinkraðu þá í smá stund og prófaðu svo aftur.
 - [A Beginner’s Guide to the Python time Module](https://realpython.com/python-time-module/)
 
<!-- 
Birtu tíma og dagsetningu ( dagur, mánuður, ár ) í Serial Monitor miðað við Ísland, sjá [Getting Time From NTP Server With ESP32](https://lastminuteengineers.com/esp32-ntp-server-date-time-tutorial/).

```C++
   ssid     = "TskoliVESM";           
   password = "Fallegurhestur";
```
-->
> Notaðu hotspot í síma ef skólanet virkar ekki.

---

#### 4. RFID (20%)

Kynntu þér SPI samskipti með því að lesa þessa [grein](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol) og/eða horfa á þetta [myndband](https://www.youtube.com/watch?v=ldRkXTBw9_o) og lestu þér til um [RC522 RFID](https://lastminuteengineers.com/how-rfid-works-rc522-arduino-tutorial/). 

1. Tengdu svo RC522 RFID við ESP32-S3 á brauðbretti samkvæmt þessari [mynd](https://raw.githubusercontent.com/VESM3/IOT/main/Myndir/verkefni_1_3_rfid_tenging.png): 
1. Settu svo inn eftirfarandi kóða (þú finnur mfrc522 klasasafnið [hér](https://github.com/cefn/micropython-mfrc522/blob/master/mfrc522.py)):
     ```python
     from mfrc522 import MFRC522
     from machine import Pin, SoftSPI

     sck = Pin(3) 
     mosi = Pin(7)
     miso = Pin(5) # algeng önnur nöfn: SCL og TX
     rst = 4
     nss = 9 # algeng önnur nöfn: SS, SDA, CS og RX

     # Búa til og virkja SPI tenginguna
     spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
     spi.init()

     # Búa til tilvik af RFID lesarann og tengjast honum með SPI
     rfid_lesari = MFRC522(spi=spi, gpioRst=rst, gpioCs=nss)

     print("Skannaðu kort!")

     while True:
          (stada, korta_tegund) = rfid_lesari.request(rfid_lesari.REQIDL)
          if stada == rfid_lesari.OK: # ef eitthvað er til að lesa
               (stada, kortastrengur) = rfid_lesari.anticoll()
               if stada == rfid_lesari.OK:
                    # kortanúmerið er í bytearray og því gott að 
                    # breyta því í heiltölu áður en unnið er með það
                    kortanumer = int.from_bytes(kortastrengur, "big")
                    print(kortanumer)
     ```

1. ESP-inn þinn er með **eina** innbyggða NeoPixel ljósadíóðu á **pinna 48**. Skoðaðu [hér](https://docs.micropython.org/en/latest/esp32/quickref.html#neopixel-and-apa106-driver) hvernig þú getur notað hana.

**Verkefnið**
1. Lestu svo *id*-ið af tveimur kortum og bættu númerunum á þeim í kóðann hér að ofan (t.d. í lista).
1. Breyttu nú forritun hér að ofan þannig að þegar þekkt kort (er í listanum í fyrri liðnum) er lesið kemur grænt ljós á NeoPixel díóðuna en ef kortið er ekki þekkt kemur rautt ljós. Ljósin eiga loga í eina sekúndu (má gera með sleep).

<!-- 

Finndu út ID á RFID tagi, sjá [víratengingar og kóða](https://esp32io.com/tutorials/esp32-rfid-nfc). 
1. Tengdu tvö LEDS (rautt og grænt) og RFID tags með RC522 til að auðkenna notanda, sjá [myndband](https://youtu.be/GX_4IAHJzBE) og [kóðadæmi](https://github.com/VESM3/IOT/blob/main/Kodi/RFID_audkenning.ino).

:warning:  Tengdu VCC í 3.3V (ekki 5V) annars skemmur þú RFID

RFID | ESP32
--- | ---
SS | GPIO 5
SCK | GPIO 18
MOSI | GPIO 23
MISO | GPIO 19
IRQ | 
GND | GND
RST | GPIO 27
VCC | **3.3V**
-->

> Nánar um [RFID og NFC](https://github.com/VESM3/IOT/wiki/RFID-og-NFC) <br>

<!--
Skrifaðu nafnið þitt á RFID tag með RC522 RFID. Notaðu lesaðgerð og birtu nafnið í Serial monitor.
fjarlægðu eftirfarandi kóða í les/skrif aðgerðum: `Serial.println(mfrc522.GetStatusCodeName(status));`
-->

---

#### 5. Tímaskráningarkerfi  (30%)

Tímaskráningarkerfið á að virka þannig að þegar starfsmaður mætir til vinnu þá ber hann kort upp að RFID skynjaranum. Á OLED skjánum á þá að birtast "Góðan daginn [nafn starfsmanns]" og NeoPixel-inn sýnir grænt ljós. Ef kortið er ekki þekkt á að birtast "Óþekktur stafsmaður" á OLED skjánum og rautt ljós á NeoPixel-num. Þegar starfsmaður yfirgefur svo svæðið ber hann kortið aftur að RFID skynjaranum og þá á að birtast "Bless [nafn starfsmanns], vinnutími: [klst:mínútur:sekúndur]." (sem er tíminn sem liðinn er frá því að hann skráði sig inn) og NeoPixel sýnir blátt ljós. Þegar ekki er verið að nota lesarann á að loga hvítt ljós á NeoPixel og OLED skjárinn á að sýna "Skannaðu kort!" ásamt klukkunni.

1. Settu upp verklega með ESP32 og brauðbretti; OLED, RFID. 
1. Notaðu NTP til að tryggja rétta klukku. 
2. Haltu utan um RFID, nafn og innskráningartíma starfsmanns t.d. með `dictonary`.

<!--

1. notaðu `id` af RFID tag fyrir auðkenningu. Þegar notandi skráir sig inn þá verður tímaskráning, nafn birtist á OLED og grænt LED logar. Þegar notandi skráir sig út þá á að birtast á OLED nafn og viðverutíminn ( frá innskráningu ) og rautt LED logar. 
 

Demo:
- [Toggle LED with NFC Tag and PIN](https://www.hackster.io/wesee/toggle-led-with-nfc-tag-and-pin-57f894)
- [Build your own Raspberry Pi RFID Attendance System](https://pimylifeup.com/raspberry-pi-rfid-attendance-system/)
- [Attendance System Using Raspberry Pi and NFC Tag Reader](https://www.instructables.com/id/Attendance-system-using-Raspberry-Pi-and-NFC-Tag-r/).
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


