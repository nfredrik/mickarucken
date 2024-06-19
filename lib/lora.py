import struct
import time

from machine import UART


# https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/lorawan/ASR650X%20AT%20Command%20Introduction-20190605.pdf

class LoRa:

    def __init__(self, debug=True):
        self._serial = UART(0, 115200)  # use RPI PICO GP0 and GP1
        self.debug = debug
        self.init()

    def _check_device_connect(self):
        restr = ""
        self._write_cmd("AT+CGMI?\r\n")
        restr = self._get_response()
        if "OK" not in restr:
            return False
        else:
            return True

    def _ng_check_device_connect(self):
        restr = ""
        self._write_cmd("AT+CGMI?\r\n")
        restr = self._get_response()
        return True if "OK" in restr else False

    def old_check_join_status(self):
        restr = ""
        self._write_cmd("AT+CSTATUS?\r\n")
        restr = self._get_response()
        if restr.find("+CSTATUS:") != -1:
            if restr.find("08") != -1:  # or restr.find("07") != -1 or restr.find("08") != -1:
                return True
            else:
                return False
        else:
            return False

    def check_join_status(self):
        restr = ""
        self._write_cmd("AT+CSTATUS?\r\n")
        restr = self._get_response()
        if restr.find("+CSTATUS:") != -1:
            if "08" in restr:  # or restr.find("07") != -1 or restr.find("08") != -1:
                return True
            else:
                return False
        else:
            return False

    def _wait_msg(self, timeout):
        restr = ""
        start = round(time.time() * 1000)
        while True:
            if (round(time.time() * 1000) - start) < timeout:
                res = self._serial.readline()
                if res:
                    if len(res) > 0:
                        restr += str(res)
            else:
                break
        return restr

    def _write_cmd(self, command):
        self._serial.write(command)
        time.sleep(0.1)

    def send_msg(self, data, confirm=1, nbtrials=1):

        cmd = f"AT+DTRX={confirm},{nbtrials},{len(data)},{data}\r\n"
        if self.debug:
            print("SENT", cmd)
        self._write_cmd(cmd)
        self._get_response()

    def _set_spreading_factor(self, sf):

        cmd = f"AT+CDATARATE={sf}\r\n"
        self._write_cmd(cmd)
        self._get_response()

    def receive_msg(self):
        restr = self._get_response()
        if restr.find("OK+RECV:") != -1 and restr.find("02,00,00") == -1:
            data = restr[restr.find("OK+RECV:") + 17:-2]
            return self._decode_msg(data)
        else:
            return ""

    def _config_otta(self, device_eui, app_eui, app_key, ul_dl_mode):
        self._write_cmd("AT+CJOINMODE=0\r\n")
        self._get_response()
        self._write_cmd("AT+CDEVEUI=" + device_eui + "\r\n")
        self._get_response()
        self._write_cmd("AT+CAPPEUI=" + app_eui + "\r\n")
        self._get_response()
        self._write_cmd("AT+CAPPKEY=" + app_key + "\r\n")
        self._get_response()
        self._write_cmd("AT+CULDLMODE=" + ul_dl_mode + "\r\n")
        self._get_response()

    def _set_class(self, mode):
        self._write_cmd("AT+CCLASS=" + mode + "\r\n")

    def _set_rx_window(self, freq):
        self._write_cmd("AT+CRXP=0,0," + freq + "\r\n")

    def _set_freq_mask(self, mask):
        self._write_cmd("AT+CFREQBANDMASK=" + mask + "\r\n")

    def start_join(self):
        self._write_cmd("AT+CJOIN=1,0,10,8\r\n")

    def _decode_msg(self, hex_encoded):
        if len(hex_encoded) % 2 == 0:
            buf = hex_encoded
            tempbuf = [None] * len(hex_encoded)
            i = 0
            loop = 2
            while loop < len(hex_encoded) + 1:
                tmpstr = buf[loop - 2:loop]
                tempbuf[i] = chr(int(tmpstr, 16))
                i += 1
                loop += 2
            return "".join(tempbuf)
        else:
            return hex_encoded

    def _old_get_response(self):

        time.sleep(0.05)
        restr = self._wait_msg(200)
        if self.debug:
            print(restr)

        return restr

    def _get_response(self):

        time.sleep(0.05)
        restr = self._wait_msg(200)
        if self.debug:
            print(restr)

        return restr or ""

    def init(self):
        while not self._check_device_connect():
            pass
        if self.debug:
            print("Module Connected")

        self._write_cmd("AT+CRESTORE\r\n")

        # Disable Log Information
        # self._write_cmd("AT+ILOGLVL=1\r\n")
        self._write_cmd("AT+ILOGLVL=5\r\n")

        self._write_cmd("AT+CSAVE\r\n")

        self._write_cmd("AT+IREBOOT=0\r\n")

        time.sleep(1)

        while not self._check_device_connect():
            pass

    def configure(self, devui, appeui, appkey):
        print("Module Config...")
        self._config_otta(devui,  # Device EUI
                          appeui,  # APP EUI
                          appkey,  # APP KEY
                          "2"  # Upload Download Mode
                          )

        # Set Class Mode
        self._set_class("2")
        self._write_cmd("AT+CWORKMODE=2\r\n")

        self._set_spreading_factor("5")

        # LoRaWAN868
        #TODO: Wrong freq?
        self._set_rx_window("869525000")

        self._set_freq_mask("0001")


    def setup_lora(self, dev_eui:str, app_eui:str, app_key:str):

        #lora.configure(DEV_EUI, APP_EUI, APP_KEY)
        self.configure(dev_eui, app_eui, app_key)

        self.start_join()
        print("Start Join.....")
        while not self.check_join_status():
            print("Joining....")
            time.sleep(1)
        print("Join success!")


    def send_over_lora(self,temp:int, hum:int):
        # Reading from sensor should be done here

        # Example temperature (in Celsius) and humidity (%) values with a negative temperature
        #temperature, humidity = -14.2, 42.5

        # Convert the float values to integers by multiplying them by a factor (example: 10)
        #temp_int = int(temperature * 10)
        #humidity_int = int(humidity * 10)

        # https://docs.micropython.org/en/latest/library/struct.html
        # >: Indicates big-endian byte order. Big-endian means the most significant byte is stored first.
        # h: Represents a short integer (2 bytes).
        # H: Represents an unsigned short integer (2 bytes).
        #payload = struct.pack(">hH", temp_int, humidity_int)
        payload = struct.pack(">hH", temp, hum)

        payload = payload.hex()

        self.send_msg(payload)
        print("Sent message:", payload)

        response = self.receive_msg()

        if response != "":
            print("Received: ", end=": ")
            print(response)

