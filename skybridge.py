from djitellopy import tello

me = tello.Tello()

me.connect()
print(me.get_battery())
me.takeoff()

# MOVE UP TO 2nd SKYBRIDGE
me.move_up(500)
me.move_up(500)
me.move_up(500)
me.move_up(500)
me.move_up(500)
me.move_up(500)

# # MOVE FORWARD OVER BRIDGE
# me.move_forward(500)
# me.move_forward(500)

# MOVE DOWN TO 1st SKYBRIDGE
me.move_down(500)
me.move_down(500)
me.move_down(500)

me.rotate_clockwise(180)

# # MOVE FORWARD OVER BRIDGE
# me.move_forward(500)
# me.move_forward(500)


me.land()

