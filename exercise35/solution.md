```python
import requests

r = requests.get("https://www.ing.nl")
cookies = r.cookies.get_dict()
with open("cookies.txt","w") as fp:
    for i, k in enumerate(cookies):
        fp.write("Cookie name: {} value {}\n".format(k,cookies.get(k)))

```