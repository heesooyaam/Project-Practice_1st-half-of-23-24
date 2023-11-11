import socket
import sqlite3

# def start_server():
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind(('127.0.0.1', 2000))
#     server.listen(4)
#     while True:
#         print("Start")
#         client_socket, addr = server.accept()
#         data = client_socket.recv(1024).decode("utf-8")
#         print(data)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))
server.listen(4)
while True:
    print("Start")
    client_socket, addr = server.accept()
    print('1')
    data = client_socket.recv(1024).decode("utf-8")
    print(data)
    # client_socket.sendall(data.encode("utf-8"))
    with sqlite3.connect('DBs/database4.db') as db:
        cursor = db.cursor()
        cursor.execute(data)
        print('2')
    reply = 'Done'
    client_socket.send(reply.encode("utf-8"))







# content = 'Query'.encode('utf-8')
# client_socket.send(content)



