import sys
from time import sleep

from http_requests import post_values, DataCakeError
from keys import WIFI_SSID, WIFI_PASS, DEV_EUI, APP_EUI, APP_KEY
from lora import LoRa
from temphum import TempHum, get_mean_values, TempHumError
from wifi import Wifi

SLEEP_INTERVAL = 10
GPIO_26 = 26
GPIO_27 = 27


class ConnectionDroppedError(Exception):
    ...


def debug_print(text: str, debug=True):
    if debug:
        print(text)


def main():

    # Setup of sensors and connections
    sensors = [TempHum(gpio_pin=GPIO_26),
               TempHum(gpio_pin=GPIO_27)
               ]

    wifi = Wifi(ssid=WIFI_SSID, password=WIFI_PASS)
    try:
        wifi.connect()
    except TimeoutError as err:
        print(f"{err}")

    #lora = LoRa()
    #lora.setup_lora(dev_eui=DEV_EUI, app_eui=APP_EUI, app_key=APP_KEY)


    # Eternal loop, if not interrupted,  of reading sensors and forward data to the cloud
    while True:
        try:
            temp, hum = get_mean_values(sensors)
            debug_print(f"Temperature: {temp} C Humidity: {hum} %")

            if not wifi.connected():
                raise ConnectionDroppedError('Error, connection dropped')

            post_values(temp=temp, hum=hum)
            #lora.send_over_lora(temp= temp, hum=hum )

            sleep(SLEEP_INTERVAL)

        except TempHumError as err:
            print(f"Error,{err}")

        except ConnectionDroppedError as err:
            print(f"Error, connection dropped {err}")

        except DataCakeError as err:
            print(f"Error, failed to post{err}")

        except KeyboardInterrupt as err:
            print(f"User interrupted, exiting...")
            return 42


if __name__ == "__main__":
    sys.exit(main())
