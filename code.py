import time
import board
import digitalio

red_led = digitalio.DigitalInOut(board.GP12)
red_led.direction = digitalio.Direction.OUTPUT
amber_led = digitalio.DigitalInOut(board.GP13)
amber_led.direction = digitalio.Direction.OUTPUT
green_led = digitalio.DigitalInOut(board.GP14)
green_led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP28)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    print(button.value)
    time.sleep(0.5)
    red_led.value = True
    time.sleep(5)
    amber_led.value = True
    time.sleep(2)
    red_led.value = False
    amber_led.value = False
    green_led.value = True
    time.sleep(5)
    green_led.value = False
    amber_led.value = True
    time.sleep(3)
    amber_led.value = False