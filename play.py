import socket
import pygame
import threading
import io
import struct
from PIL import Image
import cv2
import numpy as np

class Remote(object):
    def __init__(self):
        self.server = socket.socket()
        self.server.bind(('0.0.0.0', 1234))
        self.server.listen(0)
        self.com, self.addr = self.server.accept()
        self.connection = self.com.makefile('rb')
        print("connected to ", self.addr)

        pygame.init()
        pygame.display.set_mode([100, 100])

    def Vision(self):
        while True:
            im = struct.unpack('<L', self.connection.read(struct.calcsize('<L')))[0]
            if not im:
                break

            stream = io.BytesIO()
            stream.write(self.connection.read(im))
            stream.seek(0)
            image = Image.open(stream)

            vid = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            cv2.imshow('eye', vid)

            if cv2.waitKey(1) & 0xFF == ord('x'):
                break

    def Drive(self):
        try:
            trig = True
            while trig:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        input = pygame.key.get_pressed()

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
            self.server.close()
            cv2.destroyAllWindows()

    def Play(self):
        t1 = threading.Thread(target = self.Vision)
        t2 = threading.Thread(target = self.Drive)

        t1.start()
        t2.start()
        t1.join()
        t2.join()


if __name__ == '__main__':
    remote = Remote()
    remote.Play()
