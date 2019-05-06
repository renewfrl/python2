# Installations

* Working Windows 7 / Macbook with a Python IDE. I suggest to install an evaluation version of PyCharm or Pycharm community (please check if the license is valid for this type of usage) 
* Python 3.7 (install guide: [link](https://www.guru99.com/how-to-install-python.html))
* Git client (you should be able to do a git clone)

# Cheat sheat

## python REPL (Read, Eval, Print and Loop) 

enter: python
exit: quit()

### printing

```
print("...")
print("hello {}".format("rene"))
```

### Loops

```
entry = [1,2,3]
for a in entry:
    print("entry {}".format(a));
```

### lists +  comprehensions:

```
job = ["ops"]
job.append["dev"]

odd = [ a  for a in range(0,10) if a%2 == 1]
even = [ a  for a in range(0,10) if a%2 == 0]
```

### if/then/else

```
if condition==value:
    print("if true")
else:
    print("else true")
```

### while 
   
```
a=0
while(a<5):
    print(a)
    a+=1

# 0
# 1
# 2
# 3
# 4
```  
### and much more

[external link](https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf)