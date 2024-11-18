## Raspberry Pi 4 uppsetning 
_uppfært 18.11.2024_

### 1. Uppsetning á RPi OS stýrikerfi 
1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/) forritið í tölvuna þína.
1. Settu microSD kortið með usb lykli í tölvuna.
1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34).
    1. Veldu **Raspberry Pi 4** og **RASPBERRY PI OS (64 bit)** stýrikerfið og veldu usb portið með microSD kortinu.
    2. Veldu Edit Settings til að gera efirfarandi [stillingar (mynd)](https://github.com/VESM3/IOT/blob/main/Myndir/RPi_uppsetning.png):
        - Veldu í Image customization options `to always use`
        - hostname í `h24vesmX` þar sem X er tala sem þú færð frá kennara (ekk nota sérstafi/íslenska) 
        - Ekki breyta **pi** user og notaðu lykilorðið **Verksm1dja** 
        - Configure wifi: TskoliVESM
        - Password: Fallegurhestur
        - Set local settings: Atlantic/Reykjavík
        - Keyboard layout: IS
1. Veldu svo **YES** og aftur **YES** og hinkraðu þangað þetta er búið (c.a. 15 mín). 
1. Fjarlægðu SD kortið úr tölvunni þegar þú ert búinn og settu það í RaspberryPi 4.

<!-- [myndband upppsetning](https://www.youtube.com/watch?v=s93ss44C_yM) -->

---

### 2. Að tengjast RPi með VNC (GUI) 
Að keyra VNC server á Raspberry Pi leyfir þér að tengjast RPi desktop þráðlaust á fartölvu með [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/).
1. Tengdu RPi4 við skjá, mús og lyklaborð
1. VNC server þarf að vera enable á RPi. Farðu í _Preferences_ og þar í _Raspberry Pi Configuration_ og þar skaltu velja  _Interfaces_ og hakaðu við VNC (enable). 
1. Náðu í [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/) í fartölvuna.
    1. Búðu til VNC tengingu (New Connection)
       ```
       VNC Server:  ip talan      // eða hostname (prófaðu h24vesm1 eða h24vesm1.tskoli.vesm)
       user:  pi
       lykilorð: Verksm1dja        
       ```
    1. Tvísmelltu á tenginguna, notendafnið er `pi` (ekki breyta) og lykilorð. 
1. Núna getur þú tengst RPi4 með fartölvunni og hætt að nota skjáinn, músin og lyklaborðið með RPi4
   
---

<details>
<summary>Að tengjast Raspberry Pi með SSH </summary>
<br>
  
1. Settu SD minniskortið í RaspberryPi og tengdu við rafmagn (ekki fartölvu). Ath RPi4 þarf **3V**. Sum RPi USB port þarf að jugga til aðeins til að fá ljós.
1. Í tölvunni tengdu þig við sama wifi og á RPI4. Ef þú ert með **Windows** notaðu þá `GitBash`. Ef **Mac/Linux** þá `terminal` (þú gætir þurft að nota `sudo`)
1. Notaðu ip töluna `ssh pi@iptalan `  (best) eða hostname t.d. h24vesm1 ... til að tengjast í skólanum.    
      ```Linux
      ssh pi@h24vesm1.tskoli.vesm    # ef virkar ekki prófaðu þá pi@h24vesm1 eða pi@hostname.vesm
      password: Verksm1dj@    
      ```   
1. Skrifaðu `sudo raspi-config` og veldu _Interfacing Options_, allt þar á vera **enabled** sérstaklega VNC Server
1. Geymdu að uppfærðu RPi stýrikerfið með `sudo apt-get update` og svo `sudo apt-get upgrade` þar til þú ferð í smá pásu.
1. Endurræstu svo RPi. Núnar er RPi klárt til notkunar!
1. Náðu í `Remote - SSH` extension í VSCode í fartölvunni þinni. Tengdu þig við RPi (pi@iptalan) og prófaðu að prenta út streng með **nafninu þínu**

> Ef þú þarft að finna út IP eða MAC address á RPI í skólanum (TskoliVESM) þá er hægt að nota td. [nmap](https://www.maketecheasier.com/scan-local-network-with-terminal-macos/) `nmap 10.201.48.0/24 -sn -Pn`. **Ath** tölvan þín þarf að vera á sama wifi netinu þegar þú scannar. Svo er `ifconfig` gagnleg skipun.

</details>

<details>
<summary>Troubleshoot
 </summary>
<br>
  
- Ef þú nærð ekki VNC (_eða SSH_) samband við RPi (fartölva þarf að vera á sama wifi og RPi): 
     - nota nmap í terminal: 10.201.48.0/24 -sn -Pn.
     - keyra skipunina `nslookup hostname.tskoli.vesm` til að fá `IP` töluna sem þú getur þá notað í staðinn fyrir `hostaname.tskoli.vesm`  (virkar ekki alltaf)
- SSH. Ef permission denied (publickey) á rpi. Þá hreinsa út eldra key úr tölvunni `$ ssh-keygen -R [hostname-or-IP]`
- port 22: Connection timed out. SSH lokað útaf firewall í tölvu [windows fix](https://www.windowscentral.com/how-open-port-windows-firewall) 2 nemendur lentu í þessu
- Ef þú færð svartan skjá  gerðu þá eftirfarandi breytingu í skrá (með SSH tengingu á RPi4): `/boot/config.txt`. Taktu commentið út (`#`) af `hdmi_force_hotplug=1`.

</details>

<!-- 
Advanced IP Scanner og setja inn leitarskilyrðin: `10.201.48.1-10.201.49.254`. Það á líka að vera hægt að nota 
skanna wifi með að nota _Advanced IP Scanner_ forrit og setja inn leitarskilyrðin: 10.201.48.1-10.201.49.254.
-->

