import sys
import Adafruit_DHT

#DHT11 = 'Adafruit_DHT.DHT11'
DATA_PIN = 4

def get_data():
    DATA = {}
    try:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DATA_PIN)
        #print(humidity,temperature)
        DATA.update({"Humidity":humidity})
        DATA.update({"Temperature":temperature})
        return DATA

    except Exception as e:
        print(str(e))
        return {"Humidity":0, "Temperature":0}
    #return (humidity, temperature)

print(get_data())
