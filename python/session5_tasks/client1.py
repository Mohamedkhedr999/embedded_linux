import socket




client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#ip =socket.gethostbyname(socket.gethostname())

#print(ip)
client.connect(("localhost",5555))
msg = str(input("please enter the message you want to send: "))
msg = msg.encode('UTF-8')
client.send(msg)
print('==========================================')
rodata = client.recv(1024)
print(f"localhost is sending you this message {rodata.decode('UTF-8')}")
print('==========================================')
   
client.close()