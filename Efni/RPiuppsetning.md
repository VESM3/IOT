# Raspberry Pi 

### 1. Uppsetning á RPi OS stýrikerfi 
1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/) forritið með microSD kort og usb lykli í tölvunni.
1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34), 
    1. Veldu **Raspberry Pi OS (Legacy)** sem er **Debian Buster 32-bit** stýrikerfið (ath. það er ekki default) 
    2. Veldu Advanced options með lyklaborði `CTRL+ SHIFT + X` til að gera efirfarandi stillingar [myndband](https://www.youtube.com/watch?v=s93ss44C_yM):
        - Veldu í Image customization options `to always use`
        - hostname í `nafnið þitt` (ekk nota sérstafi/íslenska) t.d. gunnarthorunnarson
        - Enable SSH. Ekki breyta **pi** user en búðu til lykilorð t.d. _vesm3_
        - Configure wifi: sleppa (gerum seinna)
        - Wifi country: sleppa (gerum seinna)
        - Set local settings: Atlantic/Reykjavík
        - Keyboard layout: IS
1. Veldu microSD kortið þitt og smelltu á write. **Ath** Ef hann býður upp í lokin að formata drif þá velja **Cancel**
1. Fjarlægðu SD kortið úr tölvunni þegar þú ert búinn.

---

### 2. Wifi stilling á SD kort 
1. Settu SD kortið í usb lykil í tölvuna.
2. Búðu til skránna `wpa_supplicant.conf` td. með VSCode editor.   
3. Settu eftirfarandi Wifi stillingar fyrir skólann og heima í skránna:

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IS

network={
	ssid="WiFiSSIDforNetworkHome"   # finnur upplýsingarnar á router.
	priority=2
	psk="passwordforHome"  # lykilorð til að geta tengst router.
	id_str="home"
	key_mgmt=WPA-PSK   # algengt og má sleppa, getur verið mismunandi

}
network={
	ssid="Taekniskolinn"  
    	priority=1 
    	id_str="school"
    	key_mgmt=NONE
}

```
4. Vistaðu skránna í rótina (`boot`) á SD kortinu.

---

### 3. Stillingar. Stýrikerfið á Raspberry Pi

1. Settu SD minniskortið í RaspberryPi og tengdu við rafmagn (usb power port).
1. **SSH tenging**. Ef þú ert með **Windows** notaðu þá `GitBash`. Ef **Mac/Linux** þá `terminal` (þú gætir þurft að nota `sudo`)
1. Notaðu  _pi@hostname.tskoli.is_ í skólanum og _pi@hostname.local_ ef þú ert heima. hostname getur t.d. verið nafnið þitt (ekki sérstafi). Það er líka hægt að nota ip töluna `ssh pi@iptalan`      
      ```Linux
      ssh pi@hostname.tskoli.is     # heima: ssh pi@hostname.local 
      password: raspberry
      ```   
1. Skrifaðu `sudo raspi-config` og veldu _Interfacing Options_, allt þar á vera **enabled**
1. Uppfærðu RPi stýrikerfið með `sudo apt-get update` og svo `sudo apt-get upgrade`. Endurræstu svo RPi.



<!--
### 3. Að tengjast RPi með VNC (GUI), 
1. [leiðbeiningar](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#enabling-and-connecting-over-vnc). <br> Að keyra VNC server á Raspberry Pi leyfir þér að stjórna RPi desktop þráðlaust á fartölvu (the VNC viewer).
1. [stillingar á RPi OS](https://projects.raspberrypi.org/en/projects/raspberry-pi-using/0) t.d. að breyta upplausn á skjánum. 
-->


