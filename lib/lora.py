import struct
import time

from machine import UART


class LoRaTimeout(Exception):
    ...


class LoRa:
    TIMEOUT = 30
    LOG_LEVEL = 1
    FREQ = "869525000"

    def __init__(self, debug=False):
        self._serial = UART(0, 115200)  # use RPI PICO GP0 and GP1
        self.debug = debug
        self.lora_enabled = False
        self._init()

    # Private methods
    def _init(self):
        while not self._check_device_connect():
            pass
        if self.debug:
            print("Module Connected")

        self._write_cmd("AT+CRESTORE\r\n")

        # Disable Log Information
        self._write_cmd(f"AT+ILOGLVL={self.LOG_LEVEL}\r\n")

        self._write_cmd("AT+CSAVE\r\n")

        self._write_cmd("AT+IREBOOT=0\r\n")

        time.sleep(1)

        while not self._check_device_connect():
            pass

    def _check_device_connect(self):
        restr = ""
        self._write_cmd("AT+CGMI?\r\n")
        restr = self._get_response()
        return True if "OK" in restr else False

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

    def _send_msg(self, data, confirm=1, nbtrials=1):

        cmd = f"AT+DTRX={confirm},{nbtrials},{len(data)},{data}\r\n"
        if self.debug:
            print("SENT", cmd)
        self._write_cmd(cmd)
        self._get_response()

    def _set_spreading_factor(self, sf):

        cmd = f"AT+CDATARATE={sf}\r\n"
        self._write_cmd(cmd)
        self._get_response()

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


    @staticmethod
    def _decode_msg(hex_encoded):
        if len(hex_encoded) % 2 == 0:
            return "".join(chr(int(hex_encoded[i:i + 2], 16)) for i in range(0, len(hex_encoded), 2))
        else:
            return hex_encoded

    def _get_response(self):

        time.sleep(0.05)
        restr = self._wait_msg(200)
        if self.debug:
            print(restr)

        return restr or ""

    def _check_join_status(self):
        restr = ""
        self._write_cmd("AT+CSTATUS?\r\n")
        restr = self._get_response()
        if "+CSTATUS:" in restr and "08" in restr:
            return True

        return False

    # Public methods
    def start_join(self):
        self._write_cmd("AT+CJOIN=1,0,10,8\r\n")

    def receive_msg(self):
        restr = self._get_response()
        if restr.find("OK+RECV:") != -1 and restr.find("02,00,00") == -1:
            data = restr[restr.find("OK+RECV:") + 17:-2]
            return self._decode_msg(data)
        else:
            return ""

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
        self._set_rx_window(self.FREQ)

        self._set_freq_mask("0001")

    def setup_lora(self, dev_eui: str, app_eui: str, app_key: str):

        self.configure(dev_eui, app_eui, app_key)

        self.start_join()
        print("Start Join LoRa.....")
        timeout = time.time() + self.TIMEOUT
        while not self._check_join_status():
            print('.', end='')

            if time.time() > timeout:
                raise LoRaTimeout('Error failed to connect, timeout!')

            time.sleep(1)
        print("Join success!")
        self.lora_enabled = True

    def send_over_lora(self, temp: int, hum: int):

        if not self.lora_enabled:
            return

        # Reading from sensor should be done here

        # Example temperature (in Celsius) and humidity (%) values with a negative temperature
        # temperature, humidity = -14.2, 42.5

        # Convert the float values to integers by multiplying them by a factor (example: 10)
        # temp_int = int(temperature * 10)
        # humidity_int = int(humidity * 10)

        # https://docs.micropython.org/en/latest/library/struct.html
        # >: Indicates big-endian byte order. Big-endian means the most significant byte is stored first.
        # h: Represents a short integer (2 bytes).
        # H: Represents an unsigned short integer (2 bytes).
        # payload = struct.pack(">hH", temp_int, humidity_int)
        payload = struct.pack(">hH", temp, hum)

        payload = payload.hex()

        self._send_msg(payload)
        print("Sent message:", payload)

        response = self.receive_msg()

        if response != "":
            print("Received: ", end=": ")
            print(response)
