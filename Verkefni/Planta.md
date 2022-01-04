
## Tímaverkefni 8 (35%) 
- Einstaklingsverkefni 

---

### Verkefnalýsing: Pottaplanta.

Verkefnið er í grunninn að sinna pottaplöntu með notkun skynjara fyrir mælingar og IoT til að fylgjast með líðan hennar. 
Við notum [jarðvegsmælir](https://github.com/VESM3/IOT/blob/main/Efni/soilsensor.md) (e. soil sensor) til að kanna rakastig jarðveg svo við getum áttað okkur hvenær við þurfum að vökva plöntuna, [hitamælir](https://github.com/microsoft/IoT-For-Beginners/blob/main/2-farm/lessons/1-predict-plant-growth/README.md) og ljósnema til að kanna birtuþörf plöntunar. Við kveikjum á gróðurlampa (led pera) við ákveðin skilyrði og setjum [sjálfvirka vökvun](https://github.com/microsoft/IoT-For-Beginners/blob/main/2-farm/lessons/3-automated-plant-watering/README.md) af stað ef jarðvegsmælir gefur tilefni til þess. Sjá [sýnidæmi](https://learn.adafruit.com/pyportal-pet-planter-with-adafruit-io/overview)

---

### Verkþættir sem þarf að uppfylla:

1. Unnið er með skynjara (raki í jarðvegi, hitastig og ljósnema) til að greina upplýsingar úr umhverfinu.
1. Gögn eru send frá inntaki með ESP32 (eða Arduino og RPi) og send til Adafruit IO.
1. Unnið er með vefviðmót fyrir birtingu gagna (Dashboard í Adafruit IO).
1. Stýringar, unnið er með Triggers frá Adafruit IO fyrir vökvastjórnun.
1. Notað er vefþjónusta (IFTTT) til að stýra tengdum úttaksbúnaði (kveikja á LED) útfrá birtuskilyrðum.
1. Samsettning á IoT búnaði (innfeld kerfi, vélbúnaður, tæki, skynjarar, íhlutir, brauðbretti, vírar osfrv.) er með besta móti.

---

### Verkefnaskil og skýrsla

Skilaðu hlekk á lokaða (e. private) Github geymslu á Innu sem inniheldur eftirfarandi:

1. Allur kóði, skrár og gögn.
1. Skýrsla (í readme.md) sem inniheldur:
   1. verkefnalýsing ásamt skýringarmyndum og efnislista.
   1. tengil á myndband (youtube) af notkun og virkni frumgerðar.
   1. tengla á kóðaskrár
   1  rafrásarteikning t.d með [Circuit Diagram](https://www.circuit-diagram.org/).
   1. ljósmyndir af samsettningu á IoT búnað og tilraunum. 
   1. dagbók, hvað var gert og hvenær.
 
Dæmi um framsetning á skýrslu er að finna hjá [instructables](https://www.instructables.com/How-to-Write-an-Instructable-Class/) eða [Project Hub](https://create.arduino.cc/projecthub/Arduino_Genuino/how-to-submit-content-on-arduino-project-hub-cf2177)

---

## Námsmat
Einkunn byggir á vinnuframlagi sem á sér stað í kennslustund ásamt eftirfarandi: 

1. Inntak (mælingar) (20%)
   -  Mælt er birtu-, hita- og jarðvegsrakastig.
1. Viðmót í Adafruit IO. (20%)
   - Viðmót sýnir nýjustu mælingar; jarðvegsraka, hita og birtustig sem og þróunina á hita og jarðvegsraka yfir tíma (línurit), 
1. Stýringar (20%)
   - Notað er Reactive trigger til að kveikja á vökvun ef jarðvegsrakastig fer niður fyrir ákveðin mörk.
1. Vefþjónusta (20%)
   - Notað er IFTTT vefþjónustu til að ákveða hvenær best er að kveikja og slökkva á gróðurlampa (LED) t.d. útfrá birtuskilyrðum t.d. ljósaskipti, veðri, sólargang.
1. Samsettning á IoT búnaði (20%)
   - Samsettning á IoT búnaði (innfeld kerfi, vélbúnaður, tæki, skynjarar, íhlutir, brauðbretti, vírar osfrv.) er með besta móti.
   - Veróborðsmíð er til fyrirmyndar, lóðun og lengd víra eru hóflegir og skipulagðir.

<br>

**Fyrir hvern lið:** Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar. <br>
**Vinnuframlag:** Fyrir hverja kennslulotu (4 klst) í skóla sem nemandi mætir **ekki**, dregst **2.5** frá einkunn hjá viðkomandi. <br>


