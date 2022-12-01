### Rafmagnsþörf
- 64x64 can draw up to 7.68A so you will want to be using a 5V @ 10A power supply with this device.
- Each pixel can draw up to 0.06 Amps each if on full white. The total max per panel is thus 64 * 0.06 = 3.95 Amps or 128 * 0.06 = 7.68 Amps

### Söfn C++ (pyhon líka hægt en slow)
- [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix)
   - [video-viewer, láta LED Matrix skjáinn spila myndband](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/utils/video-viewer.cc)
   - [minimal-example.cc](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/examples-api-use/minimal-example.cc) grunnur til að kóða sitt eigið

### Tutorials
- [Make a Massive 4096 LED Display for Retro Pixel Art](https://www.instructables.com/Make-a-Massive-4096-LED-Display-for-Retro-Pixel-Ar/)
- [64x64 RGB LED Matrix - 2.5mm Pitch - 1/32 Scan](https://www.adafruit.com/product/3649)
- (skoða betur [Homemade Video Game Console](https://www.electromaker.io/project/view/homemade-video-game-console-powered-by-arduino))

### Nemaverkefni unnin með 64x64
- [Pong með Leapmotion + 4 x 64LEDMatrix](https://github.com/Anton-Benediktsson/VESM3-V8) Anton og Þórhallur  _VOR 2022_
- [Snake](http://tolvubraut.is/FORR3FV-Haust19-LEDMatrixSnake/) _Haust 2019_
   - [Github](https://github.com/tolvubraut/FORR3FV-Haust19-LEDMatrixSnake)
   - [snake kóðinn í C++](https://github.com/VESM3/Kennarar/blob/master/Ihlutir/Code/snake.cc)
- [64x64 LEDMatrix með veðurþjónustu (tími og hiti)](https://github.com/RafalRo/VESM3) Rafal og Valdimar, reyndu líka við gyro 
- [Arcade](http://tolvubraut.is/FORR3FV-Vor19-ArcadePi/)
   - ffmpeg screen capture til að displaya á matrixið
   - búa til custom pixel mapper
- [Sandtoy](http://tolvubraut.is/FORR3FV-Haust19-LEDMatrixToy/)
  - [Github](https://github.com/tolvubraut/FORR3FV-Haust19-LEDMatrixToy) 
  - fylgt eftir [Raspberry Pi LED Matrix Sand Toy](https://learn.adafruit.com/matrix-led-sand) 

