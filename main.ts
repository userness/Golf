let stop = 0
hummingbird.startHummingbird()
basic.forever(function () {
    if (!(input.buttonIsPressed(Button.A)) || stop == 1) {
        hummingbird.setPositionServo(FourPort.One, 90)
        basic.pause(500)
        hummingbird.setPositionServo(FourPort.One, 0)
        basic.pause(500)
    }
})
basic.forever(function () {
    let stop2: number;
if (input.buttonIsPressed(Button.A)) {
        stop = 1
    }
})
