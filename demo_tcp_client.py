import socket
host = "localhost"
port = 15555
mon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mon_socket.connect((host, port))
print(f"Connection on {port}")
mon_socket.send(b"Hey my name is Guillaume!")
mon_socket.send(bytes("Hey my name is Guillaume!", encoding="UTF-8"))
mon_socket.send(bytes("Nice to meet you !", encoding="UTF-8"))
mon_socket.send(bytes("CLOSE", encoding="UTF-8"))
print("Close")
mon_socket.close()