"""
                      [ Command Class ]
    Commands for RN2483 and RN2903 can be found in the product user guide by Microchip:

    "RN2483 LoRa® Technology Module Command Reference User’s Guide"
    https://ww1.microchip.com/downloads/en/DeviceDoc/RN2483-LoRa-Technology-Module-Command-Reference-User-Guide-DS40001784G.pdf

    "RN2903 LoRa® Technology Module Command Reference User’s Guide"
    https://ww1.microchip.com/downloads/en/DeviceDoc/RN2903%20LoRa%20Technology%20Module%20Command%20Reference%20User%20Guide-40001811B.pdf

    [-------------------------------------------------------]
    Version:
    [0.1]:
        + Changes:
            - Added command set dictionary
            - Added basic functions with commands for LoRaWAN configuration method in RN2xx3 class

        + TODO:
            - Expand the Command class based on the user guide
            - Writing proper comments for functions

"""
from json import load


class Command:

    def __init__(self, path=None):
        command_file = open(path)
        self.commands = load(command_file)

    def sys_hweui(self):
        return self.commands["SYSTEM"]["HWEUI"]

    def mac_deveui_set(self, deveui):
        return self.commands["MAC"]["DEVEUI"]['SET'].format(deveui)

    def mac_appeui_set(self, appeui):
        return self.commands["MAC"]["APPEUI"]['SET'].format(appeui)

    def mac_appkey(self, appkey):
        return self.commands["MAC"]["APPKEY"].format(appkey)

    def mac_pwridx_set(self, pwrIndex):
        return self.commands["MAC"]["POWER_INDEX"]['SET'].format(pwrIndex)

    def mac_adr_set(self, switch):
        return self.commands["MAC"]["ADAPTIVE_DATARATE"]['SET'].format(switch)

    def mac_autoreply_set(self, switch):
        return self.commands["MAC"]["AUTO_REPLY"]['SET'].format(switch)

    def mac_save(self):
        return self.commands["MAC"]["SAVE"]

    def mac_join(self, activation):
        return self.commands["MAC"]["JOIN"].format(activation)

    def mac_tx_cnf(self, portno, data):
        return self.commands["MAC"]["TX"]["CONFIRMED"].format(portno, data)

    def mac_tx_uncfn(self, portno, data):
        return self.commands["MAC"]["TX"]["UNCONFIRMED"].format(portno, data)

    def mac_pause(self):
        return self.commands["MAC"]["PAUSE"]

    def mac_resume(self):
        return self.commands["MAC"]["RESUME"]

    def mac_devAddr_set(self, devAddr):
        return self.commands["MAC"]["DEVADDR"]['SET'].format(devAddr)

    def mac_appSKey(self, AppSKey):
        return self.commands["MAC"]["APPSKEY"].format(AppSKey)

    def mac_nwkSKey(self, NwkSKey):
        return self.commands["MAC"]["NWKSKEY"].format(NwkSKey)

    def mac_reset_band(self):
        return self.commands["MAC"]["RESET_BAND"]['868']
