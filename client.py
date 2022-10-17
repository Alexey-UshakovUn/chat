import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9999))


with open('video.mp4', mode='rb') as file:
    data = file.read(2048)

    while data:
        client_socket.send(data)
        data = file.read(2048)

print('client socket close')
client_socket.close()