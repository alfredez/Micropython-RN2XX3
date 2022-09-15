"""
    Unittests Command class

    Author: Alfred Espinosa Encarnación
    Date: 15-09-2022
"""
import unittest
from src.Command import Command


class MyTestCase(unittest.TestCase):
    # Access to all commands from Command class
    try:
        cmds = Command(path='../src/commands.json')
    except FileNotFoundError as e:
        print(e)

        """[SYSTEM COMMANDS]"""

    def test_sys_sleep(self):
        self.assertEqual(self.cmds.sys_sleep(120), 'sys sleep 120')

    def test_sys_reset(self):
        self.assertEqual(self.cmds.sys_reset(), 'sys reset')

    def test_sys_erase_firmware(self):
        self.assertEqual(self.cmds.sys_erase_firmware(), 'sys eraseFW')

    def test_sys_factory_reset(self):
        self.assertEqual(self.cmds.sys_factory_reset(), 'sys factoryRESET')

    def test_sys_set_nvm(self):
        self.assertEqual(self.cmds.sys_set_nvm("300", "A5"), 'sys set nvm 300 A5')

    def test_sys_set_pindig(self):
        self.assertEqual(self.cmds.sys_set_pindig("GPIO5", 1), 'sys set pindig GPIO5 1')

    def test_sys_set_pindmode(self):
        self.assertEqual(self.cmds.sys_set_pinmode("GPIO0", "ana"), 'sys set pinmode GPIO0 ana')

    def test_sys_get_ver(self):
        self.assertEqual(self.cmds.sys_get_ver(), 'sys get ver')

    def test_sys_get_nvm(self):
        self.assertEqual(self.cmds.sys_get_nvm("300"), "sys get nvm 300")

    def test_sys_get_vdd(self):
        self.assertEqual(self.cmds.sys_get_vdd(), "sys get vdd")

    def test_sys_get_hweui(self):
        self.assertEqual(self.cmds.sys_get_hweui(), 'sys get hweui')

    def test_sys_get_pindig(self):
        self.assertEqual(self.cmds.sys_get_pindig("GPIO0"), 'sys get pindig GPIO0')

    def test_sys_get_pinana(self):
        self.assertEqual(self.cmds.sys_get_pinana("GPIO0"), 'sys get pinana GPIO0')

    """[MAC COMMANDS]"""

    def test_mac_set_appeui(self):
        self.assertEqual(self.cmds.mac_set_appeui('0000000000000000'), 'mac set appeui 0000000000000000')

    def test_mac_set_adr(self):
        self.assertEqual(self.cmds.mac_set_adr('on'), 'mac set adr on')

    def test_mac_reset(self):
        self.assertEqual(self.cmds.mac_reset(),'mac reset')

    def test_mac_reset_band(self):
        self.assertEqual(self.cmds.mac_reset_band(868), 'mac reset 868')

    def test_mac_tx_cnf(self):
        self.assertEqual(self.cmds.mac_tx_cnf(4, "5A5B5B"), 'mac tx cnf 4 5A5B5B')

    def test_mac_tx_uncnf(self):
        self.assertEqual(self.cmds.mac_tx_uncnf(4, "5A5B5B"), 'mac tx uncnf 4 5A5B5B')

    def test_mac_join(self):
        self.assertEqual(self.cmds.mac_join("otaa"), 'mac join otaa')

    def test_mac_save(self):
        self.assertEqual(self.cmds.mac_save(), "mac save")

    def test_mac_force_enable(self):
        self.assertEqual(self.cmds.mac_force_enable(), "mac forceENABLE")

    def test_mac_pause(self):
        self.assertEqual(self.cmds.mac_pause(), "mac pause")

    def test_mac_resume(self):
        self.assertEqual(self.cmds.mac_resume(), "mac resume")

    def test_mac_appkey(self):
        self.assertEqual(self.cmds.mac_set_appkey("00112233445566778899AABBCCDDEEFF"), "mac set appkey 00112233445566778899AABBCCDDEEFF")

    def test_mac_set_appskey(self):
        self.assertEqual(self.cmds.mac_set_appskey("AFBECD56473829100192837465FAEBDC"), "mac set appskey AFBECD56473829100192837465FAEBDC")

    def test_mac_set_autoreply(self):
        self.assertTrue(self.cmds.mac_set_autoreply("on"), "mac set ar on")

    def test_mac_set_bat(self):
        self.assertEqual(self.cmds.mac_set_bat(127), "mac set bat 127")

    def test_mac_set_channel_freq(self):
        self.assertEqual(self.cmds.mac_set_channel_freq(13, 864000000), "mac set ch freq 13 864000000")

    def test_mac_channel_dcycle(self):
        self.assertEqual(self.cmds.mac_set_channel_dcycle(13, 9), "mac set ch dcycle 13 9")

    def test_mac_channel_drrange(self):
        self.assertEqual(self.cmds.mac_set_channel_drrange(13, 0, 2), "mac set ch drrange 13 0 2")

    def test_mac_channel_status(self):
        self.assertEqual(self.cmds.mac_set_channel_status(4, "off"), "mac set ch status 4 off")

    def test_mac_set_class(self):
        self.assertEqual(self.cmds.mac_set_class("c"), "mac set class c")

    def test_mac_set_devaddr(self):
        self.assertEqual(self.cmds.mac_set_devaddr("ABCDEF01"), "mac set devaddr ABCDEF01")

    def test_mac_set_deveui(self):
        self.assertEqual(self.cmds.mac_set_deveui("0004A30B001A55ED"), "mac set deveui 0004A30B001A55ED")

    def test_mac_set_dnctr(self):
        self.assertEqual(self.cmds.mac_set_dnctr(30), "mac set dnctr 30")

    def test_mac_dr(self):
        self.assertEqual(self.cmds.mac_set_dr(5), "mac set dr 5")

    def test_mac_set_linkchk(self):
        self.assertEqual(self.cmds.mac_set_linkchk(600), "mac set linkchk 600")

    def test_mac_set_mcast(self):
        self.assertEqual(self.cmds.mac_set_mcast("on"), "mac set mcast on")

    def test_mac_set_mcastappskey(self):
        self.assertEqual(self.cmds.mac_set_mcastappskey("29100192AFBECD564738837465FAEBDC"), "mac set mcastappskey 29100192AFBECD564738837465FAEBDC")

    def test_mac_set_mcastdevaddr(self):
        self.assertEqual(self.cmds.mac_set_mcastdevaddr("54ABCDEF"), "mac set mcastdevaddr 54ABCDEF")

    def test_mac_set_mcastdnctr(self):
        self.assertEqual(self.cmds.mac_set_mcastdnctr(40), "mac set mcastdnctr 40")

    def test_mac_set_mcastnwkskey(self):
        self.assertEqual(self.cmds.mac_set_mcastnwkskey("6AFBECD1029384755647382910DACFEB"), "mac set mcastnwkskey 6AFBECD1029384755647382910DACFEB")

    def test_mac_set_nwkskey(self):
        self.assertEqual(self.cmds.mac_set_nwkskey("1029384756AFBECD5647382910DACFEB"), "mac set nwkskey 1029384756AFBECD5647382910DACFEB")

    def test_mac_set_pwridx(self):
        self.assertEqual(self.cmds.mac_set_pwridx(1), "mac set pwridx 1")

    def test_mac_set_retx(self):
        self.assertEqual(self.cmds.mac_set_retx(5), "mac set retx 5")

    def test_mac_set_rx_two(self):
        self.assertEqual(self.cmds.mac_set_rx_two(3, 865000000), "mac set rx2 3 865000000")

    def test_mac_set_rxdelay_one(self):
        self.assertEqual(self.cmds.mac_set_rxdelay_one(1000), "mac set rxdelay1 1000")

    def test_mac_set_synch(self):
        self.assertEqual(self.cmds.mac_set_sync("34"), "mac set sync 34")

    def test_mac_set_upctr(self):
        self.assertEqual(self.cmds.mac_set_upctr(10), "mac set upctr 10")

    def test_mac_get_adr(self):
        self.assertEqual(self.cmds.mac_get_adr(), "mac get adr")

    def test_mac_get_appeui(self):
        self.assertEqual(self.cmds.mac_get_appeui(), "mac get appeui")

    def test_mac_get_ar(self):
        self.assertEqual(self.cmds.mac_get_ar(), "mac get ar")

    def test_mac_get_channel_freq(self):
        self.assertEqual(self.cmds.mac_get_channel_freq(0), "mac get ch freq 0")

    def test_mac_get_channel_dcycle(self):
        self.assertEqual(self.cmds.mac_get_channel_dcycle(0), "mac get ch dcycle 0")

    def test_mac_get_channel_drrange(self):
        self.assertEqual(self.cmds.mac_get_channel_drrange(0), "mac get ch drrange 0")

    def test_mac_get_channel_status(self):
        self.assertEqual(self.cmds.mac_get_channel_status(2), "mac get ch status 2")

    def test_mac_get_class(self):
        self.assertEqual(self.cmds.mac_get_class(), "mac get class")

    def test_mac_get_dcycleps(self):
        self.assertEqual(self.cmds.mac_get_dcycleps(), "mac get dcycleps")

    def test_mac_get_devaddr(self):
        self.assertEqual(self.cmds.mac_get_devaddr(), "mac get devaddr")

    def test_mac_get_deveui(self):
        self.assertEqual(self.cmds.mac_get_deveui(), "mac get deveui")

    def test_mac_get_dnctr(self):
        self.assertEqual(self.cmds.mac_get_dnctr(), "mac get dnctr")

    def test_mac_get_dr(self):
        self.assertEqual(self.cmds.mac_get_dr(), "mac get dr")

    def test_mac_get_gwnb(self):
        self.assertEqual(self.cmds.mac_get_gwnb(), "mac get gwnb")

    def test_mac_mcast(self):
        self.assertEqual(self.cmds.mac_get_mcast(), "mac get mcast")

    def test_mac_get_mcastdevaddr(self):
        self.assertEqual(self.cmds.mac_get_mcastdevaddr(), "mac get mcastdevaddr")

    def test_mac_get_mcastdnctr(self):
        self.assertEqual(self.cmds.mac_get_mcastdnctr(), "mac get mcastdnctr")

    def test_mac_get_margin(self):
        self.assertEqual(self.cmds.mac_get_margin(), "mac get mrgn")

    def test_mac_get_pwridx(self):
        self.assertEqual(self.cmds.mac_get_pwridx(), "mac get pwridx")

    def test_mac_get_retx(self):
        self.assertEqual(self.cmds.mac_get_retx(), "mac get retx")

    def test_mac_get_tx_two(self):
        self.assertEqual(self.cmds.mac_get_rx_two(868), "mac get rx2 868")

    def test_mac_get_rxdelay_one(self):
        self.assertEqual(self.cmds.mac_get_rxdelay_one(), "mac get rxdelay1")

    def test_mac_get_rxdelay_two(self):
        self.assertEqual(self.cmds.mac_get_rxdelay_two(), "mac get rxdelay2")

    def test_mac_get_status(self):
        self.assertEqual(self.cmds.mac_get_status(), "mac get status")

    def test_mac_Get_sync(self):
        self.assertEqual(self.cmds.mac_get_sync(), "mac get sync")

    def test_mac_get_upctr(self):
        self.assertEqual(self.cmds.mac_get_upctr(), "mac get upctr")

    """[RADIO COMMANDS]"""

    def test_radio_rx(self):
        self.assertEqual(self.cmds.radio_rx(0), "radio rx 0")

    def test_radio_tx(self):
        self.assertEqual(self.cmds.radio_tx("48656c6C6F"), "radio tx 48656c6C6F")

    def test_radio_cw(self):
        self.assertEqual(self.cmds.radio_cw("on"), "radio cw on")

    def test_rxstop(self):
        self.assertEqual(self.cmds.rxstop(), "radio rxstop")

    def test_radio_set_afcbw(self):
        self.assertEqual(self.cmds.radio_set_afcbw(125), "radio set afcbw 125")

    def test_radio_set_bitrat(self):
        self.assertEqual(self.cmds.radio_set_bitrate(5000), "radio set bitrate 5000")

    def test_radio_set_bt(self):
        self.assertEqual(self.cmds.radio_set_bt("none"), "radio set bt none")

    def test_radio_set_bw(self):
        self.assertEqual(self.cmds.radio_set_bw(250), "radio set bw 250")

    def test_radio_set_cr(self):
        self.assertEqual(self.cmds.radio_set_cr("4/7"), "radio set cr 4/7")

    def test_radio_set_crc(self):
        self.assertEqual(self.cmds.radio_set_crc("on"), "radio set crc on")

    def test_radio_set_fdev(self):
        self.assertEqual(self.cmds.radio_set_fdev(5000), "radio set fdev 5000")

    def test_radio_set_iqi(self):
        self.assertEqual(self.cmds.radio_set_iqi("on"), "radio set iqi on")

    def test_radio_set_mod(self):
        self.assertEqual(self.cmds.radio_set_mod("lora"), "radio set mod lora")

    def test_radio_set_prlen(self):
        self.assertEqual(self.cmds.radio_set_prlen(8), "radio set prlen 8")

    def test_radio_set_pwr(self):
        self.assertEqual(self.cmds.radio_set_pwr(14), "radio set pwr 14")

    def test_radio_set_rxbw(self):
        self.assertEqual(self.cmds.radio_set_rxbw(250), "radio set rxbw 250")

    def test_radio_set_sf(self):
        self.assertEqual(self.cmds.radio_set_sf("sf7"), "radio set sf sf7")

    def test_radio_set_sync(self):
        self.assertEqual(self.cmds.radio_set_sync("12"), "radio set sync 12")

    def test_radio_set_wdt(self):
        self.assertEqual(self.cmds.radio_set_wdt(2000), "radio set wdt 2000")

    def test_radio_get_afcbw(self):
        self.assertEqual(self.cmds.radio_get_afcbw(), "radio get afcbw")

    def test_radio_get_bitrate(self):
        self.assertEqual(self.cmds.radio_get_bitrate(), "radio get bitrate")

    def test_radio_get_bt(self):
        self.assertEqual(self.cmds.radio_get_bt(), "radio get bt")

    def test_radio_get_bw(self):
        self.assertEqual(self.cmds.radio_get_bw(), "radio get bw")

    def test_radio_get_cr(self):
        self.assertEqual(self.cmds.radio_get_cr(), "radio get cr")

    def test_radio_get_crc(self):
        self.assertEqual(self.cmds.radio_get_crc(), "radio get crc")

    def test_radio_get_fdev(self):
        self.assertEqual(self.cmds.radio_get_fdev(), "radio get fdev")

    def test_radio_get_freq(self):
        self.assertEqual(self.cmds.radio_get_freq(), "radio get freq")

    def test_radio_get_iqi(self):
        self.assertEqual(self.cmds.radio_get_iqi(), "radio get iqi")

    def test_radio_get_mod(self):
        self.assertEqual(self.cmds.radio_get_prlen(), "radio get prlen")

    def test_radio_get_pwr(self):
        self.assertEqual(self.cmds.radio_get_pwr(), "radio get pwr")

    def test_radio_get_rssi(self):
        self.assertEqual(self.cmds.radio_get_rssi(), "radio get rssi")

    def test_radio_get_rxbw(self):
        self.assertEqual(self.cmds.radio_get_rxbw(), "radio get rxbw")

    def test_radio_get_sf(self):
        self.assertEqual(self.cmds.radio_get_sf(), "radio get sf")

    def test_radio_get_snr(self):
        self.assertEqual(self.cmds.radio_get_snr(), "radio get snr")

    def test_radio_get_sync(self):
        self.assertEqual(self.cmds.radio_get_sync(), "radio get sync")

    def test_radio_get_wdt(self):
        self.assertEqual(self.cmds.radio_get_wdt(), "radio get wdt")


if __name__ == '__main__':
    unittest.main()

