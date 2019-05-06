lst = [a for a in range(0,4)]
with open('output.txt', 'w') as fp:
    for l in lst:
        fp.write("{}\n".format(l))