X = 0
Y = 0

def on_button_pressed_a():
    global X, Y
    X = 0
    Y = 0
    for index in range(5):
        led.plot(X, Y)
        X += 1
        basic.pause(300)
    Y += 1
    X = 1
    for index2 in range(3):
        led.plot(X, Y)
        X += 1
        basic.pause(300)
    Y += 1
    X = 2
    led.plot(X, Y)
    basic.pause(300)
    Y += 1
    X = 1
    for index3 in range(3):
        led.plot(X, Y)
        X += 1
        basic.pause(300)
    Y += 1
    X = 0
    for index4 in range(5):
        led.plot(X, Y)
        X += 1
        basic.pause(300)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
