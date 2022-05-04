import pymongo
import json
import schedule
import time

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
    print("running sunrise sequence")


def runSunsetSequence():
    print("running sunset sequence")


sunriseJob = schedule.every().day.at('07:00').do(runSunriseSequence)
sunsetJob = schedule.every().day.at('18:00').do(runSunsetSequence)
runner()

schedule.every(1).minutes.do(runner)

while True:
    schedule.run_pending()
    time.sleep(1)