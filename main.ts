let X = 0
let Y = 0
input.onButtonPressed(Button.A, function () {
    X = 0
    Y = 0
    for (let index = 0; index < 5; index++) {
        led.plot(X, Y)
        X += 1
        basic.pause(300)
    }
    Y += 1
    X = 1
    for (let index = 0; index < 3; index++) {
        led.plot(X, Y)
        X += 1
        basic.pause(300)
    }
    Y += 1
    X = 2
    led.plot(X, Y)
    basic.pause(300)
    Y += 1
    X = 1
    for (let index = 0; index < 3; index++) {
        led.plot(X, Y)
        X += 1
        basic.pause(300)
    }
    Y += 1
    X = 0
    for (let index = 0; index < 5; index++) {
        led.plot(X, Y)
        X += 1
        basic.pause(300)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
})
basic.forever(function () {
	
})
