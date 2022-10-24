
### Til að geta tengst RPi Zero með Ethernet yfir USB (virkar bara með Pi Zero)
Það þarf að gera eftirfarandi stillingar á microSD kortinu **áður** en þú notar RPi Zero W. Leiðbeiningar [myndband](https://youtu.be/XaTmG708Mss?t=185) og [vefgrein](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html#direct-usb-connection-pi-zero-zero-w-only),

1. settu usb lykilm með SD kortinu í tölvuna og opnaðu drif sem heitir `boot`.
1. Opnaðu skránna `config.txt` sem er í rótinni á microSD kortinu,
1. Bættu við `dtoverlay=dwc2` í enda skráarinnar og vistaðu skránna.
1. Opnaðu næst `cmdline.txt` og bættu við textanum ` modules-load=dwc2,g_ether` eftir orðinu `rootwait` það á að vera autt bil á milli og vistaðu skránna.
1. Settu microSD kortið í RPi Zero
1. Tengdu micro USB kapal við USB portið á RPi Zero (ekki PWR portið). _Við þetta keyrir `firstrun.sh` skrá á RPi_
1. **Ef Windows** Ef tölvan sér ekki RPi þá þarftu líklegast networkdriver, sjá [leiðbeiningar (myndband)](https://youtu.be/XaTmG708Mss?t=415)
   1. [USB Ethernet adapter Driver (rndis)](https://www.catalog.update.microsoft.com/Search.aspx?q=USB+RNDIS+Gadget)  
   1.  sjá optional drivers í windows update og veldu þar driverinn sem á að uppfæra
1. Til að tölvan leyfir þér að nota SSH í localhost, download and install [Bonjour Print Services](https://support.apple.com/kb/DL999?viewlocale=en_US&locale=en_US) from apple.com (if you have Windows)
1. Núna getur þú notað SSH til að stýra RPi (sjá næsta lið).
