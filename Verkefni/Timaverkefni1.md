## Tímaverkefni 1 (6%)
- RaspberryPi Zero W uppsetning og stillingar.
- Einstaklingsverkefni

---

### 1. Uppsetning á [RPi OS stýrikerfi  á microSD kort og usb lykli í tölvunni þinni 
   1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
   1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34), 
       - veldu 32-bita útgáfuna af RPi OS, 
       - Á lyklaborði `CTRL+ SHIFT + X` til að gera efirfarandi stillingar [myndband](https://www.youtube.com/watch?v=s93ss44C_yM):
          - Veldu `to always use`
          - hostname í `nafnið þitt`.local (ekk nota sérstafi/íslenska)
          - Enable SSH og búðu til nýtt lykilorð 
          - Configure wifi: sleppa 
          - Wifi country: sleppa
          - Set local settings: Atlantic/Reykjavík
          - Keyboard layout: IS
   1. Veldu microSD kortið þitt og smelltu á write. **Ath** Ef hann býður upp í lokin að formata drif þá velja **Cancel**
   2. Fjarlægðu SD kortið úr tölvunni þegar þú ert búinn.

---

### 2. Wifi stilling á SD kort 

1. Búðu til skránna `wpa_supplicant.conf`
2. Settu eftirfarandi Wifi stillingar í skránna:
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IS
network={
    ssid="Taekniskolinn"
    key_mgmt=NONE
}
```
3. vistaðu skránna í  `/boot/ directory` á SD kortinu.

**Ath** Til að fá wifi heima og í skólanum þá getur þú breytt wpa_supplicant.conf skránni eftirá, sjá [leiðbeiningar](https://github.com/VESM3/V21/blob/master/wifi.md)

---

### 3. Að tengjast RPi með SSH 
1. Settu SD kortið í RaspberryPi og tengdu hann við rafmagn (usb power)
1. SSH tenging
  - Ef þú ert með **Windows** notaðu þá [PuTTY](https://www.putty.org/) og fylgdu [Connecting via SSH](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#connecting-via-ssh). Í staðinn fyrir `raspberrypi.local` notaðu `hostname`.local sem þú valdir
  - Ef **Mac/Linux**  notaðu `terminal`. Þú gætir þurft að nota `sudo`, sjá [How to SSH into a Raspberry Pi [Beginner’s Tip]](https://itsfoss.com/ssh-into-raspberry/)
      ```Linux
      ssh pi@nafn.local  
      password: raspberry
      ```  
1. skrifaðu `sudo raspi-config` og farðu næst í lið 4 til að fá VNC

---

### 4. Að tengjast RPi með VNC (GUI). 
Að keyra VNC server á Raspberry Pi leyfir þér að stjórna RPi desktop þráðlaust á fartölvu (the VNC viewer). [Leiðbeiningar: Enabling and Connecting over VNC](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#enabling-and-connecting-over-vnc)

**Ath**. Ef það er blár skjár sjá [How to Fix Raspberry Pi's 'Cannot Currently Show the Desktop' Error](https://www.tomshardware.com/how-to/fix-cannot-currently-show-desktop-error-raspberry-pi)

---

### 5. Stillingar á RPi OS. 
   1. Fylgdu [Using your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-using/0) og gerðu viðeigandi stillingar; 
      - Country, Language, Timezone osfrv.
      - upppfærðu stýrikerfið heima (tekur tíma)
   1. Ef þú átt það eftir, breyttu [`hostname`](https://www.tomshardware.com/how-to/raspberry-pi-change-hostname) í þitt nafn.

**Ath** þú þarft að uppfæra VNC tenginguna þína í `nafn.local` og nota nýja lykilorðið með notendanafninu `pi` sem á að vera óbreytt.

---

### 6. Kóðaritlar 
   1. Notaðu [Thonny](https://thonny.org/) ritil á RPi OS. Búðu til python skrá og prentaðu út strenginn með nafninu þínu. 
   1. Notaðu [nano](https://www.nano-editor.org/) command-line ritil í terminal, búðu til skrá og prentaðu út nafnið þitt. 
   <!-- hjálp: https://cuny.manifoldapp.org/read/how-to-code-in-python-3/section/007210fd-623d-4dfe-8fcd-c87ef8a75405 --> 

---

### Hugsanleg vandamál
- [Að nota USB hub](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#interoperability-with-usb-3-0-hubs)

---


<!--

### Til að geta tengst RPi Zero með Ethernet yfir USB (virkar bara með Pi Zero)
Það þarf að gera eftirfarandi stillingar á microSD kortinu **áður** en þú notar RPi Zero W. Leiðbeiningar [myndband](https://youtu.be/XaTmG708Mss?t=185) og [vefgrein](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#direct-usb-connection-pi-zero-zero-w-only),

1. settu usb lykilm með SD kortinu í tölvuna og opnaðu drif sem heitir `boot`.
1. Opnaðu skránna `config.txt` sem er í rótinni á microSD kortinu,
1. Bættu við `dtoverlay=dwc2` í enda skráarinnar og vistaðu skránna.
1. Opnaðu næst `cmdline.txt` og bættu við textanum ` modules-load=dwc2,g_ether` eftir orðinu `rootwait` það á að vera autt bil á milli og vistaðu skránna.
1. Settu microSD kortið í RPi Zero
1. Tengdu micro USB kapal við USB portið á RPi Zero (ekki PWR portið). _Við þetta keyrir `firstrun.sh` skrá á RPi_
1. **Ef Windows** Ef tölvan sér ekki RPi þá þarftu líklegast networkdriver, sjá [leiðbeiningar (myndband)](https://youtu.be/XaTmG708Mss?t=415)
   1. [USB Ethernet adapter Driver (rnds)](https://www.catalog.update.microsoft.com/Search.aspx?q=USB+RNDIS+Gadget)  
   1.  sjá optional drivers í windows update og veldu þar driverinn sem á að uppfæra
1. Til að tölvan leyfir þér að nota SSH í localhost, download and install [Bonjour Print Services](https://support.apple.com/kb/DL999?viewlocale=en_US&locale=en_US) from apple.com (if you have Windows)
1. Núna getur þú notað SSH til að stýra RPi (sjá næsta lið).

-->

### Námsmat
Yfirferð á sér stað í tíma. Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.

1. Uppsetning og stillingar (80%)
1. Getur unnið með RPi Zero W og kóðaritla (20%)
