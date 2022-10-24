from djitellopy import tello

me = tello.Tello()

me.connect()
print(me.get_battery())
me.takeoff()

me.move_up(50)
me.curve_xyz_speed(25, -25, 0, 25, -75, 0, 20)

me.land()

