
#### Wifi stillingar
`wpa_supplicant.conf` file is placed into the /boot/ directory, this will be moved to the `/etc/wpa_supplicant/` directory the next time the system is booted, overwriting the network settings. This allows a Wifi configuration to be preloaded onto a card from a Windows or other machine that can only see the boot partition.

- [Edit the file in /etc/wpa_supplicant directly on RPi ](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis#edit-the-file-in-slash-etc-slash-wpa-supplicant-3015510-9)

---

#### Wifi í skólanum

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=IS
network={
    ssid="Taekniskolinn"
    key_mgmt=NONE
}
```

---

#### Automatic switching between wifi network

The priority works that higher number connects first if both are in range.

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

---

