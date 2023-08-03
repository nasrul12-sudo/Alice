import socket

def client():
    host = socket.gethostname()
    port = 5000
    
    client_socket = socket.socket()
    client_socket.connect((host, port))
    
    massage = input(" --->>> ")
    
    while massage.lower().strip() != 'bye':
        client_socket.send(massage.encode())
        data = client_socket.recv(1024).decode()
        
        print("recived from server : " + data)
        massage = input(" ----->>> ")
        
    client_socket.close()
    
if __name__ == '__main__':
    client()