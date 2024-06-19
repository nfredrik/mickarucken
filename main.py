import sys
from time import sleep

from http_requests import post_values, DataCakeError
from keys import WIFI_SSID, WIFI_PASS, DEV_EUI, APP_EUI, APP_KEY
from lora import LoRa
from temphum import TempHum, get_mean_values
from wifi import Wifi

SLEEP_INTERVAL = 10
GPIO_27 = 27


class ConnectionDroppedError(Exception):
    ...


def debug_print(text: str, debug=True):
    if debug:
        print(text)


def main():
    sensors = [TempHum(gpio_pin=GPIO_27),
               TempHum(gpio_pin=GPIO_27)
               ]
    wifi = Wifi(ssid=WIFI_SSID, password=WIFI_PASS)

    lora = LoRa()
    lora.setup_lora(dev_eui=DEV_EUI, app_eui=APP_EUI, app_key=APP_KEY)

    try:
        wifi.connect()
    except TimeoutError as err:
        print(f"{err}")

    while True:
        try:
            temp, hum = get_mean_values(sensors)
            debug_print(f"Temperature: {temp} C Humidity: {hum} %")
            if not wifi.connected():
                raise ConnectionDroppedError('Error, connection dropped')

            post_values(temp=temp, hum=hum)
            lora.send_over_lora(temp= temp, hum=hum )

            sleep(SLEEP_INTERVAL)

        except OSError as err:
            print(f"Problems with sensors? {err}")

        except ConnectionDroppedError as err:
            print(err)

        except DataCakeError as err:
            print(f"Failed to post{err}")

        except KeyboardInterrupt as err:
            print(f'Exiting...{err}')
            return 42


if __name__ == "__main__":
    sys.exit(main())
