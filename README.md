# Toy Car with Camera

Toy car with Picamera and Raspberry pi using python

![Image of Raspberry Pi car](https://github.com/Lmanangka/toy-car-with-camera/blob/master/img/Rpi-car.jpg?raw=true)

![Image of Raspberry Pi car driver motor](https://github.com/Lmanangka/toy-car-with-camera/blob/master/img/Rpi-car-Driver-Motor.jpg?raw=true)

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

python 3.7
```shell
python3 -m pip install -U pygame --user
```
python 3.8
```shell
python3 -m pip install -U pygame==2.0.0.dev6 --user
```
Check this [Pygame installation](https://www.pygame.org/wiki/GettingStarted) if having troubles

## Block Diagram with Arduino

![Image of block diagram with Arduino](https://github.com/Lmanangka/toy-car-with-camera/blob/master/img/Rpi-car-with-arduino.png?raw=true)

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

![Image of block diagram without Arduino](https://github.com/Lmanangka/toy-car-with-camera/blob/master/img/Rpi-car-without-arduino.png?raw=true)

### Jumper from Raspberry Pi GPIO to Driver Motor

here is the link for [Raspberry Pi GPIO](https://pinout.xyz/#) or type this in Raspberry Pi terminal
```shell
pinout
```

Rpi GPIO ------------> Driver Motor
* GPI0 --------------> IN1
* GPIO --------------> IN2
* GPIO --------------> IN3
* GPIO --------------> IN4
* GND ---------------> GND

## How To Use It

1. Run this code from laptop/PC
```shell
play.py
```
2. Run this code if using Arduino
```shell
car.py
```
or run this code without Arduino
```shell
car-without-arduino.py
```
3. From Raspberry Pi terminal connect to Laptop/PC using IP address

## Author:

* [**Leonardo Rudolf Manangka**](https://github.com/Lmanangka)

## Acknowledgements:

* Raspberry Pi Picamera streaming data over wifi [reference](https://github.com/hamuchiwa/AutoRCCar)

* Sending data and receiving data [reference](https://www.youtube.com/watch?v=Lbfe3-v7yE0)
