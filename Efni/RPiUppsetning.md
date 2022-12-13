
### 1. Uppsetning á [RPi OS stýrikerfi  á microSD kort og usb lykli í tölvunni þinni 
   1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
   1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34), 
       - veldu 32-bita útgáfuna af RPi OS, 
       - CTRL+ SHIFT + X  til að fara í stillingar  [myndband](https://www.youtube.com/watch?v=s93ss44C_yM)
          - Veldu `to always use`
          - hostname í nafnið þitt.local 
          - Enable SSH og búðu til nýtt lykilorð 
          - Configure wifi: sleppa 
          - Wifi country: sleppa
          - Set local settings: Atlantic/Reykjavík
          - Keyboard layout: IS
   1. Veldu microSD kortið þitt og smelltu á write. **Ath** Ef hann býður upp í lokin að formata drif þá velja **Cancel**
   2. Fjarlægðu SD kortið úr tölvunni þegar þú ert búinn.

---

### 2. Wifi stilling á SD kort 

1. Búðu til skrá `wpa_supplicant.conf` og vistaðu  hana í  `/boot/ directory` á SD kortinu.
2. Settu inn þínar Wifi stillingar, sjá [leiðbeiningar](https://github.com/VESM3/V21/blob/master/wifi.md)

---

### 3. Að nota SSH til að vinna á RPi
Settu SD kortið í RaspberryPi og tengdu hann við rafmang  (usb power)

**Windows** Notaðu [PuTTY](https://www.putty.org/) 
Fylgdu að [tengjast via SSH](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#connecting-via-ssh) 

**Mac/Linux**  notaðu `terminal`.
```Linux
ssh pi@raspberrypi.local
password: raspberry
```  

Sjá einnig [How to SSH into a Raspberry Pi [Beginner’s Tip]](https://itsfoss.com/ssh-into-raspberry/)

<!-- 1. Notaðu [Linux skipanir](https://www.raspberrypi.com/documentation/computers/using_linux.html) til að skoða þig um til gamans. -->

---

### 4. Að tengjast RPi með VNC (GUI). 
Að keyra VNC server á Raspberry Pi leyfir þér að stjórna RPi desktop þráðlaust á fartölvu (the VNC viewer). [Leiðbeiningar](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#enabling-and-connecting-over-vnc)

---

### 5. Stillingar á RPi OS. 
   1. Fylgdu [Using your Raspberry Pi](https://projects.raspberrypi.org/en/projects/raspberry-pi-using/0) og gerðu viðeigandi stillingar; 
      - Country, Language, Timezone osfrv.
      - upppfærðu stýrikerfið heima (tekur tíma)
   1. Ef þú átt það eftir, breyttu [`hostname`](https://www.tomshardware.com/how-to/raspberry-pi-change-hostname) í þitt nafn (ekk nota sérstafi/íslenska).

**Ath** þú þarft að uppfæra VNC tenginguna þína í `nafn.local` og nota nýja lykilorðið með notendanafninu `pi` sem á að vera óbreytt.

---

### 6. Kóðaritlar 
   1. Notaðu [Thonny](https://thonny.org/) ritil á RPi OS. Búðu til python skrá og prentaðu út strenginn með nafninu þínu. 
   1. Notaðu [nano](https://www.nano-editor.org/) command-line ritil í terminal, búðu til skrá og prentaðu út nafnið þitt. 
   <!-- hjálp: https://cuny.manifoldapp.org/read/how-to-code-in-python-3/section/007210fd-623d-4dfe-8fcd-c87ef8a75405 --> 

---

