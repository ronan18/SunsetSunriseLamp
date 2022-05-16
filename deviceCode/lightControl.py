import time
from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()
uh.set_brightness(1)
global mode
mode = "UH"

import RPi.GPIO as GPIO
import time as time

if mode == "STRIP":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    blueLight = GPIO.PWM(18, 50)
    redLight = GPIO.PWM(22, 50)
    greenLight = GPIO.PWM(6, 50)
    # GPIO18, frequency=50Hz
    redLight.start(0)
    greenLight.start(0)
    blueLight.start(0)





def rgbToPercent(x):
    return (100*x)/255
def setLightColor(red,green,blue):
    global mode
    global redLight
    global blueLight
    global greenLight
    print("setting light color",red,green,blue, mode)
    if mode == "UH":
        uh.clear()
        for x in range(17):
            for y in range(7):
                uh.set_pixel(x, y, red, green, blue)
        uh.show()
    else:
        redLight.ChangeDutyCycle(rgbToPercent(red))
        greenLight.ChangeDutyCycle(rgbToPercent(green))
        blueLight.ChangeDutyCycle(rgbToPercent(blue))
    return

def runGradientFade(startRed, startGreen, startBlue, endRed, endGreen, endBlue, timeInMin):
    resolution = 1000
    timePerStep = (timeInMin*60)/resolution
    redDiff = endRed - startRed
    greenDiff = endGreen - startGreen
    blueDiff = endBlue - startBlue
    colorDiff = 1 - 0.1

    redIncrement = redDiff/resolution
    greenIncrement = greenDiff/resolution
    blueIncrement = blueDiff/resolution
    colorIncrement = colorDiff/resolution

    for i in range(resolution):
        print((i/resolution)*100, "res", 0.1 + colorIncrement)
        uh.set_brightness(0.1 + colorIncrement)
        setLightColor(round(startRed + (redIncrement*i)),round(startGreen + (greenIncrement*i)), round(startBlue + (blueIncrement*i)))
        time.sleep(timePerStep)

    return

#setLightColor(255,255,255)#
#runGradientFade(50,51,77,252,106,56,0.01)