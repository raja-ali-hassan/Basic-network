import socket

target_ip = "00:00:00"
port = 40

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(" the name of my dog is tiger and i want you to take it", (target_ip,port))

response = client.recvfrom(4096)
print(response.decode())
client.close()
