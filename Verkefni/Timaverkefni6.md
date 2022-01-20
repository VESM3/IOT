# Tímaverkefni 6 (14%)

- Einstaklingsverkefni
- Adafruit IO (IoT cloud platform)

---

### 6.1 Adafruit IO umhverfið (10%)
1. AdafruitIO+ aðgangur
   - Náðu í Adarfuit IO+ aðgang (1 ár frítt) hjá [Github Student Pack](https://education.github.com/pack) og tengdu saman Github og Adafruit reikning.
   - Skráðu þig inn hjá [Adafruit IO](https://io.adafruit.com/). Í Adafruit reikningnum skaltu velja `services`, `view discount` (þar er kóðaruna fyrir Adafruit IO).
   - Veldu Profile og veldu `Upgrade to IO+` sem er neðst á síðunni og smelltu svo á hnappinn `Redeem a Coupon or Pass` linkinn neðarlega, hægra megin og settu inn rununa til að fá 1 ár frítt. (Ath. það þarf aldrei að gefa upp kredikortaupplýsingar).
1. Skoðaðu [Welcome to Adafruit IO](https://learn.adafruit.com/welcome-to-adafruit-io) , skoðaðu sérstaklega [Feeds](https://learn.adafruit.com/adafruit-io-basics-feeds) og [Dashboards](https://learn.adafruit.com/adafruit-io-basics-dashboards). Hér eru líka [myndbönd](https://learn.adafruit.com/all-the-internet-of-things-episode-four-adafruit-io/how-adafruit-io-works).
1. Fylgdu tilraun í myndbandinu [Connecting the Raspberry Pi to Adafruit IO cloud](https://www.youtube.com/watch?v=IfzpoFGkmns)

#### Adafruit söfn og APIs:
   - [Adafruit IO Python safn](https://adafruit-io-python-client.readthedocs.io/en/latest/quickstart.html)  
   - [Adafruit IO MQTT API](https://io.adafruit.com/api/docs/mqtt.html#adafruit-io-mqtt-api)
   - [Adafruit IO HTTP API](https://io.adafruit.com/api/docs/#adafruit-io-http-api)
 
<!-- 
- [Python kóði með tutorials](https://github.com/adafruit/Adafruit_IO_Python/tree/master/examples/basics).
- AdafruitIO [forum](https://forums.adafruit.com/viewforum.php?f=56) og [discord](https://discord.com/invite/adafruit) 
-->

---

### 6.2 Digital Input (15%)
Sendu stöðu hnapps á/af (í rauntíma) sem er tengdur við Raspberry Pi til Adafruit IO. <br>
Skoðaðu niðurstöður með **Gauge block** í Dashboard. <br>

Sjá til viðmiðunar: [Digital Input (Python)](https://learn.adafruit.com/adafruit-io-basics-digital-input). 

- Notaðu GPi.Zero safnið í staðinn fyrir `adafruit_blinka`. 
- Notaðu REST API 

---

### 6.3 Digital Output (15%)
Tengdu eina LED í brauðbretti með viðnámi tengt við RaspberryPi. <br>
Kveiktu og slökktu á LED með **toogle** hnapp í Dashboard í Adafruit IO. <br>

Sjá til viðmiðunar: [Digital Output (Python)](https://learn.adafruit.com/adafruit-io-basics-digital-output). 

- Notaðu GPi.Zero safnið í staðinn fyrir `adafruit_blinka`. 
- Notaðu REST API 

---

### 6.4 Analog Input (20%) 
Tengdu LDR ljósviðnám (tengdu í 3.3v) í brauðbretti tengt við **ESP32**. Sendu mælingar (analog gildi) frá ljósviðnámi til Adafruit IO <br>
Birtu rauntímaniðurstöður með _Gauge block_ og línuriti í Dashboard, [sýnidæmi](https://cdn-learn.adafruit.com/assets/assets/000/039/356/large1024mp4/light_analog.mp4?1487262232) <br>

Til að geta notað ESP32 með AdafruitIO þá þarf að installa:
- [Adafruit IO Arduino (ESP32) safn](https://github.com/adafruit/Adafruit_IO_Arduino)
- [Arduino Http Client](https://github.com/arduino-libraries/ArduinoHttpClient)
- [Arduino MQTT Client](https://github.com/adafruit/Adafruit_MQTT_Library)

Sjá til viðmiðunar: 
- [ESP32: Adafruit IO example 8, analog in](https://github.com/adafruit/Adafruit_IO_Arduino/tree/master/examples)
   - stilltu wifi stillingar í config.h 
- [ESP32 ADC – Read Analog Values](https://randomnerdtutorials.com/esp32-adc-analog-read-arduino-ide/)

---

### 6.5 Analog Output (20%) 
Notaðu **Slider block** í **Dashbord** með Adafruit IO til að stýra birtustig á LED sem er tengd við PWM pinna á ESP32.  <!-- `(min value 0, max vale 1024)` -->

Sjá til viðmiðunar: 
- [Adafruit IO example 9, analog out](https://github.com/adafruit/Adafruit_IO_Arduino/tree/master/examples/adafruitio_09_analog_out)
- [Analog Output (Arduino)](https://learn.adafruit.com/adafruit-io-basics-analog-output)
- [ESP32 PWM with Arduino IDE (Analog Output)](https://randomnerdtutorials.com/esp32-pwm-arduino-ide/)


---


### 6.6 Triggers (20%) 

Skoðaðu [Triggers](https://learn.adafruit.com/all-the-internet-of-things-episode-four-adafruit-io/triggers) og gerðu eftirfarandi:

1. Notaðu [Schedule Triggers (python)](https://learn.adafruit.com/adafruit-io-basics-scheduled-triggers) til að kveikja og svo slökkva á LED daglega á einhverjum sérstökum tíma.
1. Búðu til tvo `reactive trigger` í Adafruit IO, annar þeirra lætur lED á þegar það dimmir en hinn slekkur á LED þegar það er bjart. <br>
  - Tengdu LDR ljósviðnám í brauðbretti tengt við ESP32. <br>
  - Tengdu led peru í brauðbretti með viðnámi tengt við RaspberryPi. <br>

Sjá einnig til viðmiðunar: [How to Use Triggers in Your Adafruit IO Project](https://www.digikey.com/en/maker/blogs/2019/how-to-use-triggers-in-your-adafruit-io-project)

---


### Námsmat og skil

- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnir af tilraunum.

