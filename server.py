
import socket
import threading

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicks = []


def sending(msg):
    for client in clients:
        client.send(msg)


def writing_data(client):
    while 1:
        try:
            msg = client.recv(1024)
            sending(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nick = nicks[index]
            sending.remove(nick)
            break


def receive():
    while 1:
        client, adress = server.accept()
        print("Connected")
        client.send('NICK'.encode('ascii'))
        nick = client.recv(1024).decode('ascii')
        nicks.append(nick)
        clients.append(client)
        print("Your nickname is {}".format(nick))
        sending("{} joined".format(nick).encode('ascii'))
        client.send('Connected to server'. encode('ascii'))
        thread = threading.Thread(target=writing_data, args=(client,))
        thread.start()


receive()
