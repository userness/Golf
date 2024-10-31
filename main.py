def on_button_pressed_a():
    global stop
    if stop == 0:
        stop = 1
    else:
        stop = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

stop = 0
hummingbird.start_hummingbird()
music.play(music.tone_playable(880, music.beat(BeatFraction.WHOLE)),
    music.PlaybackMode.IN_BACKGROUND)
stop = 0
basic.show_string("Grinch")

def on_forever():
    if stop != 1:
        hummingbird.set_position_servo(FourPort.ONE, 90)
        basic.pause(500)
        hummingbird.set_position_servo(FourPort.ONE, 0)
        basic.pause(500)
basic.forever(on_forever)

def on_forever2():
    if stop != 1:
        hummingbird.set_rotation_servo(FourPort.TWO, 70)
    else:
        hummingbird.set_rotation_servo(FourPort.TWO, 0)
basic.forever(on_forever2)

def on_forever3():
    if stop != 1:
        hummingbird.set_led(ThreePort.ONE, 100)
        basic.pause(100)
        hummingbird.set_led(ThreePort.ONE, 0)
        basic.pause(100)
basic.forever(on_forever3)

def on_forever4():
    hummingbird.set_tri_led(TwoPort.TWO, 255, 0, 0)
    hummingbird.set_tri_led(TwoPort.ONE, 0, 255, 0)
    basic.pause(100)
    hummingbird.set_tri_led(TwoPort.TWO, 0, 255, 0)
    hummingbird.set_tri_led(TwoPort.ONE, 255, 0, 0)
basic.forever(on_forever4)
