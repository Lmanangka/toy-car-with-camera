import socket
import io
import picamera
import struct
import time
import threading
from gpiozero import Motor

class Car(object):
    def __init__(self, ip, port):
        self.client =  socket.socket()
        self.client.connect((ip, port))
        self.connection = self.client.makefile('wb')
        self.msg = None

        self.motor1 = Motor(forward = 27, backward = 18)
        self.motor2 = Motor(forward = 24, backward = 10)

    def Vision(self):
        with picamera.PiCamera() as camera:
            camera.rotation = 180
            camera.resolution = (320, 240)
            # camera.resolution = (320, 120)
            camera.framerate = 15
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
                self.connection.write(struct.pack('L', stream.tell()))
                self.connection.flush()
                stream.seek(0)
                self.connection.write(stream.read())
                stream.seek(0)
                stream.truncate()
            self.connection.write(struct.pack('L', 0))

    def Drive(self):
        s = 0.5
        while True:
            self.msg = self.client.recv(1024).decode()

            if self.msg == 'w':
                self.motor1.forward(speed = s)
                self.motor2.forward(speed = s)

            elif self.msg == 'a':
                self.motor2.forward(speed = s)
                self.motor1.backward(speed = s)

            elif self.msg == 's':
                self.motor1.backward(speed = s)
                self.motor2.backward(speed = s)

            elif self.msg == 'd':
                self.motor2.backward(speed = s)
                self.motor1.forward(speed = s)

            elif self.msg == 'q':
                self.motor1.stop()
                self.motor2.stop()

            elif self.msg == 'x':
                self.connection.close()
                self.client.close()
                break

    def Run(self):
        t1 = threading.Thread(target = self.Vision)
        t2 = threading.Thread(target = self.Drive)

        t1.start()
        t2.start()
        t1.join()
        t2.join()

if __name__ == '__main__':
    ip = input("connect to player: ")
    port = 1234
    car = Car(ip, port)
    car.Run()
