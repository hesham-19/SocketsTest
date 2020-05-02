import socket


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNET_MSG = "!DISCONNECT"
SERVER = "192.168.1"  # Your local IP address
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def Send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


Send(input("Enter Message "))
input()
Send(DISCONNET_MSG)
