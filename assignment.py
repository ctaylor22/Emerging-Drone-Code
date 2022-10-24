from djitellopy import tello

me = tello.Tello()

me.connect()
print(me.get_battery())
me.takeoff()

me.move_forward()
me.move_up()
me.land()