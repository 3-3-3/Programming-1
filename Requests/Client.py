import socket

target_host = "10.21.4.247"
target_port = 4200

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b'Left')
