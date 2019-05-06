import socket
s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
s.bind(("127.0.0.1" ,0))
s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

while True:
   data = s.recvfrom(1000)
   print (data)

#ping 127.0.0.1