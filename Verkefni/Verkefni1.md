## Tímaverkefni 1 

- 15% af heildareinkunn.
- Áætlaður tími: 8 klst
- Raspberry Pi, GPIO, RFID og OLED

---
<!--
#### 1. Að tengjast Raspberry Pi með SSH
1. Settu SD minniskortið (frá kennara) í RaspberryPi og tengdu við rafmagn (usb power port).
1. Í fartölvunni þinni skrifaðu eftirfarandi í GitBash. (Ef **Mac/Linux** þá `terminal`, þú gætir þurft að nota `sudo`)
      ```Linux
      ssh pi@hostname.tskoli.is   // hostname er mismunandi milli nemanda. 
      password: raspberry         // rétt lykilorð færðu frá kennara.
      ```  
---
-->

#### 1. Thonny ritill. (5%)
Notaðu [Thonny](https://thonny.org/) ritil á RPi OS. Búðu til python skrá og prentaðu út strenginn með nafninu þínu, sjá nánar [Get Started with Thonny IDE on Raspberry Pi OS](https://roboticsbackend.com/thonny-ide-raspberry-pi-os/).

---

#### 2. Nano ritill í terminal. (5%)
Notaðu terminal og Linux skipanir til að skoða þig um í RPi stýrikerfinu. Búðu til python skrá og notaðu [nano](https://www.nano-editor.org/) command-line ritil í terminal til að skrifa python kóða sem innheldur prentskipun með nafninu þínu. Keyrðu svo python skránna í terminal. sjá [Raspberry Pi – Run Python Script in the Terminal](https://roboticsbackend.com/raspberry-pi-run-python-script-in-the-terminal/).


---

#### 3. GPIO: Blikkandi ljós. (5%)
Láttu LED blikka á brauðbretti með python kóða. Notaðu [T-Coppler](https://www.adafruit.com/product/2028) með brauðbrettinu og [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/) python safnið með kóðalausn. Nýttu þér kóðalausnir í [Basic Recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html). Hér er [GPIO Zero pinout](https://gpiozero.readthedocs.io/en/stable/cli_tools.html#pinout) þegar þú notar ekki T-Coppler.

---

#### 4. GPIO: Blikkandi LED með fade. (5%)
Láttu LED _fade_ inn og út.

---

#### 5. GPIO: Takki og LED. (10%)
Við að ýta á takka þá kemur birta af LED. 

---

#### 6. GPIO (10%)

Veldu þér tutorial til að fylgja úr [Basic Recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html)

<!-- Þurfa verkefni án tutorial -->

---


#### 7. SPI og RFID (10%)

1. Kynntu þér hvernig SPI virkar með að horfa á [myndband](https://www.youtube.com/watch?v=ldRkXTBw9_o) og lesa [BASICS OF THE SPI COMMUNICATION PROTOCOL](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol). 
1. Kynntu þér RFID, [Interface RC522 RFID Module with Arduino](https://lastminuteengineers.com/how-rfid-works-rc522-arduino-tutorial/). _Ath. Við ætlum að nota RPi í þessu verkefni, ekki Arduino._
1. RaspberryPi er með þrjá SPI controllers, sjá nánar [SPI Documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#spi-overview) 
1. Prófaðu skrif- og lesgagnaðgerðir með RFID sbr. [How to setup a Raspberry Pi RFID RC522 Chip](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
   - Ekki gleyma að stilla RaspberryPi þannig að hann virkar með SPI 
   - notaðu GPIO.Zero eða [RPi.GPIO](https://pypi.org/project/RPi.GPIO/) safnið 

#### RC522 pinnar (með T-cobbler)
RC522 | Pinni
--- | ---
SDA | CE0
SCK | SCLK
MOSI | MOSI 
MISO | MISO 
GND | GND
RST | #25
3.3v | 3.3v

Nánar um [RFID og NFC](https://github.com/VESM3/IOT/wiki/RFID-og-NFC)

---

#### 8. RFID og LEDs (15%)
Settu upp á brauðbretti RFID og tvö LEDs sbr eftirfarandi sýnidæmi [RFID reader (Arduino)](https://tutorial45.com/arduino-rfid-project-beginners/) en notaðu RaspberryPi í staðinn fyrir Arduino. 

<!-- sjá [Enabling SPI on the Raspberry Pi](https://pimylifeup.com/raspberry-pi-spi/), ath ekki gera àpt update` -->

---

#### 9. I2C og OLED (15%)
1. Kynntu þér I2C með að lesa þessa grein [I2C](https://www.circuitbasics.com/basics-of-the-i2c-communication-protocol/). 
1. Lestu [Interface OLED Graphic Display Module with Arduino](https://lastminuteengineers.com/oled-display-arduino-tutorial/).
1. Birtu nafnið þitt á OLED með Raspberry Pi Zero. Sjá t.d. [RPi OLED](https://www.electroniclinic.com/raspberry-pi-oled-display-i2c-ssd1306-display-module-interfacing-and-programming/) 

OLED | Pinni
--- | ---
S | SDA
S | SCL
G | GND 
V | Vcc 

<!--
OLED með ESP32 https://github.com/adafruit/Adafruit_SSD1306
-->

---

#### 10. Auðkennis innskráningarkerfi  (20%)
**Einn eða tveir nemendur saman**. <br>
1. Setjið saman með OLED, RFID og gagnageymslu (listi, dictionary eða skrá) fyrir auðkennis innskráningarkerfi. 
1. Notaðu id af RFID tags fyrir samanburð.
1. Birtu nafn eða icon á OLED. 

Bjargir:
- [öryggishurðakerfi](https://create.arduino.cc/projecthub/wesee/toggle-led-with-nfc-tag-and-pin-57f894?ref=tag&ref_id=nfc&offset=0).
- [Build your own Raspberry Pi RFID Attendance System](https://pimylifeup.com/raspberry-pi-rfid-attendance-system/)
- [Attendance System Using Raspberry Pi and NFC Tag Reader](https://www.instructables.com/id/Attendance-system-using-Raspberry-Pi-and-NFC-Tag-r/). 

---

#### 11. Uppsetning á RPi stýrikerfi 

heimaverkefni

Settu upp RPi stýrikerfi á SD minniskortið þitt og stilltu RPi Zero skv. [leiðbeiningum](https://github.com/VESM3/IOT/blob/main/Efni/RPiuppsetning.md) þannig að þú getur tengst wifi bæði heima og í skóla.

---


### Námsmat og skil

- Yfirferð á sér stað í tíma. 
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnum.


