
## Tímaverkefni 5 (35%) 
- Einstaklingsverkefni 

---

### Verkefnalýsing: Pottaplanta.

Verkefnið er í grunninn að sinna pottaplöntu með notkun skynjara fyrir mælingar og IoT til að fylgjast með líðan hennar. 
Við notum [jarðvegsmælir](https://github.com/VESM3/IOT/blob/main/Efni/soilsensor.md) (e. soil sensor) til að kanna rakastig jarðveg 
svo við getum áttað okkur hvenær við þurfum að vökva plöntuna, [hitamælir](https://github.com/microsoft/IoT-For-Beginners/blob/main/2-farm/lessons/1-predict-plant-growth/README.md) 
og ljósnema til að kanna birtuþörf plöntunar. Við kveikjum á gróðurlampa (led pera) við ákveðin skilyrði og setjum [sjálfvirka vökvun](https://github.com/microsoft/IoT-For-Beginners/blob/main/2-farm/lessons/3-automated-plant-watering/README.md) 
af stað ef jarðvegsmælir gefur tilefni til þess. 
Sjá [sýnidæmi](https://learn.adafruit.com/pyportal-pet-planter-with-adafruit-io/overview)

---

### Verkþættir sem þarf að uppfylla:

1. Unnið er með skynjara (raki í jarðvegi, hitastig og ljósnema) til að greina upplýsingar úr umhverfinu (ESP32).
1. Gögn eru send frá inntaki og send til MQTT Broker (RPi).
1. Stýringar fyrir vökvastjórnun (solenoid). 
1. Notað er server kóði til að stýra tengdum úttaksbúnaði (kveikja á LED og vökvastjórnun) útfrá birtu- og rakaskilyrðum.
1. Notað er vefþjónusta (IFTTT) til að tilkynna notanda þegar stýring eiga sér stað (sími).
1. Unnið er með vefviðmót fyrir birtingu gagna (vefsíða).
1. Samsettning á IoT búnaði (innfeld kerfi, vélbúnaður, tæki, skynjarar, íhlutir, brauðbretti, vírar osfrv.) er með besta móti.

---

### Verkefnaskil og skýrsla

Skilaðu hlekk á lokaða (e. private) Github geymslu á Innu sem inniheldur eftirfarandi:

1. Allur kóði, skrár og gögn.
1. Skýrsla (í readme.md) sem inniheldur:
   1. verkefnalýsing ásamt Kerfis skýringarmynd og efnislista.
   1. ljósmyndir af samsettningu á IoT búnað. 
   1. tengil á myndband (youtube) af notkun og virkni frumgerðar.
   1. tengla á kóðaskrár
   1. rafrásarteikning [Circuit Diagram](https://www.circuit-diagram.org/) eða [TinkerCad Circuit](https://www.tinkercad.com/circuits) af tengingum íhluta.   1. ljósmyndir af samsettningu á IoT búnað og tilraunum. 
   1. dagbók, hvað var gert og hvenær.
 
Hugaðu vel að uppsetningu og framsetningu á skýrslu! 

---

## Námsmat
Skil á skýrslu er forsenda þess að gefin sé einkunn fyrir verkefnið. <br>
Einkunn byggir á vinnuframlagi sem á sér stað í kennslustund ásamt útfærslu á verkþáttum: 

1. Inntak (mælingar) (20%)
   -  Mælt er birtu-, hita- og jarðvegsrakastig.
1. Úttaksbúnaður (actuator) (20%)
   - Vökvun með solenoid.
   - kveikt er á gróðurlampa.
1. Stýringar (server kóði) (20%)
   - Kveikt er á vökvun ef jarðvegsrakastig fer niður fyrir ákveðin mörk. 
   - Kveikt og slökkt er á gróðulampa (LED) útfrá birtuskilyrðum.
1. Viðmót. (20%)
   - Viðmót sýnir nýjustu mælingar; jarðvegsraka, hita og birtustig. 
1. Vefþjónusta (10%)
   - Notað er IFTTT vefþjónusta
1. Samsettning á IoT búnaði (10%)
   - Samsettning á IoT búnaði (innfeld kerfi, vélbúnaður, tæki, skynjarar, íhlutir, brauðbretti, vírar osfrv.) er með besta móti.


**Fyrir hvern lið:** Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar. <br>
**Vinnuframlag:** Fyrir hverja kennslulotu (2 klst) í skóla sem nemandi mætir **ekki**, dregst **1** frá einkunn hjá viðkomandi. <br>


