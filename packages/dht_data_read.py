import sys
import Adafruit_DHT

DHT11 = "Adafruit_DHT.DHT11"
DATA_PIN = 4

def get_data():
    DATA = {}
    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT11, DATA_PIN)
        DATA.update({"Humidity":humidity})
        DATA.update({"Temperature":temperature})
        return DATA
        
    except Exception as e:
        print(str(e))
        return {"Humidity":0, "Temperature":0}
    #return (humidity, temperature)

#data = get_data()
#print("Temp: {}C Humidity: {}%".format(data[0], data[1]))