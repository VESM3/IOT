## Tímaverkefni 5 

- IoT frumgerð 
- 35% af heildareinkunn  
  
---

### Verkefnalýsing

Lokaverkefnið snýr að IoT frumgerðasmíð þar sem ýmis tæki og íhlutir eru notuð. Unnið er með samþætting tækja og hugbúnaðar tengda netinu sem geta greint gögn og upplýsingar úr umhverfinu, miðlað þeim og stýrt tengdum úttaksbúnaði. 
<br>
Viðfangefnið verkefnis og útfærsla er frjáls en er **háð samþykki kennara** og þarf að uppfylla ákveðna verkþætti (sjá neðar). <br>
Verkefnið þarf að vera ykkar eigið og gert er ráð fyrir sjálfstæðum vinnubrögðum.
Skoðið [Adafruit](https://learn.adafruit.com/category/internet-of-things-iot?guide_page=2&total_count=224&total_verbiage=total+series-), [Makerpro](https://maker.pro/projects/category/iot?filter=popular), [Hackster](https://www.hackster.io/iot/projects) fyrir innblástur og hugmyndir

> [listi af íhlutum](https://github.com/VESM3/IOT/blob/main/Ihlutir.md) sem skólinn á (ekki tæmandi).

#### Verkþættir sem þarf að uppfylla:

- Unnið er með innfelld kerfi; ESP32 og/eða Raspberry Pi.
- Telemetry. Unnið er með inntak frá skynjurum (greint upplýsingar úr umhverfinu).
- Actuators: Unnið er með stýringar.
- IoT Protocol: MQTT eða ESP-NOW. 
- Unnið er úr gögnum (server forritun).
- Viðmót (vefsíða) fyrir birtingu gagna (mælaborð).
- Vefþjónusta; IFTTT.
- IoT hönnun; kerfisskýringarmynd, rafrásarteikning.
- Samsettning á IoT búnaði (innfelld kerfi, vélbúnaður, íhlutir, brauðbretti, vírar osfrv.).
- Skýrsla á Github (readme.md).
- Valkvæmt:
  - notendastýring.
  - gagnagreining.
    
<!--
  - 2D/3D hönnunarteikningar.
  - Smíði IoT frumgerðar (veróborðsmíði, lóðun og 2D/3D samsettning).
-->

<!--
MQTT Dashboard með 
- [Node-RED](https://nodered.org/)
- [Access Node-RED Dashboard from Anywhere using Digital Ocean](https://randomnerdtutorials.com/access-node-red-dashboard-anywhere-digital-ocean/)  
- [Getting Started with Node-RED Dashboard on Raspberry Pi](https://randomnerdtutorials.com/getting-started-node-red-dashboard/)  
-->

---

### Verkefnaskil og skýrsla

Skilið hlekk á Github geymslu á Innu sem inniheldur eftirfarandi:

- Allur kóði, skrár og gögn.
- Skýrsla ( í readme.md ) sem inniheldur:
  - verkefnalýsing, efnislisti, hvað var gert og heimildir.
  - kerfisskýringarmynd. [dæmi](https://github.com/VESM3/IOT/blob/main/Myndir/kerfismynd.drawio.png)
  - rafrásarteikning [Circuit Diagram](https://www.circuit-diagram.org/) eða [TinkerCad Circuit](https://www.tinkercad.com/circuits) af tengingum íhluta.
  - tenglar á kóðaskrár með skýringum.
  - ljósmyndir af samsettningu á IoT búnað. 
  - myndband af notkun og virkni frumgerðar.
<!--
  _valkvæmt: Hönnunarteikningar (til prentunar) 2d og eða 3d teikningar og model (.stl skráin)._
-->
Hugið vel að uppsetningu og framsetningu á skýrslu! 

> [leiðbeiningar: Að búa til skýrslu í markdown](https://github.com/VESM1VS/AFANGI/blob/main/Kennsluefni/skyrslugerd.md)

---

### Námsmat 
Skil á skýrslu er forsenda þess að gefin sé einkunn fyrir verkefnið. <br>
Einkunn byggir á vinnuframlagi sem á sér stað í kennslustund ásamt útfærslu á verkþáttum: 

1. Inntak (telemetry) með MQTT eða ESP-NOW **(25%)**
1. Stýringar (actuator) með MQTT eða ESP-NOW. **(25%)**
1. Serverkóði og vefþjónustur. **(25%)**
1. Viðmót/mælaborð (vefsíða); birting gagna (og notendainntak). **(25%)**
<!--
1. Skýrsla, hönnun, samsettning (og smíði) IoT frumgerðar. **(20%)**
-->
Einkunn fyrir hvern lið: 
- 4/4 lausn er vel útfærð.
- 3/4 lausn er smávægilega ábótavant (vantar smá upp á).
- 2/4 lausn er ábótavant, helmingur er vel útfærður.
- 1/4 lausn er stórlega ábótavant, tíma og kóðavinna lögð í lausn.
- 0/4 lausn vantar eða óunnin.

**Vinnuframlag:** Fyrir hverja kennslulotu (2 x 50 mín) í skóla sem nemandi mætir **ekki** dregst **1** frá einkunn hjá viðkomandi. 
