from machine import UART, Pin
from src.rn2xx3 import RN2xx3 as RN2483

ApplicationEUI = "INSERT APPEUI"
ApplicationKey = "INSERT APPKEY"

# Initialize serial connection for Raspberry Pi Pico
uart = UART(0, baudrate=57600, tx=Pin(0), rx=Pin(1))

# Initialize module
module = RN2483(connection=uart)

# Configure module
module.config_otaa(appeui=ApplicationEUI, appkey=ApplicationKey)

# Transmit a message
module.send("Hello")

# Close serial connection
module.serial_close()
