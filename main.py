import sys
from time import sleep

import dht
from dht import DHT11
from machine import Pin

GPIO_27 = 27
SLEEP_INTERVAL = 2


class TempHum:
    def __init__(self) -> None:
        self.sensor: DHT11 = dht.DHT11(Pin(GPIO_27))

    def read_sensor(self) -> tuple[int, int]:
        self.sensor.measure()
        temp = self.sensor.temperature()
        hum = self.sensor.humidity()
        return temp, hum


def main():
    sensor = TempHum()

    while True:
        try:
            sleep(SLEEP_INTERVAL)
            temp, hum = sensor.read_sensor()
            print(f"Temperature: {temp:.1f} C")
            print(f"Humidity: {hum:.1f} %")

            # blink with green LED to indicate success?

        except OSError as e:
            print('Failed to read sensor.')
            # blink with red LED to indicate failure?

        except KeyboardInterrupt as e:
            print('Exiting...')
            sys.exit(1)


if __name__ == "__main__":
    main()