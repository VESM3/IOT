## Tímaverkefni 3 (9%) 

- Samskiptastaðlar; SPI og I2C
- RFID og OLED

---

### 3.1 SPI og RFID (20%)

1. Kynntu þér hvernig SPI virkar með að horfa á [myndband](https://www.youtube.com/watch?v=ldRkXTBw9_o) og lesa [BASICS OF THE SPI COMMUNICATION PROTOCOL](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol). 
1. Kynntu þér RFID, [Interface RC522 RFID Module with Arduino](https://lastminuteengineers.com/how-rfid-works-rc522-arduino-tutorial/). 
1. RaspberryPi Zero er með þrjá SPI controllers, sjá nánar [SPI Documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#spi-overview) 
1. Prófaðu skrif- og lesgagnaðgerðir með RFID sbr. [How to setup a Raspberry Pi RFID RC522 Chip](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
   - Ekki gleyma að stilla RaspberryPi þannig að hann virkar með SPI 
   - notaðu GPIO Zero safnið ekki RPi.GPIO safnið 

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

---

### 3.2 RFID og LEDs (20%)
1. Settu upp á brauðbretti RFID og tvö LEDs sbr eftirfarandi sýnidæmi [RFID reader (Arduino)](https://tutorial45.com/arduino-rfid-project-beginners/) en notaðu RaspberryPi í staðinn fyrir Arduino. 

<!-- sjá [Enabling SPI on the Raspberry Pi](https://pimylifeup.com/raspberry-pi-spi/), ath ekki gera àpt update` -->

---

### 3.3 I2C og OLED (30%)
1. Kynntu þér I2C með að lesa þessa grein [I2C](https://www.circuitbasics.com/basics-of-the-i2c-communication-protocol/). 
1. Lestu [Interface OLED Graphic Display Module with Arduino](https://lastminuteengineers.com/oled-display-arduino-tutorial/).
1. Birtu nafnið þitt á OLED með Raspberry Pi Zero. Sjá t.d. [RPi OLED](https://www.electroniclinic.com/raspberry-pi-oled-display-i2c-ssd1306-display-module-interfacing-and-programming/)
1. Birtu mynd.  

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

### 3.4 Skráningar- eða öryggiskerfi  (30%)

Búið til tveir nemendur saman öryggikerfi eða skráningarkerfi:

1. [öryggishurðakerfi](https://create.arduino.cc/projecthub/wesee/toggle-led-with-nfc-tag-and-pin-57f894?ref=tag&ref_id=nfc&offset=0) með RFID/NFC, OLED og Keypad.
1. Skráningarkerfi sem heldur um nemendamætingar. sýnidæmi [Build your own Raspberry Pi RFID Attendance System](https://pimylifeup.com/raspberry-pi-rfid-attendance-system/) og [Attendance System Using Raspberry Pi and NFC Tag Reader](https://www.instructables.com/id/Attendance-system-using-Raspberry-Pi-and-NFC-Tag-r/). Notið RFID/NFC og OLED, notaðu gagnageymslu að eigin vali (dictioary, skrá, JSON, SQL).

---

### Námsmat
- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu öllum kóðalausnum.

<!--
- [Make your own NFC data cufflinks](https://www.raspberrypi.org/blog/make-your-own-nfc-data-cufflinks/) 
-  Using Serial Peripheral Interface (SPI) in Raspberry Pi: https://iot-guider.com/raspberrypi/using-spi-in-raspberry-pi/
- [LED Matrix með SPI](https://core-electronics.com.au/tutorials/i-spi-with-raspberry-pi.html)

### RFID og IOTA (wallet)
- [RPi with RFID RC522 Reader and record data on IOTA](https://medium.com/coinmonks/for-beginners-how-to-set-up-a-raspberry-pi-rfid-rc522-reader-and-record-data-on-iota-865f67843a2d)
- [IOTA](https://www.iota.org/get-started/what-is-iota)
-->

   
