import socket
import threading
import RPi.GPIO as io

pin = 11

io.setmode(io.BOARD)
io.setup(pin, io.OUT)

servo = io.PWM(pin, 50)
servo.start(7)

servo_pos = 7
ip = '10.21.0.254'
port = 4200

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))


server.listen(5)


def handle(client):
    req = client.recv(1024)
    print(req)
    global servo_pos

    if req == b'left':
        servo_pos += 1
        servo.ChangeDutyCycle(servo_pos)
    if req == b'right':
        servo_pos -= 1
        servo.ChangeDutyCycle(servo_pos)
        

while True:
    client, addr = server.accept()
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()


