import socket
import picamera
import io
import struct
import time
import smbus
import threading

class Car(object):
    def __init__(self, ip, port):
        self.client = socket.socket()
        self.client.connect((ip, port))
        self.connection = self.client.makefile('wb')

        self.address = 0x04
        self.i2c = smbus.SMBus(1)
        self.msg = None

    def Vision(self):
        with picamera.PiCamera() as camera:
            camera.rotation = 180
            camera.resolution = (640, 480)
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
            self.connection.write(struct.pack('<L', 0))

    def Drive(self):
        while True:
            self.msg = self.client.recv(1024).decode()

            if self.msg == 'w':
                self.i2c.write_byte(self.address, 0)

            elif self.msg == 'a':
                self.i2c.write_byte(self.address, 1)

            elif self.msg == 's':
                self.i2c.write_byte(self.address, 2)

            elif self.msg == 'd':
                self.i2c.write_byte(self.address, 3)

            elif self.msg == 'q':
                self.i2c.write_byte(self.address, 4)

            elif self.msg == 'x':
                self.i2c.write_byte(self.address, 5)
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
    ip = input("coneect to server: ")
    port = 1234
    car = Car(ip, port)
    car.Run()
