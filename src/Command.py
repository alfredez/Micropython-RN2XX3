"""
                      [ Command Class ]
    Commands for RN2483 and RN2903 can be found in the product user guide by Microchip:

    "RN2483 LoRa® Technology Module Command Reference User’s Guide"
    https://ww1.microchip.com/downloads/en/DeviceDoc/RN2483-LoRa-Technology-Module-Command-Reference-User-Guide-DS40001784G.pdf

    "RN2903 LoRa® Technology Module Command Reference User’s Guide"
    https://ww1.microchip.com/downloads/en/DeviceDoc/RN2903%20LoRa%20Technology%20Module%20Command%20Reference%20User%20Guide-40001811B.pdf

    [-------------------------------------------------------]
    Version:
    [1.0]:
        + Changes:
            - Added command dictionary
            - Added all commands based on the RN2483 and RN2903 user's guide
"""
from json import load


class Command:
    """
    Command Class based on the 'Command Reference User's Guide' for the RN2483 and RN2903 module.

    Before using any functions, read the information about the commands in the user guide for the appropriate module.
    """

    def __init__(self, path=None):
        """
        Construct a Command object to provide access to all commands for the module

        Args:
            path (str): Location of the command dictionary
        """
        # Opening JSON file
        command_file = open(path)

        # returns JSON object as a dictionary
        self.commands = load(command_file)

    """[SYSTEM COMMANDS]"""

    def sys_sleep(self, length: int) -> str:
        return self.commands["SYSTEM"]["SLEEP"].formmat(length)

    def sys_reset(self):
        return self.commands["SYSTEM"]["RESET"]

    def sys_erase_firmware(self):
        return self.commands["SYSTEM"]["ERASEFW"]

    def sys_factory_reset(self):
        return self.commands["SYSTEM"]["FACTORY_RESET"]

    def sys_set_nvm(self, address: str, data: str) -> str:
        return self.commands["SYSTEM"]["NVM"]["SET"].format(address, data)

    def sys_set_pindig(self, pin_name: str, pin_state: int) -> str:
        return self.commands["SYSTEM"]["PINDIG"]["SET"].format(pin_name, pin_state)

    def sys_set_pinmode(self, pin_name: str, pin_mode: str) -> str:
        return self.commands["SYSTEM"]["PINDMODE"].format(pin_name, pin_mode)

    def sys_get_ver(self):
        return self.commands["SYSTEM"]["VERSION"]

    def sys_get_nvm(self, address: str) -> str:
        return self.commands["SYSTEM"]["NVM"]["GET"].format(address)

    def sys_get_vdd(self):
        return self.commands["SYSTEM"]["VOLTAGE"]

    def sys_get_hweui(self):
        return self.commands["SYSTEM"]["HWEUI"]

    def sys_get_pindig(self, pin_name: str) -> str:

        return self.commands["SYSTEM"]["PINDIG"]["GET"].format(pin_name)

    def sys_get_pinana(self, pin_name: str) -> str:
        return self.commands["SYSTEM"]["PINANA"].format(pin_name)

    """[MAC COMMANDS]"""

    def mac_set_appeui(self, appeui: str) -> str:
        return self.commands["MAC"]["APPEUI"]['SET'].format(appeui)

    def mac_set_adr(self, switch: str) -> str:
        return self.commands["MAC"]["ADAPTIVE_DATARATE"]['SET'].format(switch)

    def mac_reset(self):
        return self.commands["MAC"]["RESET"]

    def mac_reset_band(self, band: int) -> str:
        if band == 868:
            return self.commands["MAC"]["RESET_BAND"]['868']
        else:
            return self.commands["MAC"]["RESET_BAND"]['433']

    def mac_tx_cnf(self, portno: int, data: str) -> str:
        return self.commands["MAC"]["TX"]["CONFIRMED"].format(portno, data)

    def mac_tx_uncfn(self, portno: int, data: str) -> str:
        return self.commands["MAC"]["TX"]["UNCONFIRMED"].format(portno, data)

    def mac_join(self, mode: str) -> str:
        return self.commands["MAC"]["JOIN"].format(mode)

    def mac_save(self):
        return self.commands["MAC"]["SAVE"]

    def mac_force_enable(self):
        return self.commands["MAC"]["FORCE_ENABLE"]

    def mac_pause(self):
        return self.commands["MAC"]["PAUSE"]

    def mac_resume(self):
        return self.commands["MAC"]["RESUME"]

    def mac_set_appkey(self, appkey: str) -> str:
        return self.commands["MAC"]["APPKEY"].format(appkey)

    def mac_set_appskey(self, appskey: str) -> str:
        return self.commands["MAC"]["APPSKEY"].format(appskey)

    def mac_set_autoreply(self, state: str) -> str:
        return self.commands["MAC"]["AUTO_REPLY"]['SET'].format(state)

    def mac_set_bat(self, level: int) -> str:
        return self.commands["MAC"]["BAT"].format(level)

    def mac_set_channel_freq(self, channel_id: int, frequency: int) -> str:
        return self.commands["MAC"]["CHANNEL"]["FREQUENCY"]["SET"].format(channel_id, frequency)

    def mac_set_channel_dcycle(self, channel_id: int, duty_cycle: int) -> str:
        return self.commands["MAC"]["CHANNEL"]["DCYCLE"]["SET"].format(channel_id, duty_cycle)

    def mac_set_channel_drrange(self, channel_id: int, min_range: int, max_range: int) -> str:
        return self.commands["MAC"]["CHANNEL"]["DRRANGE"]["SET"].format(channel_id, min_range, max_range)

    def mac_set_channel_status(self, channel_id: int, status: str) -> str:
        return self.commands["MAC"]["CHANNEL"]["STATUS"]["SET"].format(channel_id, status)

    def mac_set_class(self, device_class: str) -> str:
        return self.commands["MAC"]["CLASS"]['SET'].format(device_class)

    def mac_set_devaddr(self, devaddr: str) -> str:
        return self.commands["MAC"]["DEVADDR"]['SET'].format(devaddr)

    def mac_set_deveui(self, deveui: str) -> str:
        return self.commands["MAC"]["DEVEUI"]['SET'].format(deveui)

    def mac_set_dnctr(self, FCntDown: int) -> str:
        return self.commands["MAC"]["DNCTR"]['SET'].format(FCntDown)

    def mac_set_dr(self, dataRate: int) -> str:
        return self.commands["MAC"]["DATARATE"]['SET'].format(dataRate)

    def mac_set_linkchk(self, linkCheck: int) -> str:
        return self.commands["MAC"]["LINK_CHECK"].format(linkCheck)

    def mac_set_mcast(self, state: str) -> str:
        return self.commands["MAC"]["MCAST"]['SET'].format(state)

    def mac_set_mcastappskey(self, mcastApplicationSessionkey: str) -> str:
        return self.commands["MAC"]["MCAST_APPSKEY"]['SET'].format(mcastApplicationSessionkey)

    def mac_set_mcastdevaddr(self, mcastAddress: str) -> str:
        return self.commands["MAC"]["MCAST_DEVADDR"]['SET'].format(mcastAddress)

    def mac_set_mcastdnctr(self, fMcastCntDown: int) -> str:
        return self.commands["MAC"]["MCAST_DNCTR"]['SET'].format(fMcastCntDown)

    def mac_set_mcastnwkskey(self, mcastNetworkSessionkey: str) -> str:
        return self.commands["MAC"]["MCAST_NWKSKEY"]['SET'].format(mcastNetworkSessionkey)

    def mac_set_nwkskey(self, nwkSessKey: str) -> str:
        return self.commands["MAC"]["NWKSKEY"].format(nwkSessKey)

    def mac_set_pwridx(self, pwrIndex: int) -> str:
        return self.commands["MAC"]["POWER_INDEX"]['SET'].format(pwrIndex)

    def mac_set_retx(self, reTxNb: int) -> str:
        return self.commands["MAC"]["RETX"]['SET'].format(reTxNb)

    def mac_set_rx_two(self, dataRate: int, frequency: int) -> str:
        return self.commands["MAC"]["RX2"]['SET'].format(dataRate, frequency)

    def mac_set_rxdelay_one(self, rxDelay: int) -> str:
        return self.commands["MAC"]["RXDELAY1"]['SET'].format(rxDelay)

    def mac_set_sync(self, synchWord: str) -> str:
        return self.commands["MAC"]["SYNC"]['SET'].format(synchWord)

    def mac_set_upctr(self, fCntup: int) -> str:
        return self.commands["MAC"]["UPCTR"]['SET'].format(fCntup)

    def mac_get_adr(self):
        return self.commands["MAC"]["ADAPTIVE_DATARATE"]['GET']

    def mac_get_appeui(self):
        return self.commands["MAC"]["APPEUI"]['GET']

    def mac_get_ar(self):
        return self.commands["MAC"]["AUTO_REPLY"]['GET']

    def mac_get_channel_freq(self, channel_id: int) -> str:
        return self.commands["MAC"]["CHANNEL"]["FREQUENCY"]["GET"].format(channel_id)

    def mac_get_channel_dcycle(self, channel_id: int) -> str:
        return self.commands["MAC"]["CHANNEL"]["DCYCLE"]["GET"].format(channel_id)

    def mac_get_channel_drrange(self, channel_id: int) -> str:
        return self.commands["MAC"]["CHANNEL"]["DRRANGE"]["GET"].format(channel_id)

    def mac_get_channel_status(self, channel_id: int) -> str:
        return self.commands["MAC"]["CHANNEL"]["STATUS"]["GET"].format(channel_id)

    def mac_get_class(self):
        return self.commands["MAC"]["CLASS"]['GET']

    def mac_get_dcycleps(self):
        return self.commands["MAC"]["DYCLEPS"]

    def mac_get_devaddr(self):
        return self.commands["MAC"]["DEVADDR"]['GET']

    def mac_get_deveui(self):
        return self.commands["MAC"]["DEVEUI"]['GET']

    def mac_get_dnctr(self):
        return self.commands["MAC"]["DNCTR"]['GET']

    def mac_get_dr(self):
        return self.commands["MAC"]["DATARATE"]['GET']

    def mac_get_gwnb(self):
        return self.commands["MAC"]["GATEWAY_NUMBER"]

    def mac_get_mcast(self):
        return self.commands["MAC"]["MCAST"]['GET']

    def mac_get_mcastdevaddr(self):
        return self.commands["MAC"]["MCAST_DEVADDR"]['GET']

    def mac_get_mcastdnctr(self):
        return self.commands["MAC"]["MCAST_DNCTR"]['GET']

    def mac_get_margin(self):
        return self.commands["MAC"]["MARGIN"]

    def mac_get_pwridx(self):
        return self.commands["MAC"]["POWER_INDEX"]['GET']

    def mac_get_retx(self):
        return self.commands["MAC"]["RETX"]['GET']

    def mac_get_rx_two(self, frequency_band: int) -> str:
        return self.commands["MAC"]["RX2"]['GET'].format(frequency_band)

    def mac_get_rxdelay_one(self):
        return self.commands["MAC"]["RXDELAY1"]['GET']

    def mac_get_rxdelay_two(self):
        return self.commands["MAC"]["RXDELAY2"]['GET']

    def mac_get_status(self):
        return self.commands["MAC"]["STATUS"]

    def mac_get_sync(self):
        return self.commands["MAC"]["SYNC"]['GET']

    def mac_get_upctr(self):
        return self.commands["MAC"]["UPCTR"]['GET']

    """[RADIO COMMANDS]"""

    def radio_rx(self, rxWindowSize: int) -> str:
        return self.commands["RADIO"]["RX"].format(rxWindowSize)

    def radio_tx(self, data: str) -> str:
        return self.commands["RADIO"]["TX"].format(data)

    def radio_cw(self, state: str) -> str:
        return self.commands["RADIO"]["CW"].format(state)

    def rxstop(self):
        return self.commands["RADIO"]["RXSTOP"]

    def radio_set_afcbw(self, autoFreqBand: float) -> str:
        return self.commands["RADIO"]["AUTOFREQBAND"]["SET"].format(autoFreqBand)

    def radio_set_bitrate(self, fskBitrate: int) -> str:
        return self.commands["RADIO"]["BITRATE"]["SET"].format(fskBitrate)

    def radio_set_bt(self, gfBT: str) -> str:
        return self.commands["RADIO"]["BT"]["SET"].format(gfBT)

    def radio_set_bw(self, bandwidth: int) -> str:
        return self.commands["RADIO"]["BANDWIDTH"]["SET"].format(bandwidth)

    def radio_set_cr(self, coding_rate: str) -> str:
        return self.commands["RADIO"]["CODING_RATE"]["SET"].format(coding_rate)

    def radio_set_crc(self, crc_header: str) -> str:
        return self.commands["RADIO"]["CRC"]["SET"].format(crc_header)

    def radio_set_fdev(self, freqdev: int) -> str:
        return self.commands["RADIO"]["FREQDEV"]["SET"].format(freqdev)

    def radio_set_iqi(self, iq_invert: str) -> str:
        return self.commands["RADIO"]["IQI"]["SET"].format(iq_invert)

    def radio_set_mod(self, mode: str) -> str:
        return self.commands["RADIO"]["MODE"]["SET"].format(mode)

    def radio_set_prlen(self, preamble: int) -> str:
        return self.commands["RADIO"]["PREAMBLE"]["SET"].format(preamble)

    def radio_set_pwr(self, pwrout: int) -> str:
        return self.commands["RADIO"]["POWER"]["SET"].format(pwrout)

    def radio_set_rxbw(self, rxBandwidth: float) -> str:
        return self.commands["RADIO"]["RXBW"]["SET"].format(rxBandwidth)

    def radio_set_sf(self, spreading_factor: str) -> str:
        return self.commands["RADIO"]["SF"]["SET"].format(spreading_factor)

    def radio_set_sync(self, syncword: str) -> str:
        return self.commands["RADIO"]["SYNC"]["SET"].format(syncword)

    def radio_set_wdt(self, watchdog: int) -> str:
        return self.commands["RADIO"]["WATCHDOG"]["SET"].format(watchdog)

    def radio_get_afcbw(self):
        return self.commands["RADIO"]["AUTOFREQBAND"]["GET"]

    def radio_get_bitrate(self):
        return self.commands["RADIO"]["BITRATE"]["GET"]

    def radio_get_bt(self):
        return self.commands["RADIO"]["BT"]["GET"]

    def radio_get_bw(self):
        return self.commands["RADIO"]["BANDWIDTH"]["GET"]

    def radio_get_cr(self):
        return self.commands["RADIO"]["CODING_RATE"]["GET"]

    def radio_get_crc(self):
        return self.commands["RADIO"]["CRC"]["GET"]

    def radio_get_fdev(self):
        return self.commands["RADIO"]["FREQDEV"]["GET"]

    def radio_get_freq(self):
        return self.commands["RADIO"]["FREQUENCY"]["GET"]

    def radio_get_iqi(self):
        return self.commands["RADIO"]["IQI"]["GET"]

    def radio_get_mod(self):
        return self.commands["RADIO"]["MODE"]["GET"]

    def radio_get_prlen(self):
        return self.commands["RADIO"]["PREAMBLE"]["GET"]

    def radio_get_pwr(self):
        return self.commands["RADIO"]["POWER"]["GET"]

    def radio_get_rssi(self):
        return self.commands["RADIO"]["RSSI"]["GET"]

    def radio_get_rxbw(self):
        return self.commands["RADIO"]["RXBW"]["GET"]

    def radio_get_sf(self):
        return self.commands["RADIO"]["SF"]["GET"]

    def radio_get_snr(self):
        return self.commands["RADIO"]["SNR"]

    def radio_get_sync(self):
        return self.commands["RADIO"]["SYNC"]["GET"]

    def radio_get_wdt(self):
        return self.commands["RADIO"]["WATCHDOG"]["GET"]
