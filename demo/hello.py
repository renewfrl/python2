import socket

s = socket.socket()
print("Socket successfully created")

port = 44444

s.bind(('', port))
print ("socket binded to %s" % (port))

s.listen(5)
print ("socket is listening")

while True:
    c, addr = s.accept()
    print ('Got connection from {}'.format(addr))
    c.send(b'Hello its me, rwi \n\n')
    c.close()