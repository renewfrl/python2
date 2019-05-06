```
list = [ str(a) for a in range(0,100)]
with open('output.txt', 'w') as f:
    for item in list:
        f.write("{}\n".format(item))
            
```