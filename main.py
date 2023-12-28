def on_button_pressed_a():
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global millivolts
    millivolts = Math.round(pins.analog_read_pin(AnalogPin.P0) * 3000 / 1023)
    basic.show_number(millivolts)
    if millivolts < 1200:
        basic.show_icon(IconNames.SAD)
    else:
        basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.B, on_button_pressed_b)

millivolts = 0
basic.show_string("Battery Tester")