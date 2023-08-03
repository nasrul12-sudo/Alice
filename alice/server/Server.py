import socket
def server():
    hots = socket.gethostname()
    port = 5000
    
    server_socket = socket.socket()
    server_socket.bind((hots, port))
    
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("connect from : " + str(address))
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connection user : " + str(data))
        data = input(" --->>> ")
        conn.send(data.encode())
    conn.close()
    
if __name__ == '__main__':
    server()