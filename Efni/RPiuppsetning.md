
### 1. Uppsetning á RPi OS stýrikerfi 
   1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/) með microSD kort og usb lykli í tölvunni 
   1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34), 
       - veldu **Raspberry Pi OS (Legacy)** sem er **Debian Buster** stýrikerfið (ath. það er ekki default) 
       - Á lyklaborði `CTRL+ SHIFT + X` til að gera efirfarandi stillingar [myndband](https://www.youtube.com/watch?v=s93ss44C_yM):
          - Veldu `to always use`
          - hostname í `nafnið þitt`.tskoli.is (ekk nota sérstafi/íslenska)
          - Enable SSH og búðu til nýtt lykilorð 
          - Configure wifi: sleppa 
          - Wifi country: sleppa
          - Set local settings: Atlantic/Reykjavík
          - Keyboard layout: IS
   1. Veldu microSD kortið þitt og smelltu á write. **Ath** Ef hann býður upp í lokin að formata drif þá velja **Cancel**
   2. Fjarlægðu SD kortið úr tölvunni þegar þú ert búinn.

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
	ssid="WiFiSSIDforNetworkHome"
	priority=2
	psk="passwordforHome"
	id_str="home"
	key_mgmt=WPA-PSK   # algengt og má sleppa, getur verið mismunandi e. protocol

}
network={
	ssid="Taekniskolinn"  
    	priority=1 
    	id_str="school"
    	key_mgmt=NONE
}


```
4. Vistaðu skránna í rótina (`/boot`) á SD kortinu.
5. Gerðu viðeigandi stillingar í RPi og uppfærðu stýrikerfið sjá nánar [Tímaverkefni 1](https://github.com/VESM3/IOT/blob/main/Verkefni/Timaverkefni1.md#1-a%C3%B0-tengjast-raspberry-pi-15).

<!--
**Ath** Til að fá wifi líka heima og í skólanum þá þarftu að breyta `wpa_supplicant.conf` skránni, sjá [leiðbeiningar](https://github.com/VESM3/IOT/blob/main/Efni/wifi.md#automatic-switching-between-wifi-network). vistaðu skránna í  `/boot/ directory` á SD kortinu.
-->
