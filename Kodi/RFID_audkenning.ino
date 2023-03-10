
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN  5  // ESP32 pin GIOP5 
#define RST_PIN 27 // ESP32 pin GIOP27 
MFRC522 mfrc522(SS_PIN, RST_PIN);

void setup(){
        Serial.begin(9600);
        SPI.begin();
        mfrc522.PCD_Init();
}

void loop(){

        //here we have to wait for the card, when it is near to the sensor
        if ( ! mfrc522.PICC_IsNewCardPresent()){
        return;
        }

        //we can read it's value
        if ( ! mfrc522.PICC_ReadCardSerial()) {
        return;
        }
        
        String content= "";
        for (int i = 0; i < mfrc522.uid.size; i++) {
                Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
                Serial.print(mfrc522.uid.uidByte[i], HEX);
            content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
            content.concat(String(mfrc522.uid.uidByte[i], HEX));
        }
        content.toUpperCase();
        content = content.substring(1);
        
        // change UID
        if(content == "B3 8B EE A3"){
            Serial.println("Já");
        }else{
            Serial.println("Nei");
        }
        Serial.println();
}
