#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
clr_sense = ColorSensor(Port.S3)
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor,right_motor,55,142)

# Define variables
threshold = 10
speed = 100
turn = 20

# ---- MAIN LOOP ----
while clr_sense.color() != Color.RED:
    if clr_sense.reflection() > threshold:
        robot.drive(speed,turn)
    else:
        robot.drive(speed,turn*-1)