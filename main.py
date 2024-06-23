import sys
from time import sleep

from http_requests import post_values, DataCakeError
from keys import WIFI_SSID, WIFI_PASS, DEV_EUI, APP_EUI, APP_KEY
from lora import LoRa, LoRaTimeout
from machine import Timer
from temphum import TempHum, get_mean_values, TempHumError
from wifi import Wifi, WifiTimeout, MonitorWifi

SLEEP_INTERVAL = 10


class ConnectionDroppedError(Exception):
    ...


def debug_print(text: str, debug=True):
    if debug:
        print(text)


def main():
    sensors = [TempHum(gpio_pin=26),
               TempHum(gpio_pin=27),
               TempHum(gpio_pin=22)
               ]

    wifi = Wifi(ssid=WIFI_SSID, password=WIFI_PASS)
    try:
        wifi.connect()
    except WifiTimeout as err:
        print(f"Error {err}")

    monitor_wifi = MonitorWifi(wifi=wifi)
    Timer(period=5000, mode=Timer.PERIODIC, callback=lambda t: monitor_wifi())

    lora = LoRa()
    try:
        lora.setup_lora(dev_eui=DEV_EUI, app_eui=APP_EUI, app_key=APP_KEY)
    except LoRaTimeout as err:
        print(f"Error, timeout on LoRa: {err}")

    while True:
        try:
            temp, hum = get_mean_values(sensors)
            debug_print(f"Temperature: {temp} C Humidity: {hum} %")

            post_values(temp=temp, hum=hum)

            lora.send_over_lora(temp=temp, hum=hum)

            

        except TempHumError as err:
            print(f"Error, {err}")

        except ConnectionDroppedError as err:
            print(f"Error, connection dropped {err}")

        except DataCakeError as err:
            print(f"Error, failed to post{err}")

        except KeyboardInterrupt as err:
            print(f"User interrupted, exiting...")
            return 42

        sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
    sys.exit(main())
