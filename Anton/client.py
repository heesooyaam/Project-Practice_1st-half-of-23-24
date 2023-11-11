import socket

def GET(column_name, table_name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 2000))
    get = f"SELECT {column_name} FROM {table_name}"
    sock.send(get.encode('utf8'))
    data = sock.recv(1024)
    sock.close()

    print('I found: ', data)

def CREATE(table_name, columns):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 2000))
    create = f"CREATE TABLE {table_name} ({columns})"
    sock.send(create.encode('utf8'))
    data = sock.recv(1024)
    print(data.decode('utf8'))
    sock.close()

    # print('I found: ', data)


def SET():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 2000))
    set = f"INSERT INTO {table_name} (id, name, surname, birthdate) VALUES (2, 'Petr', 'Ivanov', '2003-12-13') "
    sock.send(set.encode('utf8'))
    data = sock.recv(1024)
    sock.close()

    print('I post: ', data)

print('Print table_name')
# column_name = str(input())
table_name = str(input())
print('input column names and "0" in the end')
columns = input()
cur = input()
while cur != '0':
    columns += ', ' + cur
    cur = input()
# GET(column_name, table_name)
CREATE(table_name, columns)

