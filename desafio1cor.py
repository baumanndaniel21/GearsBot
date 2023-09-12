#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
btn = Button()
radio = Radio()

ultrasonic_sensor_in1 = UltrasonicSensor(INPUT_1)
color_sensor_in2 = ColorSensor(INPUT_2)


# Here is where your code starts

# Descreva esta função...
def left():
    steering_drive.on_for_rotations((-100), 20, 0.6)

# Descreva esta função...
def right():
    steering_drive.on_for_rotations(100, 20, 0.6)

# Descreva esta função...
def forward():
    steering_drive.on_for_rotations(0, 20, 1)

# Descreva esta função...
def stop():
    tank_drive.off(brake=True)


while not color_sensor_in2.color == 5:
    forward()
stop()
