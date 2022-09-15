from machine import UART
from src.rn2xx3 import RN2xx3 as RN2483

ApplicationEUI = "INSERT APPEUI"
ApplicationKey = "INSERT APPKEY"

# Initialize serial connection for ESP32
uart = UART(2, baudrate=57600, tx=17, rx=16)

# Initialize module
module = RN2483(connection=uart)

# Configure module
module.config_otaa(appeui=ApplicationEUI, appkey=ApplicationKey)

# Transmit a message
module.send("Hello world")

# Close serial connection
module.serial_close()
