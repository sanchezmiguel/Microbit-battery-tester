input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(pins.analogReadPin(AnalogPin.P0))
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    millivolts = Math.round(pins.analogReadPin(AnalogPin.P0) * 3000 / 1023)
    basic.showNumber(millivolts)
    if (millivolts < 1200) {
        basic.showIcon(IconNames.Sad)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    
})
let millivolts = 0
basic.showString("Battery Tester")
