```
with open("test.txt", "r") as reader:
    line = reader.readline()
    while line:
        print("# {}".format(line.strip()))
        line = reader.readline()

            
```