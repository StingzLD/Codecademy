from adafruit_circuitplayground.express import cpx
from time import sleep
import board
import touchio

touch = touchio.TouchIn(board.A1)

while True:
    if cpx.switch:
        if cpx.button_a:
            print("Temperature:", cpx.temperature)
            sleep(0.25)

        if cpx.button_b:
            print("Light:",cpx.light)
            sleep(0.25)
    else:
        print(touch.raw_value)
        sleep(0.5)
