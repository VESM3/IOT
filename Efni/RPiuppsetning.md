# Raspberry Pi 

### 1. Uppsetning á RPi OS stýrikerfi 
1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/) forritið með microSD kort og usb lykli í tölvunni.
1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34), 
    1. Veldu **Raspberry Pi OS (Legacy)** sem er **Debian Buster 32-bit** stýrikerfið (ath. það er ekki default) 
    2. Veldu Settings (tannhjólið) eða `CTRL+ SHIFT + X` til að gera efirfarandi stillingar [myndband](https://www.youtube.com/watch?v=s93ss44C_yM):
        - Veldu í Image customization options `to always use`
        - hostname í `nafnið þitt` (ekk nota sérstafi/íslenska) t.d. gunnarthorunnarson
        - Enable SSH. Ekki breyta **pi** user og notaðu lykilorðið **raspberry**  (breytum seinna lykilorðinu)
        - Configure wifi: sleppa (gerum seinna í config skrá)
        - Wifi country: sleppa (gerum seinna í config skrá)
        - Set local settings: Atlantic/Reykjavík
        - Keyboard layout: IS
1. Veldu microSD kortið þitt og smelltu á write. **Ath** Ef hann býður upp í lokin að formata drif þá velja **Cancel**
1. Fjarlægðu SD kortið úr tölvunni þegar þú ert búinn.

---

### 2. Wifi stilling á SD kort 
1. Settu SD kortið í usb lykil í tölvuna.
2. Búðu til skránna `wpa_supplicant.conf` td. með VSCode editor.   
3. Settu eftirfarandi Wifi stillingar sem virkar fyrir skólann og heima í skránna:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IS

network={
	ssid="WiFiSSIDforNetworkHome"   # finnur upplýsingarnar á router.
	priority=2
	psk="passwordforHome"  # lykilorð til að geta tengst router.
	id_str="home"
	key_mgmt=WPA-PSK       # algengt og má sleppa, getur verið mismunandi

}
network={
	ssid="TskoliVESM"  
    	priority=1 
	psk="Fallegurhestur"  # lykilorð
    	id_str="school"
    	key_mgmt=NONE
}

```
4. Vistaðu skránna í rótina (`boot`) á SD kortinu.

---

### 3. Stillingar. Stýrikerfið á Raspberry Pi

1. Settu SD minniskortið í RaspberryPi og tengdu við rafmagn (usb power port).
1. **SSH tenging**. Ef þú ert með **Windows** notaðu þá `GitBash`. Ef **Mac/Linux** þá `terminal` (þú gætir þurft að nota `sudo`)
1. Notaðu  _pi@hostname.tskoli.vesm_ í skólanum og _pi@hostname.local_ ef þú ert heima. 
    - hostname getur t.d. verið nafnið þitt (ekki sérstafi). Það er líka hægt að nota ip töluna `ssh pi@iptalan`.     
      ```Linux
      ssh pi@hostname.local  # skóli: ssh pi@hostname.tskoli.vesm       
      password: raspberry    
      ```   
1. Breyttu sjálfgefna _raspberry_ lykilorðinu í eitthvað annað (lágmark 8 stafir).
1. Skrifaðu `sudo raspi-config` og veldu _Interfacing Options_, allt þar á vera **enabled**
1. Uppfærðu RPi stýrikerfið með `sudo apt-get update` og svo `sudo apt-get upgrade`. Endurræstu svo RPi.
1. Núnar er RPi klárt til notkunar!

Ef þú þarft að finna út IP eða MAC address á RPI í skólanum (TskoliVESM) þá er hægt að nota td. Advanced IP Scanner og setja inn leitarskilyrðin: `10.201.48.1-10.201.49.254`. Það á líka að vera hægt að nota [nmap](https://www.maketecheasier.com/scan-local-network-with-terminal-macos/) `nmap 10.201.48.0/24`. **Ath** tölvan þín þarf að vera á sama wifi netinu þegar þú scannar. Svo er `ifconfig` gagnleg skipun.

---

### 4. Að tengjast RPi með VNC (GUI) 
1. [leiðbeiningar](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#enabling-and-connecting-over-vnc). <br> Að keyra VNC server á Raspberry Pi leyfir þér að tengjast RPi desktop þráðlaust á fartölvu með [VNC viewer](https://www.realvnc.com/en/connect/download/viewer/). VNC server þarf að vera enable á RPi.
1. [stillingar á RPi OS](https://projects.raspberrypi.org/en/projects/raspberry-pi-using/0) t.d. að breyta upplausn á skjánum (1024x768). 



