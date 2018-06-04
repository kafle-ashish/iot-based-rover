import requests
import json
#import time as t

def get_data():
        #print("Sleeping......")
        #t.sleep(1)
        #print("Connecting to dweet.io")
        data = requests.get("http://dweet.io/get/latest/dweet/for/m2d2").text
        data = json.loads(data)
        print("Data is {}".format(data))
        return list(data['with'][0]['content'].keys())


