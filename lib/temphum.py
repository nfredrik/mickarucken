import dht
from machine import Pin


class TempHum:
    def __init__(self, gpio_pin: int) -> None:
        self.sensor = dht.DHT11(Pin(gpio_pin))

    def read_sensor(self) -> tuple[int, int]:
        self.sensor.measure()
        temp = self.sensor.temperature()
        hum = self.sensor.humidity()
        return temp, hum
    
    
def get_mean_values(sensors: list) -> tuple[int, int]:
    def calculate_mean(arr: list):
        return sum(arr) / len(arr)

    valid_temps = []
    valid_hums = []

    for sensor in sensors:
        temp, hum = sensor.read_sensor()
        if 0 <= temp <= 50:
            valid_temps.append(temp)
        if 0 <= hum <= 100:
            valid_hums.append(hum)

    temp, hum = calculate_mean(valid_temps), calculate_mean(valid_hums)

    return temp, hum    
