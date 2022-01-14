# Tímaverkefni 4 (9%) 

- M2M samskipti

Machine to machine [(M2M)](https://en.wikipedia.org/wiki/Machine_to_machine) is direct communication between devices using any communications channel, including wired and wireless. M2M derives from telemetry technology and generally refers to data exchange between various devices (usually) through the Internet without human participation. See also [IoT vs M2M](https://www.avsystem.com/blog/iot-and-m2m-what-is-the-difference/)

---

### 4.1 Remote GPIO með RPi. (20%)
Að stýra RPi + GPIO yfir netið frá tölvu. 

1. Lestu vel yfir og gerðu viðeigandi stillingar skv. [Configuring Remote GPIO](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html#configuring-remote-gpio) þannig að þú getur stýrt RPi frá tölvunni þinni, notaðu VSCode.  
1. Láttu LED blikka með eftifarandi kóða [4.4. Pin factories](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html#pin-factories)

---

### 4.2 Remote GPIO. (20%)

- Tveir saman.
1. Framkvæmið [tilraun 5.1](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#led-button) með tveimur RPI.
<!--
1. Framkvæmið [tilraun 5.2](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#led-2-buttons) með þrjá RPi og tölvu.
1. Framkvæmið [tilraun 5.4](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#multi-room-doorbell) með tvo RPI og tölvu.
-->

---

### 4.3 ESP32 WROOM DevKitC v4 með Arduino IDE. (20%)  

1. Lestu þig til um ESP32, [Insight Into ESP32 Features & Using It With Arduino IDE](https://lastminuteengineers.com/esp32-arduino-ide-tutorial/)
1. Svo þú getir notað ESP32 með Arduino IDE þá er einfaldasta leiðin að installa með [board manager](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html#installing-using-boards-manager) að **Windows**. 
   - Install leiðbeiningar fyrir Mac tölvur: [Guide](https://www.hackster.io/shahizat005/getting-started-with-esp32-on-a-mac-4b3997#toc-installing-esp32-add-on-in-arduino-ide-4) og [driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
1. Veldu **ESP32 DEV Module** í Tools -> Board í Arduino IDE Láttu [LED blikka með ESP32](https://docs.espressif.com/projects/arduino-esp32/en/latest/tutorials/blink.html) 
   - Þetta er rétt [pinout](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/_images/esp32-devkitC-v4-pinout.png).
   - pinni sem er númeraðu 2 er sama og GPIO2 (ekki nota D2)
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

### 4.4 ESP32 sem vefþjónn. (20%)
1. Fylgdu eftir báðum tilraununum í [Create A Simple ESP32 Web Server In Arduino IDE](https://lastminuteengineers.com/creating-esp32-web-server-arduino-ide/).

**ath** Það gæti verið nauðsynlegt að breyta ssid **ef** það eru fleiri en tveir að tengjast wifi, sjá t.d. [How to Set an ESP32 Access Point (AP) for Web Server](https://randomnerdtutorials.com/esp32-access-point-ap-web-server/)

---

### 4.5 ESP32 og RPi. (20%)
- einn eða tveir saman

1. Tengdu buzzer við ESP32.
1. Búið til einfalda vefsíðu sem tekur við [HTTP requests](https://www.w3schools.com/tags/ref_httpmethods.asp) sem er hýst á ESP32 vefþjóni (STA mode). 
1. Með takka (eða tveimur) tengdan við RPi á að vera hægt að kveikja og slökkva á buzzernum með notkun GET request yfir netið.


---

## Námsmat
- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu vefslóð kóðalausnir af tilraunum.
