import requests
import json

DHT_URL = "https://dweet.io/dweet/for/m2d2-dht?"
def http_post(DATA):
    try:
        requests.post(DHT_URL, data=DATA)
    except Exception as e:
        print(e)
        #pass
    return