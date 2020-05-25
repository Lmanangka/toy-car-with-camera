# Toy Car with Camera

Toy car with Picamera and Raspberry pi using python
![Image of Raspberry Pi car](https://github.com/Lmanangka/toy-car-with-camera/tree/master/img/Rpi-car.jpg)

![Image of Raspberry Pi car driver motor](https://github.com/Lmanangka/toy-car-with-camera/tree/master/img/Rpi-car-Driver-Motor)

## Requirement

* Raspberry Pi
* Picamera
* Motor Driver
* DC Motor(L298 H-Bridge)
* Arduino Nano(Optional)
* Car Body
* Battery and Power bank for driver motor and Raspberry Pi
* Cable Jumper
* Laptop or PC

## Install Pygame

for python 3.7
> python3 -m pip install -U pygame --user >

for python 3.8
> python3 -m pip install -U pygame==2.0.0.dev6 --user >

Check this [Pygame installation](https://www.pygame.org/wiki/GettingStarted) if having troubles

## Block Diagram with Arduino

![Image of Block Diagram with Arduino](https://github.com/Lmanangka/toy-car-with-camera/tree/master/img/Rpi-car-with-arduino.png)

### Jumper from Arduino Nano to Driver Motor

Use PWM pin in Arduino to control motors speed
here is the links for [Arduino PWM pin](https://www.arduino.cc/reference/en/language/functions/analog-io/analogwrite/) and [Arduino PWM tutorial](https://www.arduino.cc/en/tutorial/PWM)

Arduino Nano ------> Driver Motor
* D11 -------------> IN1
* D10 -------------> IN2
* D9 --------------> IN3
* D6 --------------> IN4
* GND -------------> GND
* 5V --------------> 5V <<-------- to power Arduino nano with battery

## Block Diagram without Arduino

![Image of Block Diagram without Arduino](https://github.com/Lmanangka/toy-car-with-camera/tree/master/img/Rpi-car-without-arduino.png)

### Jumper from Raspberry Pi GPIO to Driver Motor

here is the link for [Raspberry Pi GPIO](https://pinout.xyz/#) or type in Raspberry Pi terminal > pinout >.

Rpi GPIO ------------> Driver Motor
* GPI0 --------------> IN1
* GPIO --------------> IN2
* GPIO --------------> IN3
* GPIO --------------> IN4
* GND ---------------> GND

## How To Use It

1. Run > play.py > from Laptop/PC
2. Run > car.py > (using Arduino) or > car-without-arduino.py > (without Arduino) from Raspberry Pi Terminal
3. From Raspberry Pi terminal connect to Laptop/PC using IP address

## Author:

* [**Leonardo Rudolf Manangka**](https://github.com/Lmanangka)

## Acknowledgements:

* Raspberry Pi Picamera streaming data over wifi [reference](https://github.com/hamuchiwa/AutoRCCar)

* Sending data and receiving data [reference](https://www.youtube.com/watch?v=Lbfe3-v7yE0)
