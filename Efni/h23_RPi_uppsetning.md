## Raspberry Pi uppsetning og stilling á stýrikerfi

### 1. Uppsetning á RPi OS stýrikerfi (Búið að gera af kennara)
1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/) forritið með microSD kort og usb lykli í tölvunni.
1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34), 
    1. Veldu **Raspberry Pi OS (Legacy)** sem er **Debian Bullsey** stýrikerfið (ath. það er ekki default) 
    2. Veldu Settings (tannhjólið) eða `CTRL+ SHIFT + X` til að gera efirfarandi stillingar [myndband](https://www.youtube.com/watch?v=s93ss44C_yM):
        - Veldu í Image customization options `to always use`
        - hostname í `h23vesmX-` (ekk nota sérstafi/íslenska) 
        - Enable SSH. Ekki breyta **pi** user og notaðu lykilorðið **Verksm1dj@** 
        - Configure wifi: TskoliVESM
        - Password: Fallegurhestur
        - Set local settings: Atlantic/Reykjavík
        - Keyboard layout: IS
1. Veldu microSD kortið þitt og smelltu á write. **Ath** 
1. Fjarlægðu SD kortið úr tölvunni þegar þú ert búinn.


---

### 2. Að tengjast Raspberry Pi með SSH (þarf að gera fyrst)

1. Settu SD minniskortið í RaspberryPi og tengdu við rafmagn (ekki fartölvu). Ath RPi4 þarf **3V**.
1. **SSH tenging**. Ef þú ert með **Windows** notaðu þá `GitBash`. Ef **Mac/Linux** þá `terminal` (þú gætir þurft að nota `sudo`)
1. Notaðu  _pi@hostname.tskoli.vesm_ eða ip töluna `ssh pi@iptalan` til að tengjast í skólanum.    
      ```Linux
      ssh pi@h23vesm1.vesm    # eða pi@h23vesm1   
      password: Verksm1dj@    
      ```   
1. Skrifaðu `sudo raspi-config` og veldu _Interfacing Options_, allt þar á vera **enabled**
1. Geymdu að uppfærðu RPi stýrikerfið með `sudo apt-get update` og svo `sudo apt-get upgrade` þar til þú ferð í smá pásu.
1. Endurræstu svo RPi. Núnar er RPi klárt til notkunar!

Ef þú þarft að finna út IP eða MAC address á RPI í skólanum (TskoliVESM) þá er hægt að nota td. Advanced IP Scanner og setja inn leitarskilyrðin: `10.201.48.1-10.201.49.254`. Það á líka að vera hægt að nota [nmap](https://www.maketecheasier.com/scan-local-network-with-terminal-macos/) `nmap 10.201.48.0/24`. <br>
**Ath** tölvan þín þarf að vera á sama wifi netinu þegar þú scannar. Svo er `ifconfig` gagnleg skipun.

---

### 3. Að tengjast RPi með VNC (GUI) 
1. [leiðbeiningar](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#enabling-and-connecting-over-vnc). <br> Að keyra VNC server á Raspberry Pi leyfir þér að tengjast RPi desktop þráðlaust á fartölvu með [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/). VNC server þarf að vera enable á RPi.
1. [stillingar á RPi OS](https://projects.raspberrypi.org/en/projects/raspberry-pi-using/0) t.d. að breyta upplausn á skjánum (1024x768). 



