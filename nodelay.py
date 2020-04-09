import socket

message_number = 0
s = socket.socket(socket.AF_INET, socket.SocketKind.SOCK_DGRAM)
s.connect(("localhost", 12345))

message = "ping message number " + str(message_number)

s.sendall(message.encode())
a = s.recv(4096)
print(a)
message = "ping message number " + str(message_number+1)

s.sendall(message.encode())
a = s.recv(4096)
print(a)

s.close()
