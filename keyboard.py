# simple example demonstrating how to control a Tello using your keyboard.
# For a more fully featured example see manual-control-pygame.py
# 
# Use W, A, S, D for moving, E, Q for rotating and R, F for going up and down.
# When starting the script the Tello will takeoff, pressing ESC makes it land
#  and the script exit.

from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()


tello.takeoff()

while True:

    key = input('Move: ')

    if key == 27: # ESC
        break
    elif key == 'w':
        tello.move_forward(30)
    elif key == 's':
        tello.move_back(30)
    elif key == 'a':
        tello.move_left(30)
    elif key == 'd':
        tello.move_right(30)
    elif key == 'e':
        tello.rotate_clockwise(30)
    elif key == 'q':
        tello.rotate_counter_clockwise(30)
    elif key == 'r':
        tello.move_up(30)
    elif key == 'f':
        tello.move_down(30)
    elif key == 'o':
        tello.flip_forward()

tello.land()