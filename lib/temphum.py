import dht
from machine import Pin
import time

class TempHumError(Exception):
    ...


class TempHum:
    def __init__(self, gpio_pin: int) -> None:
        self.sensor = dht.DHT11(Pin(gpio_pin))

    def read_sensor(self) -> tuple[int, int]:
        try:
            self.sensor.measure()
            temp = self.sensor.temperature()
            hum = self.sensor.humidity()
        except Exception as err:
            raise TempHumError(f'Error, failed to read sensors! {err}')

        # The DHT11 can be called no more than once per second.
        # Avoid any complications delay it here.
        time.sleep(1)

        return temp, hum


def get_mean_values(sensors: list[int]) -> tuple[float, float]:
    def closest_pair(values: list) -> tuple:
        a, b, c = values[0], values[1], values[2]
        # Calculate the absolute differences between each pair
        ab_diff = abs(a - b)
        ac_diff = abs(a - c)
        bc_diff = abs(b - c)

        # Determine the pair with the smallest difference
        if ab_diff <= ac_diff and ab_diff <= bc_diff:
            return a, b
        if ac_diff <= ab_diff and ac_diff <= bc_diff:
            return a, c

        return b, c

    def calculate_mean(arr: tuple) -> float:
        return sum(arr) / len(arr)

    temps = []
    hums = []

    for sensor in sensors:
        temp, hum = sensor.read_sensor()
        if 0 <= temp <= 50:
            temps.append(temp)
        if 0 <= hum <= 100:
            hums.append(hum)

    valid_temps = closest_pair(temps)
    valid_hums = closest_pair(hums)

    temp, hum = calculate_mean(valid_temps), calculate_mean(valid_hums)

    return temp, hum



