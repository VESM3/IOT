
### 1. Uppsetning á [RPi OS stýrikerfi  á microSD kort og usb lykli í tölvunni þinni 
   1. Settu upp [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
   1. Settu upp RPi OS með RPi Imager, sjá [myndband](https://www.youtube.com/watch?v=ntaXWS8Lk34), 
       - veldu 32-bita útgáfuna af RPi OS, 
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

**Ath** Til að fá wifi heima og í skólanum þá getur þú breytt wpa_supplicant.conf skránni eftirá, sjá [leiðbeiningar](https://github.com/VESM3/IOT/blob/main/Efni/wifi.md)
