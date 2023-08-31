import socket
import threading



def handle_client(client):
    rodata = client.recv(1024)
    print(f"{address} is sending you this message {rodata.decode('UTF-8')}")
    print('==========================================')
    msg = str(input("please enter your respond: "))
    msg = msg.encode('UTF-8')
    client.send(msg)
    client.close()

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mysocket.bind(('localhost',5555))
mysocket.listen()

while True:
    client , address = mysocket.accept()
    print(f"{address} is connected ")
    print('==========================================')
    client_thread = threading.Thread(target=handle_client,args=(client,))
    client_thread.start()