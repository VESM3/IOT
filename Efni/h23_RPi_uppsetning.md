## Raspberry Pi uppsetning og stilling á stýrikerfi

### 1. Uppsetning á RPi OS stýrikerfi 
1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/) forritið í tölvuna þína. 
1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34) á microSD kortið með usb lykli í tölvunni.
    1. Veldu **Raspberry Pi OS (Legacy)** sem er **Debian Bullsey** stýrikerfið 
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

1. Settu SD minniskortið í RaspberryPi og tengdu við rafmagn (ekki fartölvu). Ath RPi4 þarf **3V**. Sum RPi USB port þarf að jugga til aðeins til að fá ljós.
1. **SSH tenging**. Ef þú ert með **Windows** notaðu þá `GitBash`. Ef **Mac/Linux** þá `terminal` (þú gætir þurft að nota `sudo`)
1. Notaðu ip töluna `ssh pi@iptalan `  (best) eða hostname t.d. h23vesm1, h23vesm2 ... til að tengjast í skólanum.    
      ```Linux
      ssh pi@h23vesm1.tskoli.vesm    # ef virkar ekki prófaðu þá pi@h23vesm1 eða pi@hostname.vesm
      password: Verksm1dj@    
      ```   
1. Skrifaðu `sudo raspi-config` og veldu _Interfacing Options_, allt þar á vera **enabled** sérstaklega VNC Server
1. Geymdu að uppfærðu RPi stýrikerfið með `sudo apt-get update` og svo `sudo apt-get upgrade` þar til þú ferð í smá pásu.
1. Endurræstu svo RPi. Núnar er RPi klárt til notkunar!
1. Náðu í `Remote - SSH` extension í VSCode í fartölvunni þinni. Tengdu þig við RPi (pi@iptalan) og prófaðu að prenta út streng með **nafninu þínu**

> Ef þú þarft að finna út IP eða MAC address á RPI í skólanum (TskoliVESM) þá er hægt að nota td. [nmap](https://www.maketecheasier.com/scan-local-network-with-terminal-macos/) `nmap 10.201.48.0/24 -sn -Pn`. **Ath** tölvan þín þarf að vera á sama wifi netinu þegar þú scannar. Svo er `ifconfig` gagnleg skipun.

---

### 3. Að tengjast RPi með VNC (GUI) 
Að keyra VNC server á Raspberry Pi leyfir þér að tengjast RPi desktop þráðlaust á fartölvu með [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/). VNC server þarf að vera enable á RPi (sjá lið 2).
1. Náðu í [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/) í fartölvuna.
   1. Búðu til VNC tengingu (New Connection)
   ```
   VNC Server:  ip talan      // eða hostname; hostname.tskoli.vesm, h23vesm1, h23vesm2 osfrv.  Notaðu IP tölu ef hostname virkar ekki.
   user:  pi
   lykilorð:                  // Lykilorð færðu frá kennara.
   ```
   1. Tvísmelltu á tenginguna, notendafnið er `pi` (ekki breyta) og lykilorð færðu frá kennara. 
1. Skoðaðu stýrikerfið og [stillingar](https://projects.raspberrypi.org/en/projects/raspberry-pi-using/0).
1. Notaðu [Thonny](https://thonny.org/) ritil. Búðu til python skrá og prentaðu út streng með **nafninu þínu**, sjá [Thonny IDE on Raspberry Pi OS](https://roboticsbackend.com/thonny-ide-raspberry-pi-os/).

> Ef þú færð svartan skjá  gerðu þá eftirfarandi breytingu í skrá (með SSH tengingu á RPi4): `/boot/config.txt`. Taktu commentið út (`#`) af `hdmi_force_hotplug=1`.

---

### Troubleshoot

- Ef þú nærð ekki VNC (_eða SSH_) samband við RPi (fartölva þarf að vera á sama wifi og RPi): 
     - nota nmap í terminal: 10.201.48.0/24 -sn -Pn.
     - keyra skipunina `nslookup hostname.tskoli.vesm` til að fá `IP` töluna sem þú getur þá notað í staðinn fyrir `hostaname.tskoli.vesm`  (virkar ekki alltaf)
- SSH. Ef permission denied (publickey) á rpi. Þá hreinsa út eldra key úr tölvunni `$ ssh-keygen -R [hostname-or-IP]`
- port 22: Connection timed out. SSH lokað útaf firewall í tölvu [windows fix](https://www.windowscentral.com/how-open-port-windows-firewall) 2 nemendur lentu í þessu

<!-- 
Advanced IP Scanner og setja inn leitarskilyrðin: `10.201.48.1-10.201.49.254`. Það á líka að vera hægt að nota 
skanna wifi með að nota _Advanced IP Scanner_ forrit og setja inn leitarskilyrðin: 10.201.48.1-10.201.49.254.
-->

