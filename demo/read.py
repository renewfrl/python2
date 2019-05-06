with open('demo.txt', 'r') as fp:
    for l in fp:
        print(l.strip())

# with open('demo.txt', 'r') as fp2:
#     firstline = fp2.readline()
#     print(firstline.strip())
#
# with open('demo.txt', 'r') as fp3:
#     firstfour = fp3.read(4)
#     print(firstfour)
#     #print(firstfour.replace("\n",""))
