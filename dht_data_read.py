import sys
import Adafruit_DHT

def get_data():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    return (humidity, temperature)

data = get_data()
print("Temp: {}C Humidity: {}%".format(data[0], data[1]))
