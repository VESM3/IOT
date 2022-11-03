## Vandamál sem komu upp:

### Verkefni 1

- RPi Zero portin eru frekar leiðinleg, þarf að jugga til aðeins til að fá ljós
- RPi3 skemmdist við skammhlaup, (töng í tvo pinna)

---

### Verkefni 2
- Notið hotspot í síma ef skólanet virkar ekki (gekk fínt).
- liður 2.2  
   - Passa að í seinna sýnidæminu er nota tómt bil í user og password.  
   - Ýta á reset takka á ESP32 og baud rate 115200 til að sjá ip-tölu.
   - nota punkt ekki kommu í vafranum fyrir ip töluna.
- liður 2.3
   - DHT sensor vandræði nota rétt lib (dht er kommentað út) 
   - passa að hafa ekki fleiri en eitt include með DHT.
   
---

### Verkefni 3
- gátum scannað eftir ip tölum
- ip tölur á TskoliVESM 10.20.48.XXX, Advanced ip scanner 10.201.48.1-10.201.49.254
- sumir komust ekki inná hostname pi@hostname.tskoli.vesm en ip gékk
- 3 nemendur fengu permission denied (publickey) á rpi. Það að hreinsa út eldra key úr tölvunni `$ ssh-keygen -R [hostname-or-IP]`
- port 22: Connection timed out. SSH lokað útaf firewall í tölvu [windows fix](https://www.windowscentral.com/how-open-port-windows-firewall) 2 nemendur lentu í þessu
- eigum eftir að prófa V3.2 með Eclipse Mosquitto via port 1883 - líklegast lokað skv. Aroni, komið í beiðni um að opna.
- ein fartölvan var að grilla RPi zero via usb tengi. 
- Allir að nota power adapter með RPi (5V)

---

### Verkefni 4

---

### Verkefni 5
