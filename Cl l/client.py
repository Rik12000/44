import socket
import threading
import os


UDP_MAX_SIZE = 65535

# Функция для слушание сообщении и их отображении 
def listen(s: socket.socket):

    while True:
        msg = s.recv(UDP_MAX_SIZE)
        print('\r\r' + msg.decode('utf-8') + '\n' + f'you: ', end='')


def connect(host: str = '127.0.0.1', port: int = 3000):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Клиент подключается к серверу 
    s.connect((host, port))

    threading.Thread(target=listen, args=(s,), daemon=True).start()

    # Сообщает серверу что клиент присоединился к чату 
    s.send('__join'.encode('utf-8'))

    # Клиент может писать сообщении сколько угодно 
    while True:
        msg = input(f'you: ')
        s.send(msg.encode('utf-8'))

# Очищение терминала, приветствие клиента и соединение к серверу 
if __name__ == '__main__':
    os.system('clear')
    print('Welcome to chat!')
    connect()

