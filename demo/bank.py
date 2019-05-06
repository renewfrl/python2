import requests

r = requests.get("www.ing.nl")
r.status_code
r.text

with open("output.html","w") as fp:
    fp.write(r.text)