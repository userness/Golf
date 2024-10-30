input.onButtonPressed(Button.A, function () {
    if (stop == 0) {
        stop = 1
    } else {
        stop = 0
    }
})
let stop = 0
hummingbird.startHummingbird()
music.play(music.tonePlayable(880, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
stop = 0
basic.showString("Grinch")
basic.forever(function () {
    if (stop != 1) {
        hummingbird.setPositionServo(FourPort.One, 90)
        basic.pause(500)
        hummingbird.setPositionServo(FourPort.One, 0)
        basic.pause(500)
    }
})
basic.forever(function () {
    if (stop != 1) {
        hummingbird.setRotationServo(FourPort.Two, 100)
    }
})
basic.forever(function () {
    hummingbird.setTriLED(
    TwoPort.Two,
    255,
    0,
    0
    )
    hummingbird.setTriLED(
    TwoPort.One,
    0,
    255,
    0
    )
    basic.pause(100)
    hummingbird.setTriLED(
    TwoPort.Two,
    0,
    255,
    0
    )
    hummingbird.setTriLED(
    TwoPort.One,
    255,
    0,
    0
    )
})
basic.forever(function () {
	
})
