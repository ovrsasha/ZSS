import socket
import threading
import time


class Client():
    def get_string(self):
        pass

    def init_client(self, q, q2):

        def get_text():
            # print(str, end='')
            while True:
                if q.empty():
                    time.sleep(0.2)
                else:
                    return q.get()

        key = 8194
        shutdown = False
        join = False

        def receving(name, sock):
            while not shutdown:
                try:
                    while True:
                        data, addr = sock.recvfrom(1024)
                        # print(data.decode())
                        q2.put(data.decode())
                        time.sleep(0.2)
                except:
                    pass

        host = socket.gethostbyname(socket.gethostname())
        port = 0

        q2.put('Если сервер запущен локально то введите 0')
        q2.put('\nВведите IP сервера: ')
        server = get_text()
        q2.put(server)

        if server == '0':
            server = (socket.gethostbyname(socket.gethostname()), 9090)
        else:
            server = (server, 9090)

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((host, port))
        s.setblocking(0)

        q2.put('\nВведите имя: ')
        alias = get_text()
        q2.put(alias + '\n')

        t_receving = threading.Thread(target=receving, args=('RecvThread', s))
        t_receving.start()

        while not shutdown:
            if not join:
                s.sendto((alias + '<Вошёл в чат>').encode(), server)
                join = True
            else:
                message = get_text()
                s.sendto((alias + ': ' + message).encode(), server)

        t_receving.join()
        s.close()

    def __init__(self, q, q2):
        super().__init__()

        self.init_client(q, q2)


if __name__ == '__main__':
    ex = Client()
