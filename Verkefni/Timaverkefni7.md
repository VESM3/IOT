
_drög_

# Tímaverkefni 7 (14%)

- Einstaklingsverkefni
- Adafruit IO (IoT cloud platform)

---

### 7.1 Adafruit IO umhverfið (5%)
1. AdafruitIO+ aðgangur
   - Náðu í Adarfuit IO+ aðgang (1 ár frítt) hjá [Github Student Pack](https://education.github.com/pack) og tengdu saman Github og [Adafruit](https://www.adafruit.com/) reikning.
   - Í Adafruit reikningnum skaltu velja `services`, `view discount` (þar er kóðaruna fyrir Adafruit IO).
   - Skráðu þig inn hjá [Adafruit IO](https://io.adafruit.com/). Veldu `Upgrade to IO+` sem er neðst á síðunni og smelltu svo á hnappinn `Redeem a Coupon or Pass` og settu inn rununa til að fá 1 ár frítt. Ath. það þarf aldrei að gefa upp kredikortaupplýsingar.
1. Skoðaðu [Welcome to Adafruit IO](https://learn.adafruit.com/welcome-to-adafruit-io) , skoðaðu sérstaklega [Feeds](https://learn.adafruit.com/adafruit-io-basics-feeds) og [Dashboards](https://learn.adafruit.com/adafruit-io-basics-dashboards). Hér eru svo [myndbönd](https://learn.adafruit.com/all-the-internet-of-things-episode-four-adafruit-io/how-adafruit-io-works).
1. Fylgdu tilraun í myndbandinu [Connecting the Raspberry Pi to Adafruit IO cloud](https://www.youtube.com/watch?v=IfzpoFGkmns)

#### Adafruit söfn og APIs:
   - [Adafruit IO Python safn](https://adafruit-io-python-client.readthedocs.io/en/latest/quickstart.html) 
   - [Adafruit IO Arduino (ESP32) safn](https://github.com/adafruit/Adafruit_IO_Arduino)
      - þarf að hafa einnig ArduinoHTTPClient og Adafruit MQTT söfn.  
   - [Adafruit IO MQTT API](https://io.adafruit.com/api/docs/mqtt.html#adafruit-io-mqtt-api)
   - [Adafruit IO HTTP API](https://io.adafruit.com/api/docs/#adafruit-io-http-api)
 
<!-- 
- [Python kóði með tutorials](https://github.com/adafruit/Adafruit_IO_Python/tree/master/examples/basics).
- AdafruitIO [forum](https://forums.adafruit.com/viewforum.php?f=56) og [discord](https://discord.com/invite/adafruit) 
-->

---

### 7.2 Digital Input (15%)
Sendu stöðu hnapps á/af (í rauntíma) sem er tengdur við Raspberry Pi til Adafruit IO. <br>
Skoðaðu niðurstöður með **Gauge block** í Dashboard. <br>

Sjá til viðmiðunar: [Digital Input (Python)](https://learn.adafruit.com/adafruit-io-basics-digital-input). 

- Notaðu GPi.Zero safnið í staðinn fyrir `adafruit_blinka`. 
- Notaðu REST API 

---

### 7.3 Digital Output (15%)
Tengdu eina LED í brauðbretti með viðnámi tengt við RaspberryPi. <br>
Kveiktu og slökktu á LED með **toogle** hnapp í Dashboard í Adafruit IO. <br>

Sjá til viðmiðunar: [Digital Output (Python)](https://learn.adafruit.com/adafruit-io-basics-digital-output). 

- Notaðu GPi.Zero safnið í staðinn fyrir `adafruit_blinka`. 
- Notaðu REST API 

---

### 7.4 Schedule Triggers (15%) 

Tengdu eina led peru í brauðbretti með viðnámi tengt við RaspberryPi. <br>
Notaðu [Schedule Triggers (python)](https://learn.adafruit.com/adafruit-io-basics-scheduled-triggers) til að kveikja og slökkva á led með 30 minútu millibili.

- Notaðu GPi.Zero safnið í staðinn fyrir `adafruit_blinka`. 

---

### 7.5 Analog Input (15%) 
Tengdu LDR ljósviðnám í brauðbretti tengt við ESP32. <br>
Sendu mælingar (analog gildi) frá ljósviðnámi til Adafruit IO <br>
Birtu rauntímaniðurstöður með _Gauge block_ og línuriti í Dashboard.  <br>

- Notaðu MQTT (eða REST API)


Sjá til viðmiðunar: 
- [Analog Input (Arduino)](https://learn.adafruit.com/adafruit-io-basics-analog-input) 
- [ESP32 ADC – Read Analog Values with Arduino IDE](https://randomnerdtutorials.com/esp32-adc-analog-read-arduino-ide/)

<!--
- [python kóði með notkun MCPP3008 ADC converter](https://github.com/adafruit/Adafruit_IO_Python/blob/master/examples/basics/analog_in.py) 
-->

---

### 7.6 Analog Output (15%) 

Notaðu **Slider block** í **Dashbord** með Adafruit IO til að stýra birtustig á LED sem er tengd við PWM pinna á ESP32.  <!-- `(min value 0, max vale 1024)` -->
- Notaðu MQTT (eða REST API)

Sjá til viðmiðunar: 
- [Analog Output (Arduino)](https://learn.adafruit.com/adafruit-io-basics-analog-output)
- [ESP32 PWM with Arduino IDE (Analog Output)](https://randomnerdtutorials.com/esp32-pwm-arduino-ide/)


<!--
- [Kóðalausn, en með notkun PWM driver (erum ekki með)](https://learn.adafruit.com/adafruit-io-basics-analog-output/python-code)
- [RPi Python Programming 16: Analog output and software PWM](https://www.engineersgarage.com/raspberrypi/articles-raspberry-pi-python-software-pwm-led-fading/)
- [Raspberry Pi PWM Tutorial | Control Brightness of LED](https://electronicshobbyists.com/raspberry-pi-pwm-tutorial-control-brightness-of-led-and-servo-motor/)
-->

---


### 7.7 Reactive Triggers (20%) 

Tengdu LDR ljósviðnám í brauðbretti tengt við ESP32. <br>
Tengdu led peru í brauðbretti með viðnámi tengt við RaspberryPi. <br>
Búðu til `reactive trigger` í Adafruit IO sem lætur led peru kveikja á sér þegar það dimmir en slekkur á sér þegar það er bjart. <br>

Sjá til viðmiðunar: [How to Use Triggers in Your Adafruit IO Project](https://www.digikey.com/en/maker/blogs/2019/how-to-use-triggers-in-your-adafruit-io-project)

- Notaðu GPi.Zero safnið í staðinn fyrir `adafruit_blinka`. 

---


### Námsmat og skil

- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnir af tilraunum.

