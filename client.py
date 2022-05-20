
import socket
import threading


nick = input("Type your nick: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


def receive():
    while 1:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == "NICK":
                client.send(nick.encode('ascii'))
            else:
                print(msg)
        except:
            print("error")
            client.close()
            break


def writing():
    while 1:
        msg = '{}: {}'.format(nick, input(''))
        client.send(msg.encode('ascii'))


rcv_thread = threading.Thread(target=receive)
rcv_thread.start()
write_thread = threading.Thread(target=writing)
write_thread.start()
