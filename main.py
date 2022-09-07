from machine import UART, Pin
from src import rn2xx3

ApplicationEUI = "INSERT APPEUI"
ApplicationKey = "INSERT APPKEY"

'''
Initialize serial connection for Raspberry Pi Pico
'''
uart = UART(0, baudrate=57600, tx=Pin(0), rx=Pin(1))

# Initialize transceiver
device = rn2xx3.Lora(connection=uart)

print(device.config_otaa(appkey=ApplicationKey, appeui=ApplicationEUI))

device.send("Hello")
print("End")
