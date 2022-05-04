import time
def setLightColor(red,green,blue):
    print("setting light color",red,green,blue)
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
        setLightColor(round(startRed + (redIncrement*i)),round(startGreen + (greenIncrement*i)), round(startRed + (redIncrement*i)))
        time.sleep(timePerStep)

    return

#runGradientFade(15,200,130,255,255,255,1)