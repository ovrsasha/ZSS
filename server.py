import socket, time

host = socket.gethostbyname(socket.gethostname())
print('host:', host)
port = 9090

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

quit = False
print('[ Server Started ]')

while not quit:
    try:
        data, addr = s.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        # print(addr)
        print("[" + addr[0] + "]=[" + str(addr[1]) + "]=[" + itsatime + "]/", end="")
        print(data.decode())

        for client in clients:
            # if addr != client:
            s.sendto((data.decode() + '\n').encode(), client)
    except:
        print("\n[ Server Stopped ]")
        quit = True

s.close()
