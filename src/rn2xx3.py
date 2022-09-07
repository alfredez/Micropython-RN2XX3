"""
                      [ RN2483 Library ]
    MicroPython library for RN2483 LoRaWAN transceiver
    This implementation is meant to be used on embedded devices that supports MicroPython.
    [-------------------------------------------------------]
    Version:
    [0.1]:
        + Changes:
            - Added compatibility for Raspberry Pi Pico
            - Added LoRaWAN configuration method
            - Added Command class

        + TODO:
            - Complete the RN2XX3 Class
            - Complete the Command class
            - Add error handling
            - Test ESP32 compatibility
            - Writing proper comments for classes and functions
"""
import binascii
from src.exceptions import HostError
import time
from src.Command import Command


class Lora:
    """Commands for RN2483 and RN2903 can be found in the product user guide by Microchip"""

    def __init__(self, connection=None):
        """ Class init, check if serial connection is open """
        self.connection = connection
        self.commands = Command(path='commands.json')

        self.activation = {
            "otaa": True,
            "deveui": None,
            "appeui": None,
            "appkey": None,
            "devAddr": None,
            "AppSKey": None,
            "NwkSKey": None,
            "joined": False
        }

        if self.connection is None:
            raise HostError

    def config_otaa(self, appkey, appeui):
        """ Configure Over The Air Authentication """
        self.activation['otaa'] = True
        self.activation['appeui'] = appeui
        self.activation['appkey'] = appkey
        cmd = self.commands

        deveui = self.execute(self.commands.sys_hweui())

        while len(deveui) != 16:
            deveui = self.execute(self.commands.sys_hweui())
            time.sleep_ms(10000)

        print("When using OTAA, register this DevEUI: {0}".format(deveui))
        self.activation['deveui'] = deveui

        response = {"deveui": None,
                    "appeui": None,
                    "appkey": None,
                    "TxoutputPower": None,
                    "ARD": None,
                    "AR": None,
                    "status": None}

        list_cmd = [
            cmd.mac_reset_band(),
            cmd.mac_deveui_set(self.activation['deveui']),
            cmd.mac_appeui_set(appeui),
            cmd.mac_appkey(appkey),
            cmd.mac_pwridx_set(1),
            cmd.mac_adr_set('off'),
            cmd.mac_autoreply_set('off'),
            cmd.mac_save()
        ]

        for x in list_cmd:
            self.execute(x)

        print('trying to join')
        while not self.activation['joined']:
            status = self.execute(cmd.mac_join("otaa"))
            if self.determine_response(status) is True:
                self.activation['joined'] = True
                break
            time.sleep_ms(5000)
        print("Successfully joined TTN")
        return response

    def config_abp(self, devAddr, AppSKey, NwkSKey):
        """ Configure Authentication By Personalisation."""
        self.activation['devAddr'] = devAddr
        self.activation['AppSKey'] = AppSKey
        self.activation['NwkSKey'] = NwkSKey
        cmd = self.commands

        response = {"devAddr": None,
                    "AppSKey": None,
                    "NwkSKey": None,
                    "TxoutputPower": None,
                    "ARD": None,
                    "AR": None,
                    "status": None}

        list_cmd = [
            cmd.mac_reset_band(),
            cmd.mac_devAddr_set(devAddr),
            cmd.mac_appSKey(AppSKey),
            cmd.mac_nwkSKey(NwkSKey),
            cmd.mac_pwridx_set(1),
            cmd.mac_adr_set('off'),
            cmd.mac_autoreply_set('off'),
            cmd.mac_save()]

        for x in list_cmd:
            self.execute(x)

        print('trying to join')
        while not self.activation['joined']:
            status = self.execute(cmd.mac_join("abp"))
            if self.determine_response(status) is True:
                self.activation['joined'] = True
                break
            time.sleep_ms(5000)
        print("Successfully joined TTN")
        return (response)

    def execute(self, command):
        print('command {0}'.format(command))
        ''' Passes and Executes command to device, returns devices response '''
        self.connection.write(bytes(str(command) + "\r\n", "utf-8"))
        time.sleep_ms(100)
        response = self.connection.readline()
        if response is None:
            return (None)
        response = response.decode("utf-8").strip("\r\n")
        print('execute respons command {0}'.format(response))
        return response

    def send(self, data):
        """ Send data """
        self.txUncnf(data)

    def txCnf(self, data):
        """Send data without confirmation"""
        buffer = self.encodeData(data)
        command = self.commands.mac_tx_cnf(1, buffer)
        self.txCommand(command)

    def txUncnf(self, data):
        """Send data without confirmation"""
        buffer = self.encodeData(data)
        command = self.commands.mac_tx_uncfn(1, buffer)
        self.txCommand(command)

    def txCommand(self, command):
        """Transmission Command"""
        send_succes = False
        retry = 0

        while not send_succes:
            if retry > 10 or send_succes == True:
                break
            response = self.execute(command)
            send_succes = self.determine_response(response)
            retry += 1

    def encodeData(self, data):
        """Encode data to hex"""
        encoded = bytes(data, 'utf-8')
        buffer = binascii.hexlify(encoded).decode('utf-8')
        return buffer

    def determine_response(self, response):
        if response == 'ok':
            time.sleep_ms(10000)
            transmission_response = self.connection.readline()
            transmission_response = transmission_response.decode("utf-8").strip("\r\n")
            print('oke t-response {0}'.format(transmission_response))

            if transmission_response == 'mac_tx_ok':
                return True
            elif transmission_response == 'mac_rx':
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
            self.activation['joined'] = False
            self.reconnect()
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

    def reconnect(self):
        if self.activation['otaa']:
            return self.config_otaa(self.activation['appkey'], self.activation['appeui'])
        elif not self.activation['otaa']:
            return self.config_abp(self.activation['devAddr'], self.activation['NwkSKey'], self.activation['AppSKey'])
