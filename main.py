hummingbird.start_hummingbird()

def on_forever():
    stop = 0
    if not (input.button_is_pressed(Button.A)) or stop == 1:
        hummingbird.set_position_servo(FourPort.ONE, 90)
        basic.pause(500)
        hummingbird.set_position_servo(FourPort.ONE, 0)
        basic.pause(500)
basic.forever(on_forever)

def on_forever2():
    if input.button_is_pressed(Button.A):
        stop2 = 1
basic.forever(on_forever2)
