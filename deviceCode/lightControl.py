import time
from unicornhatmini import UnicornHATMini
uh = UnicornHATMini()
uh.set_brightness(1)
global mode
mode = "UH"
def setLightColor(red,green,blue):
    global mode
    print("setting light color",red,green,blue, mode)
    if mode == "UH":
        uh.clear()
        for x in range(17):
            for y in range(7):
                uh.set_pixel(x, y, red, green, blue)
        uh.show()
    return

def runGradientFade(startRed, startGreen, startBlue, endRed, endGreen, endBlue, timeInMin):
    resolution = 1000
    timePerStep = (timeInMin*60)/resolution
    redDiff = endRed - startRed
    greenDiff = endGreen - startGreen
    blueDiff = endBlue - startBlue

    redIncrement = redDiff/resolution
    greenIncrement = greenDiff/resolution
    blueIncrement = blueDiff/resolution

    for i in range(resolution):
        print(i)
        setLightColor(round(startRed + (redIncrement*i)),round(startGreen + (greenIncrement*i)), round(startRed + (blueIncrement*i)))
        time.sleep(timePerStep)

    return

#setLightColor(255,255,255)
runGradientFade(50,51,77,252,106,56,0.1)