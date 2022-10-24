from time import sleep
from djitellopy import tello

# 30.48 = 1 ft
FOOT = 30

me = tello.Tello()

me.connect()
print(me.get_battery())
me.takeoff()
# me.move_down(FOOT)
me.move_forward(250)
me.move_up(90)
me.move_forward(200)
me.land()