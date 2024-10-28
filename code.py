# Blinky

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
print("Hello! SM, started :",int(time.monotonic()), "sec ago" )
print(dir(board))
while True:
    led.value = True
    time.sleep(.2)
    led.value = False
    time.sleep(.5)
