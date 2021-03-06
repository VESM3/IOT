## Tímaverkefni 1 (6%)

- Raspberry Pi 
- GPIO

---

#### 1. Að tengjast Raspberry Pi (15%)
1. Settu SD minniskortið (frá kennara) sem inniheldur Bullsey stýrikerfi í RaspberryPi og tengdu við rafmagn (usb power port).
1. **SSH tenging**. Ef þú ert með **Windows** notaðu þá `GitBash`. Ef **Mac/Linux** þá `terminal` (þú gætir þurft að nota `sudo`)
1. Notaðu  _hostname.tskoli.is_ í skólanum og _hostname.local_ heima     
      ```Linux
      ssh pi@hostname.tskoli.is     # heima: ssh pi@hostname.local   
      password: raspberry
      ```  
1. Skrifaðu `sudo raspi-config` og veldu:
   1. Interfacing Options, allt þar á vera **enabled**
   1. System Options og breyttu eftirfarandi:
      * hostname í t.d ykkar nafn
      * password, ekki breyta user (er pi)
1. Að tengjast RPi með VNC (GUI),  [leiðbeiningar](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#enabling-and-connecting-over-vnc). <br> Að keyra VNC server á Raspberry Pi leyfir þér að stjórna RPi desktop þráðlaust á fartölvu (the VNC viewer).
1. Gerðu aðrar viðeigandi [stillingar á RPi OS](https://projects.raspberrypi.org/en/projects/raspberry-pi-using/0) t.d. að breyta upplausn á skjánum. 
1. Til að tengjast heima og í skólanum, þá skaltu búa til skrá á SD kortinu boot/ sem heitir `wpa_supplicant.conf`. Það er einnig hægt að gera breytingarnar í skólanum í nano beint á RPi ef þú veist [wifi stillingarnar](https://github.com/VESM3/IOT/blob/main/Efni/wifi.md) heima. 

      ```
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
      update_config=1
      country=IS

      network={
          ssid="Taekniskolinn"
          key_mgmt=NONE
          priority=-999
      }

      network={
              ssid="ssid á beini (ráter)"
              key_mgmt=WPA-PSK
              proto=WPA2
              pairwise=CCMP
              group=CCMP
              psk="lykilorð á beini"
              priority=1
      }
      ```
<!-- 
**Ath**. Ef það er blár skjár sjá [How to Fix Raspberry Pi's 'Cannot Currently Show the Desktop' Error](https://www.tomshardware.com/how-to/fix-cannot-currently-show-desktop-error-raspberry-pi)
[PuTTY](https://www.putty.org/) og fylgdu [Connecting via SSH](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#connecting-via-ssh).
-->


**Ath.** [Leiðbeiningar](https://github.com/VESM3/IOT/blob/main/Efni/RPiuppsetning.md) til að setja upp RPi stýrikerfi og wifi stillingar frá grunni.

---

#### 2. Thonny ritill. (10%)
Notaðu [Thonny](https://thonny.org/) ritil á RPi OS. Búðu til python skrá og prentaðu út strenginn með nafninu þínu. 
- [Get Started with Thonny IDE on Raspberry Pi OS](https://roboticsbackend.com/thonny-ide-raspberry-pi-os/) 

---

#### 3. Nano ritill í terminal. (10%)
1. Kynntu þér og notaðu [nano](https://www.nano-editor.org/) command-line ritil í terminal, búðu til skrá og prentaðu út nafnið þitt, sjá t.d. [Raspberry Pi – Run Python Script in the Terminal](https://roboticsbackend.com/raspberry-pi-run-python-script-in-the-terminal/). Prófaðu m.a. að nota músina, fá línunúmer og fleira.


---

#### 4. GPIO: Blikkandi ljós. (15%)
Láttu LED blikka á brauðbretti með python kóða. Notaðu [T-Coppler](https://www.adafruit.com/product/2028) með brauðbrettinu og [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/) python safnið með kóðalausn. Nýttu þér kóðalausnir í [Basic Recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html). Hér er svo [GPIO Zero pinout](https://gpiozero.readthedocs.io/en/stable/cli_tools.html#pinout) þegar þú notar ekki T-Coppler.

---

#### 5. GPIO: Blikkandi LED með fade. (15%)
Láttu LED _fade_ inn og út.

---

#### 6. GPIO: Takki og LED. (15%)
Við að ýta á takka þá kemur birta af LED. 


---

#### 7. Bluedot og GPIO. (20%)
1. Notaðu [BlueDot](https://gpiozero.readthedocs.io/en/stable/recipes_advanced.html#bluedot-led) (bluetooth) með android símanum þínum til að kveikja/slökkva á LED sem er uppsett á brauðbretti tengt við RPi.
1. Notaðu BlueDot til að kveikja á RGB LED. Það á að vera hægt að velja um 4 mismunandi liti með BlueDot.
<br>

**Ath.** iPhone virkar ekki með BlueDot en það er hægt að nota annan RPi og [Blue Dot Python App](https://bluedot.readthedocs.io/en/latest/bluedotpythonapp.html) í stað síma.

---

### Námsmat og skil

- Yfirferð á sér stað í tíma. 
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu kóðalausnir.


