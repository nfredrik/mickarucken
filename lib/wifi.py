from time import sleep, time

import machine
import network


class WifiTimeout(Exception):
    ...


class Wifi:
    TIMEOUT = 15

    def debug_print(self, text: str, end: str = ''):
        if self.debug:
            print(text, end=end)

    def __init__(self, ssid: str, password: str, debug: bool = False) -> None:
        self.debug = debug
        self.ssid = ssid
        self.password = password
        self.debug_print("Put modem on Station mode")
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self) -> None:
        self.debug_print("Check if already connected")
        if self.wlan.isconnected():
            return

        self.debug_print('Activate network interface')
        self.wlan.active(True)

        self.debug_print("Set power mode to get WiFi power-saving off (if needed)")
        self.wlan.config(pm=0xa11140)

        self.debug_print("Set wifi creds")
        self.wlan.connect(self.ssid, self.password)

        timeout = time() + self.TIMEOUT

        self.debug_print('Waiting for connection...', end='')
        while not self.wlan.isconnected() and \
                self.wlan.status() >= network.STAT_GOT_IP:
            self.debug_print('.', end='')
            sleep(1)
            if time() > timeout:
                raise TimeoutError('Error failed to connect, timeout!')

    def connected(self) -> bool:
        return self.wlan.isconnected()

    def __del__(self):
        if self.wlan:
            self.wlan.disconnect()
        self.wlan = None


class MonitorWifi:

    def __init__(self, wifi):
        self.wifi = wifi
        self.led = machine.Pin("LED", machine.Pin.OUT)

    def __call__(self, *args, **kwargs):
        if self.wifi.connected():
            self.led.toggle()
