import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 9999))
server_socket.listen()

client_socket, client_addres = server_socket.accept()
print('connection recv', client_addres)

with open('server_video.mp4', mode='wb') as file:
    data = client_socket.recv(2048)

    while data:
        print(data)
        file.write(data)
        data = client_socket.recv(2048)

