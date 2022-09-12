# Raspberry Pi Pico - RN2483
[Quick reference for the RP2](https://docs.micropython.org/en/latest/rp2/quickref.html)<br>
In this example it is shown how to send "Hello world" to [The Things Stack](https://www.thethingsindustries.com/docs/getting-started/),
with a Raspberry Pi Pico and SODAQ LoraBee. LoraBee is a BEE formfactor board with the Microchip RN2483 LoRaWAN module.

This [link](https://www.thethingsindustries.com/docs/devices/adding-devices/) contains instructions for adding devices on The Things Stack.
# Serial connection
|     | Pico     |     | LoraBee |
|-----|----------|-----|---------|
| VDD | 3V3(OUT) | ->  | 3.3V    |
| GND | GND      | ->  | GND     |
| TX  | GP0      | ->  | RX      |
| RX  | GP1      | ->  | TX      |
# Implementation
## Import and initialize modules
```python
from machine import UART, Pin
from src.rn2xx3 import RN2xx3 as RN2483

ApplicationEUI = "INSERT APPEUI"
ApplicationKey = "INSERT APPKEY"

# Initialize serial connection for Raspberry Pi Pico
uart = UART(0, baudrate=57600, tx=Pin(0), rx=Pin(1))

# Initialize module
module = RN2483(connection=uart)
```
## End Device Activation method
Every end device must be registered with a network before sending and receiving messages. This procedure is known
as activation. There are two activation methods available:

- Over-The-Air-Activation (OTAA) - the most secure and recommended activation method for end devices. Devices perform 
a join procedure with the network, during which a dynamic device address is assigned and security keys are negotiated with the device.

- Activation By Personalization (ABP) - requires hardcoding the device address as well as the security keys 
in the device. ABP is less secure than OTAA and also has the downside that devices can not switch network providers without manually changing keys in the device.
Configure - Over The Air Authentication

For more information about activation, please read it on [The Things Network](https://www.thethingsnetwork.org/docs/lorawan/end-device-activation/)

```python
# Configure module
module.config_otaa(appeui=ApplicationEUI, appkey=ApplicationKey)
```

Configure - Authentication By Personalization

```python
# Configure module
module.config_abp(devaddr=DeviceAddress, appskey=ApplicationSessionKey, nwskey=NetworkSessionKey)
```

## Transmission
After successfully joined the network, it is possible to transmit data with the following function.
```python
# Transmit a message
module.send("Hello world")
```
At your end device on The Things Stack, you can setup a "Custom Javascript formatter" in the tab "Payload formatters".
The JavaScript [decodeUplink()](https://www.thethingsindustries.com/docs/integrations/payload-formatters/javascript/uplink/) function is called when a data uplink message is received from a device. 
This function decodes the binary payload received from the end device to a human-readable JSON object that gets send upstream to the application.
```json
function decodeUplink(input) {
  return {
    data: {
      Message: String.fromCharCode(...input.bytes)
    },
    warnings: [],
    errors: []
  };
}
```
![Decoded-uplink](/home/alfred/PycharmProjects/Micropython-RN2483/Images/decoded-uplink.png)
