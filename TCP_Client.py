import socket

target = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target,target_port))

client.send(b"GET / HTTP/1.1\r\n HOST: google.com \r\n\r\n")

recieved = client.recv(4096)
print(recieved.decode())
client.close()
