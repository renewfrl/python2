```
import json

with open("twilio.json", "r") as read_file:
    data = json.load(read_file)
    print("from: {} price: {}".format(data['from'], data["price"]))
            
```