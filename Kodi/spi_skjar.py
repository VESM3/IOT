from machine import Pin, SPI
from ssd1306 import SSD1306_SPI

# --- Pin connections (change numbers to match your board!) ---
SCK_PIN = 13     # connects to display SCL
MOSI_PIN = 14    # connects to display SDA
CS_PIN = 5       # CS
DC_PIN = 16      # DC
RST_PIN = 17     # RES

# Display size
WIDTH = 128
HEIGHT = 64

# Initialize SPI
spi = SPI(1,
          baudrate=10000000,
          polarity=0,
          phase=0,
          sck=Pin(SCK_PIN),
          mosi=Pin(MOSI_PIN),
          miso=Pin(19))

cs = Pin(CS_PIN, Pin.OUT)
dc = Pin(DC_PIN, Pin.OUT)
rst = Pin(RST_PIN, Pin.OUT)

display = SSD1306_SPI(WIDTH, HEIGHT, spi, dc, rst, cs)
