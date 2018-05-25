from packages import dht_data_read
from packages import post_data

def post():
    post_data.http_post(dht_data_read.get_data())
    return

