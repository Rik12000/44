import socket

# Константа UDP пакета 
UDP_MAX_SIZE = 65535

 # Функция для запуска сервера 
def listen(host: str = '127.0.0.1', port: int = 3000):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Адрес сервера 
    s.bind((host, port))

    # Порт сервера 
    print(f'Listening at {host}:{port}')

    members = []
    while True:
        msg, addr = s.recvfrom(UDP_MAX_SIZE)

        # Добавлять клиента 
        if addr not in members:
            members.append(addr)
        
        # Функция для сообщений, если сообщений пустое то не уведомлять остальных клиентов чата 
        if not msg:
            continue

        # Уведомляет сервер что клиент присоединился серверу 
        client_id = addr[1]
        if msg.decode('utf-8') == '__join':

            # Ид клиента 
            print(f'Client {client_id} joined chat')
            continue
        
        # Уведомление о новом сообщении от другого клиента 
        msg = f'client{client_id}: {msg.decode("utf-8")}'
        for member in members:
            if member == addr:
                continue

            s.sendto(msg.encode('utf-8'), member)

# Запуск 
if __name__ == '__main__':
    listen()
