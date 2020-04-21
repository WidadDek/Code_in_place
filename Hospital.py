from karel.stanfordkarel import *


# File: hospital.py
# -----------------------------
# Here is a place to program your section problem
def main():
    move()
    build_hospital()
    for i in range(4):
        move()
    build_hospital()
    move()
    move()
    build_hospital()


def build_hospital():
    move()
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()
