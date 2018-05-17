import requests
import json
import time as t

def get_data():
        #print("Sleeping......")
        t.sleep(1)
        #print("Connecting to dweet.io")
        data = requests.get("http://dweet.io/get/latest/dweet/for/dunebot").text
        data = json.loads(data)
        data = list(data["with"][0]["content"])[0] 
        #print("Data is {}".format(DATA))

        return data