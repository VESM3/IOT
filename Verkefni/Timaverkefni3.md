## Tímaverkefni 3 (9%) 

- Einstaklingsverkefni
- Samskiptastaðlar; SPI og I2C
- RFID og NFC 

---

### 3.1 SPI og RFID (20%)

1. Kynntu þér hvernig SPI virkar með að horfa á [myndband](https://www.youtube.com/watch?v=ldRkXTBw9_o) og lesa [BASICS OF THE SPI COMMUNICATION PROTOCOL](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol). 
1. Kynntu þér RFID og sett upp verklega með **Arduino** kóðadæmin í [Interface RC522 RFID Module with Arduino](https://lastminuteengineers.com/how-rfid-works-rc522-arduino-tutorial/). 
   - Notaðu Serial Monitor í staðinn fyrir 16×2 character LCDs.

---

### 3.2 RFID og RaspberryPi (20%)
RaspberryPi Zero er með þrjá SPI controllers, sjá nánar [SPI Documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#spi-overview) 

1. Prófaðu skrif- og lesgagnaðgerðir með RFID sbr. [How to setup a Raspberry Pi RFID RC522 Chip](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
   - Ekki gleyma að stilla RaspberryPi þannig að hann virkar með SPI 
   - notað er RPi.GPIO safnið

#### RC522 pinnar (með T-cobbler)
RC522 | Pinni
--- | ---
SDA | CEO
SCK | SCLK
MOSI | MOSI 
MISO | MISO 
GND | GND
RST | #25
3.3v | 3.3v

---

### 3.3 RFID og LEDs (20%)
1. Settu upp á brauðbretti RFID og tvö LEDs sbr eftirfarandi sýnidæmi [RFID reader (Arduino)](https://tutorial45.com/arduino-rfid-project-beginners/) en notaðu RaspberryPi í staðinn fyrir Arduino. 

<!-- sjá [Enabling SPI on the Raspberry Pi](https://pimylifeup.com/raspberry-pi-spi/), ath ekki gera àpt update` -->

---

### 3.4 I2C og OLED (20%)
1. Kynntu þér I2C með að lesa þessa grein [I2C](https://www.circuitbasics.com/basics-of-the-i2c-communication-protocol/). <br>
1. Lestu [Interface OLED Graphic Display Module with Arduino](https://lastminuteengineers.com/oled-display-arduino-tutorial/) og settu upp verklega.
   1. Birtu nafnið þitt á skjá.
   1. Birtu mynd af þér. 
1. Birtu textann Hrekkjavaka! á OLED með Raspberry Pi Zero.

---

### 3.5 Skráningarkerfi (kladdi) (20%)

- tveir nemendur saman

Búið til skráningarkerfi sem heldur um nemendamætingar í kennslustund. Notið Raspberry Zero, RFID/NFC og OLED, notaðu gagnageymslu að eigin vali (skrá, JSON, SQL), sýnidæmi [Build your own Raspberry Pi RFID Attendance System](https://pimylifeup.com/raspberry-pi-rfid-attendance-system/) og [Attendance System Using Raspberry Pi and NFC Tag Reader](https://www.instructables.com/id/Attendance-system-using-Raspberry-Pi-and-NFC-Tag-r/)
  
  
<!-- 
---

### Interrupts 
1. Kynntu þér hvernig interrupts virkar og svaraðu eftirfarandi hugleiðingum:
   1. Hvernig notar þú interrupts?
   1. Hvenær er heppilegt að nota interrupts?
   1. Hvað eru volatile breytur?
1. Settu upp verklega kóða sem notar takka og led með notkun interrupts.
1. Prófaðu að nota IRQ pinnann þ.e. interrupt til að spara orkugjafa (batterí).

**Bjargir:**
- [Myndband; Arduino Interrupts](https://www.youtube.com/watch?v=QtyOiTw0oQc) 
- [Vefgrein: Interrupt Service Routines (ISR)](http://gammon.com.au/interrupts)
- [attachinterrupt()](https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/)
- Adafruit - Multi-tasking the Arduino (notar class); [Part 1: millis](https://learn.adafruit.com/multi-tasking-the-arduino-part-1) og [Part 2: interrupts](https://learn.adafruit.com/multi-tasking-the-arduino-part-2/overview)

-->

<!--

---

### SPI verkefni:
-  Using Serial Peripheral Interface (SPI) in Raspberry Pi: https://iot-guider.com/raspberrypi/using-spi-in-raspberry-pi/
- [LED Matrix með SPI](https://core-electronics.com.au/tutorials/i-spi-with-raspberry-pi.html)

### NFC 
- [Make your own NFC data cufflinks](https://www.raspberrypi.org/blog/make-your-own-nfc-data-cufflinks/) 
- [Arduino nfc verkefni](https://create.arduino.cc/projecthub/wesee/toggle-led-with-nfc-tag-and-pin-57f894?ref=tag&ref_id=nfc&offset=0)

### RFID og IOTA (wallet)
- [RPi with RFID RC522 Reader and record data on IOTA](https://medium.com/coinmonks/for-beginners-how-to-set-up-a-raspberry-pi-rfid-rc522-reader-and-record-data-on-iota-865f67843a2d)
- [IOTA](https://www.iota.org/get-started/what-is-iota)
  
-->

---

### Námsmat
- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu öllum kóðalausnum.



   
