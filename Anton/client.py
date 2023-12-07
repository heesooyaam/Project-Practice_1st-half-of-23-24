import socket

def GET():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 2000))
    print('Print table_name')
    table_name = str(input())
    print('Chose column')
    column_name = input()
    get = f"SELECT {column_name} FROM {table_name}"
    sock.send(get.encode('utf8'))
    data = sock.recv(1024)
    sock.close()

    print('I found: ', data)

def CREATE():
    print('Print table_name')
    table_name = str(input())
    print('input column names and "0" in the end')
    columns = input()
    cur = input()
    while cur != '0':
        columns += ', ' + cur
        cur = input()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 2000))
    create = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    sock.send(create.encode('utf8'))
    data = sock.recv(1024)
    print(data.decode('utf8'))
    sock.close()

    # print('I found: ', data)


def SET():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 2000))
    print('Print table_name')
    table_name = str(input())
    set = f"INSERT INTO {table_name} (id, name, surname, birthdate) VALUES (2, 'Petr', 'Ivanov', '2003-12-13') "
    sock.send(set.encode('utf8'))
    data = sock.recv(1024)
    sock.close()

    print('I post: ', data)
def SET_FILE():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 2000))
    print('Print table_name')
    table_name = str(input())
    print("Print name of your file and path to it")
    fileName = input()
    filePath = input()
    with open(filePath, 'rb') as file:
        file_data = file.read()
    setFile = f"INSERT INTO {table_name} (filename, data) VALUES ({fileName}, {file_data}) "


actions = ['CRETE_TABLE', 'SET_DATA', "GET_DATA"]
print('Chose action:\n')
print(actions)
action = input()
if action == 'CRETE_TABLE':
    CREATE()
elif action == 'SET_DATA':
    print('Do you want to add file?\nYes/No')
    ans = str(input())
    if ans == 'YES':
        SET_FILE()
    else:
        SET()
else:
    GET()
