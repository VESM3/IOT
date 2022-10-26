# Tímaverkefni 2

- Námsmat 15% af heildareinkunn
- ESP32

---


### 1 ESP32 WROOM DevKitC v4 með Arduino IDE. (20%)  

1. Lestu þig til um [ESP32 with Arduino IDE](https://lastminuteengineers.com/esp32-arduino-ide-tutorial/) og [rétta pinout](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/_images/esp32-devkitC-v4-pinout.png).
1. Svo þú getir notað ESP32 með Arduino IDE þá er einfaldasta leiðin að installa með [board manager](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html#installing-using-boards-manager) að **Windows**. 
   - Install leiðbeiningar fyrir Mac tölvur: [Guide](https://www.hackster.io/shahizat005/getting-started-with-esp32-on-a-mac-4b3997#toc-installing-esp32-add-on-in-arduino-ide-4) og [driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
1. Veldu **ESP32 DEV Module** í Tools -> Board í Arduino IDE Láttu [LED blikka með ESP32](https://docs.espressif.com/projects/arduino-esp32/en/latest/tutorials/blink.html) 
   - pinni sem er númeraðu 2 er sama og GPIO2 (ekki D2)
   - svarta snúran er eingöngu power snúra. Notaðu blá USB mircro data kapalsnúru 
   - þú gætir þurft að breyta upload speed í 115200

#### Athugaðu:

- ESP32 notast við 3.3V logic levels fyrir samskipti 
- GPIO pinnarnir þola ekki 5V, það er ekki hægt að vinna með íhluti sem krefjast 5V logic.
<!-- - [usb driver fyrir Mac tölvu](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) -->

<!--
- [ESP32-DevKitC V4 Getting Started Guide](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/hw-reference/esp32/get-started-devkitc.html#esp32-devkitc-v4-getting-started-guide)
- [ESP32 WROOM DevKitC v4 on Arduino IDE](https://www.iottechtrends.com/getting-started-with-esp32-wroom-devkitc/)
- [IOT Made Simple: Playing With the ESP32 on Arduino IDE](https://www.instructables.com/IOT-Made-Simple-Playing-With-the-ESP32-on-Arduino-/)
-->

---

### 2. ESP32 sem vefþjónn. (20%)
1. Fylgdu eftir báðum tilraununum í [Create A Simple ESP32 Web Server In Arduino IDE](https://lastminuteengineers.com/creating-esp32-web-server-arduino-ide/).

<!--
**Kennari: Skoða** Það gæti verið nauðsynlegt að breyta ssid **ef** það eru fleiri en tveir að tengjast wifi, sjá t.d. [How to Set an ESP32 Access Point (AP) for Web Server](https://randomnerdtutorials.com/esp32-access-point-ap-web-server/)
-->

---

### 3. DHT11/DHT22 með ESP32 (20%)

- [Interface DHT11/DHT22 with ESP32 & Display Values Using Web Server](https://lastminuteengineers.com/esp32-dht11-dht22-web-server-tutorial/)

---

### 4. Pottaplanta með ESP32 (20%)
Verkefnið er að mæla þarfir pottaplöntu með notkun tvo skynjara og svo vefsíðu til að birta mælingarnar. 
Við notum [jarðvegsmælir](https://github.com/VESM3/IOT/blob/main/Efni/soilsensor.md) til að kanna rakastig jarðveg svo við getum áttað okkur hvenær við þurfum að vökva plöntuna og ljósnema [BH1750](https://www.arduino.cc/reference/en/libraries/bh1750/) til að kanna birtuþörf plöntunar. 

Bjargir
- [Interface Multiple DS18B20s with ESP32 & Display Values Using Web Server](https://lastminuteengineers.com/multiple-ds18b20-esp32-web-server-tutorial/)
- [Create A Simple ESP32 Weather Station With BME280](https://lastminuteengineers.com/bme280-esp32-weather-station/)
- [BH1750 sýnidæmi](https://github.com/claws/BH1750#example) 
   - SDA (SDI) = GPIO21
   - SCL (SCK) = GPIO22 
---


### 5. Getting Date & Time From NTP Server With ESP3 (20%)
Birtu dagsetningu og tíma með íslensku sniði. Sjá tutorial, [Getting Time From NTP Server With ESP32](https://lastminuteengineers.com/esp32-ntp-server-date-time-tutorial/)

<!--  
- [Interface OLED with ESP32](https://lastminuteengineers.com/oled-display-esp32-tutorial/) 
-->

---

## Námsmat
- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu vefslóð kóðalausnir af tilraunum.
