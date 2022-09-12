"""
                      [ RN2XX3 Library ]
    MicroPython library for RN2483 and RN2903 LoRaWAN module
    This implementation is meant to be used on embedded devices that supports MicroPython.
    [-------------------------------------------------------]
    Version:
    [1.0]:
        + Changes:
            - Added compatibility for Raspberry Pi Pico & ESP32
            - Added LoRaWAN configuration method
            - Added Command class
            - Wrote proper comments for classes and functions

        + TODO
            - Test compatibility with ESP8223
"""
from binascii import hexlify, unhexlify
import time
from src.Command import Command


class RN2xx3:
    """MicroPython library to communicate with the Microchip RN2483 and RN2903 module using a simple UART interface"""

    def __init__(self, connection):
        """
        Construct a RN2xx3 object representing the module

        Args:
            connection (UART): UART object of where the module is connected
        """
        self.connection = connection

        # Access to all commands from Command class
        self.commands = Command(path='src/commands.json')

        # Dictonary to store activation settings
        self.activation = {}

    def config_otaa(self, appeui: str, appkey: str) -> bool:
        """
        Configure Over The Air Authentication

        Args:
            appkey (str): 16-byte hexadecimal number representing the application key
            appeui (str): 8-byte hexadecimal number representing the application EUI

        Returns:
            joined (bool): bool value representing if the join procedure was successful

        """
        # Storing activation settings
        self.activation['otaa'] = True
        self.activation['appeui'] = appeui
        self.activation['appkey'] = appkey
        self.activation['joined'] = False

        # get hweui, otherwise try untill successful
        deveui = self.execute(self.commands.sys_get_hweui())

        while len(deveui) != 16:
            deveui = self.execute(self.commands.sys_get_hweui())
            time.sleep_ms(10000)

        print("When using OTAA, register this DevEUI: {0}".format(deveui))
        self.activation['deveui'] = deveui

        # Creating a list of commands to configure the module
        list_cmd = [
            self.commands.mac_reset_band(868),
            self.commands.mac_set_deveui(self.activation['deveui']),
            self.commands.mac_set_appeui(appeui),
            self.commands.mac_set_appkey(appkey),
            self.commands.mac_set_pwridx(1),
            self.commands.mac_set_adr('off'),
            self.commands.mac_set_autoreply('off'),
            self.commands.mac_save()
        ]

        # Executing all the commands
        for x in list_cmd:
            self.execute(x)

        # Try to join the network
        print('Trying to join')
        while not self.activation['joined']:
            status = self.execute(self.commands.mac_join("otaa"))
            if self.determine_response(status) is True:
                self.activation['joined'] = True
                break
            time.sleep_ms(5000)
        print("Successfully joined TTN")
        return self.activation['joined']

    def config_abp(self, devAddr: str, AppSKey: str, NwkSKey: str) -> bool:
        """
        Configure Authentication By Personalisation

        Args:
            devAddr (str): 4-byte hexadecimal number representing the device address
            AppSKey (str): 16-byte hexadecimal number representing the application session key
            NwkSKey (str): 16-byte hexadecimal number representing the network session key

        Returns:
            joined (bool): bool value representing if the join procedure was successful
        """

        # Storing activation settings
        self.activation['otaa'] = False
        self.activation['devAddr'] = devAddr
        self.activation['AppSKey'] = AppSKey
        self.activation['NwkSKey'] = NwkSKey
        self.activation['joined'] = False

        # Creating a list of commands to configure the module
        list_cmd = [
            self.commands.mac_reset_band(868),
            self.commands.mac_set_devaddr(devAddr),
            self.commands.mac_set_appskey(AppSKey),
            self.commands.mac_set_nwkskey(NwkSKey),
            self.commands.mac_set_pwridx(1),
            self.commands.mac_set_adr('off'),
            self.commands.mac_set_autoreply('off'),
            self.commands.mac_save()
        ]

        # Executing all the commands
        for x in list_cmd:
            self.execute(x)

        # Try to join the network
        print('trying to join')
        while not self.activation['joined']:
            status = self.execute(self.commands.mac_join("abp"))
            if self.determine_response(status) is True:
                self.activation['joined'] = True
                break
            time.sleep_ms(5000)
        print("Successfully joined TTN")
        return self.activation['joined']

    def execute(self, command: str) -> str:
        """
        Passes the command to the device to be executed. Upon successful reception a command,
        based on the specific command the module will respond.
        For more info read the user's guide (Chapter 2.2 Command Organization)

        Args:
            command (str): Example: mac tx uncnf 1 23A5

        Returns:
            response (str): Response from the module; Example: ok
        """
        print('executing command {0}'.format(command))

        # Write the command to the module
        self.connection.write(bytes(str(command) + "\r\n", "utf-8"))
        time.sleep_ms(100)

        # Read the response from the module
        response = self.connection.readline()
        if response is None:
            return ''

        # Decode the response
        response = response.decode("utf-8").strip("\r\n")
        print('response module {0}'.format(response))
        return response

    def send(self, data):
        """
        Function to pass the data to the transmission function, which can be (un)confirmed

        Args:
            data (str): Data that needs to be transmitted
        """
        self.txUncnf(data)

    def txCnf(self, data):
        """
        Send data with confirmation

        Encode the data and prepare the command to be passed to the module

        Args:
            data (str): Data that needs to be transmitted
        """
        port_number = 1
        buffer = self.encodeData(data)
        command = self.commands.mac_tx_cnf(port_number, buffer)
        self.txCommand(command)

    def txUncnf(self, data):
        """
        Send data without confirmation

        Encode the data and prepare the command to be passed to the module

        Args:
            data (str): Data that needs to be transmitted
        """
        port_number = 1
        buffer = self.encodeData(data)
        command = self.commands.mac_tx_uncfn(port_number, buffer)
        self.txCommand(command)

    def txCommand(self, command):
        """
        Try to transmit the command and determine the result

        Args:
            command (str): Example: mac tx uncnf 1 23A5
        """
        send_succes = False
        retry = 0

        while not send_succes:
            if retry > 10 or send_succes == True:
                break
            response = self.execute(command)
            send_succes = self.determine_response(response)
            retry += 1

    def encodeData(self, data):
        """
        Convert the data into a hexadecimal number representing

        Args:
            data (str): Data that needs to be transmitted

        Returns:
            buffer (str): A hexadecimal number representation of the data
        """
        encoded = bytes(data, 'utf-8')
        buffer = hexlify(encoded).decode('utf-8')
        return buffer

    def decodeData(self, rx_data):
        """
        Convert the received hexadecimal number representing data into a string readable for user's and print the result

        Args:
            rx_data (str): The received hexadecimal number representing data
        """
        data = unhexlify(rx_data).decode('utf-8')
        print(data)

    def determine_response(self, response):
        """
        After transmitting, determine the response received from the module.
        For more info read the user's guide (Chapter 2.2 Command Organization)

        Args:
            response (str): Response from the device

        Returns:
            (bool): bool value representing if the transmission was successful
        """
        if response == 'ok':
            time.sleep_ms(10000)
            transmission_response = self.connection.readline()
            transmission_response = transmission_response.decode("utf-8").strip("\r\n")
            print('oke t-response {0}'.format(transmission_response))

            if transmission_response == 'mac_tx_ok':
                return True
            elif 'mac_rx' in transmission_response:
                rx_data = transmission_response.rsplit(" ")[2]
                self.decodeData(rx_data)
                return True
            elif transmission_response == 'mac_err':
                # init()
                return False
            elif transmission_response == 'invalid_data_len':
                return True
            elif transmission_response == 'radio_tx_ok':
                return True
            elif transmission_response == 'radio_err':
                # init()
                return False
            elif transmission_response == 'accepted':
                return True
            elif transmission_response == 'busy':
                return False
            else:
                return False

        elif response == 'invalid_param':
            return False
        elif response == 'not_joined':
            self.rejoin()
            return False
        elif response == 'no_free_ch':
            return False
        elif response == 'silent':
            return False
        elif response == 'frame_counter_err_rejoin_needed':
            return False
        elif response == 'busy':
            time.sleep_ms(1000)
            return False
        elif response == 'mac_paused':
            return False
        elif response == 'invalid_data_len':
            time.sleep_ms(1000)
            return True
        else:
            return False

    def rejoin(self):
        """
        When the module is not joined to the network anymore, try to reconnect.

        Returns:
            joined (bool): bool value representing if the join procedure was successful
        """
        if self.activation['otaa']:
            return self.config_otaa(self.activation['appkey'], self.activation['appeui'])
        else:
            return self.config_abp(self.activation['devAddr'], self.activation['NwkSKey'], self.activation['AppSKey'])

    def serial_info(self):
        """
        Returns:
            Serial connection info
        """
        return self.connection

    def serial_close(self):
        """
        Turn off the UART bus.
        """
        self.connection.deinit()
