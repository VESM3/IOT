# Tímaverkefni 4 (9%) 

- M2M samskipti
- Einstaklingsverkefni

---

Machine to machine [(M2M)](https://en.wikipedia.org/wiki/Machine_to_machine) is direct communication between devices using any communications channel, including wired and wireless. M2M derives from telemetry technology and generally refers to data exchange between various devices (usually) through the Internet without human participation. See also [IoT vs M2M](https://www.avsystem.com/blog/iot-and-m2m-what-is-the-difference/)

---

### 4.1 Serial samskipti (via USB): RPi og Arduino (30%)
Lestu [Raspberry Pi Arduino Serial Communication – Everything You Need To Know](https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/) og fylgdu eftir tilraununum í greininni: 
1. Simple Serial communication from Arduino to Raspberry Pi
1. bidirectional Serial communication between Raspberry Pi and Arduino
1. Raspberry Pi Arduino Serial communication: Application example

#### Punktar
- Þú þarft að enable Serial og I2C í Raspberry Pi t.d. í terminal með `sudo raspi-config`.
- notaðu USB-USBmicro millistykki til að tengja saman tækin. 
- ekki tengja Arduion og RPi saman með Tx/Rx pinnum, þú þarft til þess 3.3V/5V level-shifter þar sem þessi tæki vinna á sitthvoru spennunni.
- til að finna SPI hardware port. Með Arduion tengt við RPi og í terminal keyrðu `ls /dev/tty*`  ACM með númeri líklegast `/dev/ttyACM0`
- skoðaðu [Python String encode()](https://www.programiz.com/python-programming/methods/string/encode) td. til að breyta unicode streng í bytes
- skoðaðu [pySerial](https://pythonhosted.org/pyserial/shortintro.html)

<!--
[BASICS OF UART COMMUNICATION](https://www.circuitbasics.com/basics-uart-communication/) 
Til umhugsunar:
   - UART notast við baud rate, hver er tilgangur þess.
   - Hvernig er UART frábrugðið SPI? 
-->

---

### 4.2 Serial samskipti (via USB): Arduino til RPi (20%)

Fylgdu eftir verklega [How to Connect and Interface a Raspberry Pi With an Arduino](https://maker.pro/raspberry-pi/tutorial/how-to-connect-and-interface-raspberry-pi-with-arduino) þ.e. láttu Arduino senda strenginn "Hello from Arduino" til Raspberry Pi. Raspberry Pi við móttöku prentar út strenginn og lætur LED blikka.

- Tutorial notar RPi GPIO.BOARD, notaðu frekar GPIO.ZERO
- Ef þú færð meldinguna `IndentationError: expected an indented block` þá þarftu að hreinsa til autt svæði (tab/enter) í python kóðanum
- Laga þarf kóðann í tutorialnum  Hér er lagfærður kóði með `decode()` og `strip()` notkun: 
```python
      while True:
        read_ser=ser.readline()
        msg = read_ser.decode('utf-8')   # To convert byte strings to Unicode, líka hægt að nota bytes.decode(read_ser)
        print(msg) 
        if(msg.strip()=="Hello From Arduino!"):
            blink(11)
```

Við notum `decode()` til að umbreyta bytes frá Arduion yfir í annað gagnatag. Við notum `strip()` til að losna við new line (\n).

<!-- Tilgangur: Að nota GPIO á RPi stýrt frá Arduino. -->

---

### 4.3 Remote GPIO (20%)
Að stýra RPi + GPIO yfir netið frá tölvu. 

1. Lestu vel og gerðu viðeigandi stillingar skv. [Configuring Remote GPIO](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html#configuring-remote-gpio) þannig að þú getur stýrt RPi frá tölvunni þinni, notaðu VSCode ritilinn.  
2. Láttu LED blikka með eftifarandi kóða [4.4. Pin factories](https://gpiozero.readthedocs.io/en/stable/remote_gpio.html#pin-factories)

---

### 4.4 Remote GPIO - tveir nemendur saman (30%)

1. Framkvæmið [tilraun 5.1](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#led-button) með tvo RPi.
1. Framkvæmið [tilraun 5.2](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#led-2-buttons) með tvo RPi og tölvu.
1. **Bónus:** Framkvæmið [tilraun 5.4](https://gpiozero.readthedocs.io/en/stable/recipes_remote_gpio.html#multi-room-doorbell) nokkrir nemendur saman.

---

## Námsmat
- Yfirferð á sér stað í tíma.
- Fyrir hvern lið: Fullt fyrir fullnægjandi útfærslu, hálft ef lausn er ábótavant og ekkert ef lausn er stórlega ábótavant eða vantar.
- Skilaðu á Innu vefslóð kóðalausnir af tilraunum.
