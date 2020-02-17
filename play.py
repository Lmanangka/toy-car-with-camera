import struct
import io
import socket
import pygame
from PIL import Image

class Remote(object):
    def __init__(self, ip, port):
        self.client = socket.socket()
        self.client.connect(('ip', port))
        self.addr = self.client.accept()[0]
        self.connection = self.client.makefile('rb')
        print("connected to ", self.addr)

        pygame.init()
        pygame.display.set_mode([100, 100])

    def Vision(self):
        while True:
            image_len = struct.unpack('<L', self.connection(struct.calcsize('<L')))[0]

            if not image_len:
                break

            stream = io.BytesIO()
            stream.write(self.connection.read(image_len))
            stream.seek(0)
            image = Image.open(stream)
            image.verify()

    def KeyboardControl(self):
        try:
            trig = True
            while trig:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        input = pygame.get_pressed()

                        if input[pygame.K_w]:
                            print("forward")
                            self.com.sendall(str.encode('w'))

                        elif input[pygame.K_a]:
                            print("left")
                            self.com.sendall(str.encode('a'))

                        elif input[pygame.K_s]:
                            print("reverse")
                            self.com.sendall(str.encode('s'))

                        elif input[pygame.K_d]:
                            print("right")
                            self.com.sendall(str.encode('d'))

                        elif input[pygame.K_x]:
                            print("exit")
                            self.com.sendall(str.encode('x'))
                            trig = False
                            break

                    elif event.type == pygame.KEYUP:
                        self.com.sendall(str.encode('q'))

        except KeyboardInterrupt:
            self.com.sendall(str.encode('q'))
            print("KeyboardInterrupt")

        finally:
            self.connection.close()
            self.client.close()

    def Play(self):
        t1 = threading.Thread(target = Remote.Vision)
        t2 = threading.Thread(target = Remote.KeyboardControl)

        t1 = start()
        t2 = start()
        t1 = join()
        t2 = join()


if __name__ == '__main__':
    ip = input("connect to: ")
    port = 1234
    remote = Remote('ip', port)
    remote.Play()
