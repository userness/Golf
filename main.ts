let stop = 0
hummingbird.startHummingbird()
music.play(music.tonePlayable(880, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
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
        hummingbird.setRotationServo(FourPort.One, 100)
    }
})
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        if (stop == 0) {
            stop = 1
        } else {
            stop = 0
        }
    }
})
