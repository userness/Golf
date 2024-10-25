hummingbird.start_hummingbird()
music.play(music.tone_playable(880, music.beat(BeatFraction.WHOLE)),
    music.PlaybackMode.IN_BACKGROUND)
stop = 0

def on_forever():
    if stop != 1:
        hummingbird.set_position_servo(FourPort.ONE, 90)
        basic.pause(500)
        hummingbird.set_position_servo(FourPort.ONE, 0)
        basic.pause(500)
basic.forever(on_forever)

def on_forever2():
    if stop != 1:
        hummingbird.set_rotation_servo(FourPort.ONE, 100)
basic.forever(on_forever2)

def on_forever3():
    global stop
    if input.button_is_pressed(Button.A):
        if stop == 0:
            stop = 1
        else:
            stop = 0
basic.forever(on_forever3)
