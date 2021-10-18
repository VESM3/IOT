## Tímaverkefni 1 (6%)
- RaspberryPi Zero W uppsetning og stillingar.
- Einstaklingsverkefni

---

### 1. Uppsetning á RPi OS stýrikerfi á microSD kort. 
   1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
   1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34), 
       - veldu 32-bita útgáfuna af RPi OS, uppsetningin getur tekið c.a. 10 mín.
   1. Enable SSH. Búðu til tóma textaskrá sem heitir `SSH` með enga endingu í rótina á microSD kortinu.

---

### 2. Til að tengjast RPi Zero með Ethernet yfir USB (virkar bara með Pi Zero) 
Til að tengjast RPi Zero W frá tölvunni þinni með USB gagna portinu (knýr einnig RPi Zero), [leiðbeiningar](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#direct-usb-connection-pi-zero-zero-w-only), sjá einnig [myndband](https://www.youtube.com/watch?v=XaTmG708Mss)
   1. Opnaðu skránna `config.txt` sem er í rótinni á microSD kortinu,
   2. Bættu við `dtoverlay=dwc2` í enda skráarinnar.
   3. Opnaðu `cmdline.txt` og bættu við textanum `modules-load=dwc2,g_ether` eftir orðinu `rootwait` og vistaðu skránna.
   4. Fyrir Windows: 
        - download and install [Bonjour Print Services](https://support.apple.com/kb/DL999?viewlocale=en_US&locale=en_US) from apple.com (if you have Windows)
           - helps your PC to see the Pi
           - gætir þurft einnig [USB Ethernet Driver](https://www.catalog.update.microsoft.com/Search.aspx?q=USB+RNDIS+Gadget), (sjá myndband) 
   5. Settu microSD kortið í RPi Zero.
   6. Tengdu micro USB kapal við USB portið á RPi Zero (ekki PWR portið).
   7. Núna getur þú notað SSH til að stýra RPi (sjá næsta lið).

---

### 3. Að nota SSH til að vinna á RPi Zero (yfir USB). 
Notaðu `PowerShell`  (eða PuTTY) ef þú ert með Windows stýrikerfið. Notaðu `Terminal` í Mac og Linux. Fylgdu svo eftirfarandi [leiðbeiningum](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#connecting-via-ssh) 
    
   1. Tengdu micro USB kapal við USB portið á RPi Zero (ekki PWR portið).  
   1. Opnaðu PowerShell/Terminal og skrifaðu til að tengjast RPi með [SSH](https://en.wikipedia.org/wiki/Secure_Shell):
        ```Linux
           ssh pi@raspberrypi.local
           password: raspberry
        ```  
   1. Samþykktu allt, ekki breyta lykilorðinu (í bili).
   1. Notaðu [Linux skipanir](https://www.raspberrypi.com/documentation/computers/using_linux.html) til að skoða þig um.

---

### 4. Að tengjast RPi með VNC (GUI). 
Að keyra VNC server á Raspberry Pi leyfir þér að stjórna RPi desktop þráðlaust á fartölvu (the VNC viewer). [Leiðbeiningar](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#enabling-and-connecting-over-vnc)

---

### 5. Stillingar á RPi OS. 
   1. Fylgdu [Using your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-using/0) og gerðu viðeigandi stillingar; 
      - Country, Language, Timezone osfrv.
      - Tengdu RPi við wifi og upppfærðu stýrikerfið (tekur um 15-30 mín)
   1. Breyttu [`hostname`](https://www.tomshardware.com/how-to/raspberry-pi-change-hostname) í þitt nafn (ekk nota sérstafi/íslenska).

**Ath** þú þarft að uppfæra VNC tenginguna þína í `nafn.local` og nota nýja lykilorðið með notendanafninu `pi` sem á að vera óbreytt.

---

### 6. Kóðaritlar 
   1. Notaðu SSH og [nano](https://www.nano-editor.org/) command-line ritil í terminal og prentaðu út í console nafnið þitt með python. 
   1. Notaðu VNC og [Thonny](https://thonny.org/) ritil á RPi OS. Prentaðu út í console strenginn með nafninu þínu með python. 

---

### Námsmat
Yfirferð á sér stað í tíma. Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.

1. Uppsetning og stillingar (70%)
1. Getur unnið með RPi Zero W og kóðaritla (30%)
