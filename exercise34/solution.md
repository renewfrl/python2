
import json

with open("twilio.json", "r") as read_file:
    data = json.load(read_file)
    for entry in data:
        if entry['error_code'] == 'ERR':
            print(entry['error_message'])


