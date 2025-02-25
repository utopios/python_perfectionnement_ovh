import socket
mon_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mon_socket.bind(('', 15555))
while True:
    mon_socket.listen(5)
    client, address = mon_socket.accept()
    print(f"{address} connected")
    response = client.recv(255) # 255 octets max
    if response != "":
        print(response)
        if response.endswith(b"CLOSE"):
            break
print("Close")
client.close()
mon_socket.close()