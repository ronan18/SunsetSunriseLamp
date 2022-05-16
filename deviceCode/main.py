import pymongo
import json
import schedule
import time
import lightControl
with open('../private/keys.json') as f:
    keys = json.load(f)

mongoKey = keys["mongoKey"]
client = pymongo.MongoClient(f"mongodb+srv://server:{mongoKey}@sunrisesunsetlamp.vqjpt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["sunrise-sunset"]

global sunriseJob
global lightConfig
global sunsetJob
sunriseJob = False
lightConfig = False
sunsetJob = False

def getConfigFor(id):
    return db["configurations"].find_one({"configID": id})


def runner():
    global lightConfig
    global sunriseJob
    global sunsetJob
    print("updating config")
    lightConfig = getConfigFor("testing")
    print(lightConfig, "updated config")
    if (sunriseJob):
        schedule.cancel_job(sunriseJob)
    if (sunsetJob):
            schedule.cancel_job(sunsetJob)
    sunriseJob = schedule.every().day.at(lightConfig["sunriseStart"]).do(runSunriseSequence)
    sunsetJob = schedule.every().day.at(lightConfig["sunsetStart"]).do(runSunsetSequence)
    all_jobs = schedule.get_jobs()
   # print(all_jobs, "job summery")

def runSunriseSequence():
    global lightConfig
    print("running sunrise sequence")
    lightControl.runGradientFade(int(lightConfig["sunriseRed"])-10,int(lightConfig["sunriseGreen"])-10, int(lightConfig["sunriseBlue"])-10,int(lightConfig["sunriseRed"]),int(lightConfig["sunriseGreen"]), int(lightConfig["sunriseBlue"]), int(lightConfig["sunriseRunTimeInMin"]))


def runSunsetSequence():
    global lightConfig
    print("running sunset sequence")
    lightControl.runGradientFade(int(lightConfig["sunsetRed"])-10,int(lightConfig["sunsetGreen"])-10, int(lightConfig["sunsetBlue"])-10,int(lightConfig["sunsetRed"]),int(lightConfig["sunsetGreen"]), int(lightConfig["sunsetBlue"]), int(lightConfig["sunsetRunTimeInMin"]))




sunriseJob = schedule.every().day.at('07:00').do(runSunriseSequence)
sunsetJob = schedule.every().day.at('21:00').do(runSunsetSequence)
runner()

schedule.every(20).seconds.do(runner)

while True:
    schedule.run_pending()
    time.sleep(1)