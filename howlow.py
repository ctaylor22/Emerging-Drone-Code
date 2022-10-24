from djitellopy import tello

me = tello.Tello()

me.connect()
print(me.get_battery())
me.takeoff()

me.move_down(50)
me.move_forward(100)
me.land()