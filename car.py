import socket
import picamera
import io
import struct
import time
import smbus
import threading

class Car(object):
    def __init__(self):
        self.server = socket.socket()
        self.server.bind(('0.0.0.0', 1234))
        self.server.listen(0)
        self.com, self.addr = self.server.accept()[0]
        self.connection = self.com.makefile('wb')
        print("connected to", self.addr)

        address = 0x04
        self.i2c = smbus.SMBus(1)
        self.msg = None

    def Vision(self):
        with picamera.PiCamera() as camera:
            camera.rotation = 180
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(2)

            stream - io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg'):
                self.connection.write(struct.pack('<L', stream.tell()))
                self.connection.flush()
                stream.seek(0)
                self.connection.write(stream.read())
                stream.seek(0)
                stream.truncate()
            self.connection.write(struct.pack('<L', 0))

    def Drive(self):
        while True:
            self.msg = self.server.recv(1024).decode()

            if msg == 'w':
                self.i2c.write_byte(self.address, 0)

            elif msg == 'a':
                self.i2c.write_byte(self.address, 1)

            elif msg == 's':
                self.i2c.write_byte(self.address, 2)

            elif msg == 'd':
                self.i2c.write_byte(self.address, 3)

            elif msg == 'q':
                self.i2c.write_byte(self.address, 4)

            elif msg == 'x':
                self.i2c.write_byte(self.address, 5)
                self.connection.close()
                self.server.close()
                break

    def Run(self):
        t1 = threading.Thread(target = Car.Vision)
        t2 = threading.Thread(target = Car.Drive)

        t1.start()
        t2.start()
        t1.join()
        t2.join()

if __name__ == '__main__':
    car = Car()
    car.Run()
