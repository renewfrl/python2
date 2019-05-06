```
import csv
with open('test.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        # lazy solution should normally iterate for the rows or put the rows in a dictionary
        print(row[0])
        print(row[1])
            
```