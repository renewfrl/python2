import ssl
import requests
from datetime import datetime

def check_server(url):
    start = datetime.now().strftime("s")
    res = requests.get(url)
    stop = datetime.now().strftime("s")
    if res.status_code == 200:
        print("jippy")

