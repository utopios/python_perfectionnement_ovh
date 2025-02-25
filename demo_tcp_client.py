import socket
host = "localhost"
port = 15555
mon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mon_socket.connect((host, port))
print(f"Connection on {port}")
mon_socket.send(b"Hey my name is Ihab!")
data = mon_socket.recv(255)
print(data)
mon_socket.close()