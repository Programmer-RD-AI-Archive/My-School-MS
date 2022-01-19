import datetime

import pymongo

"""
This File constantly runs and checks the 2 factor authentication and see's if there is more time remaining for 1 code set.
Ex.
one 2 fac = [2020.05.03.10.10.10]
current time = [2020.05.03.10.10.9]
if one 2 fac == to current time:
    then it will delete the set of code.
    one 2 fac deleted from db
"""


def two_fac_auth_checking() -> None:
    mongodb_link = "mongodb://ranuga:ranuga@ms-shard-00-00.xrgdr.mongodb.net:27017,ms-shard-00-01.xrgdr.mongodb.net:27017,ms-shard-00-02.xrgdr.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-fwaf6t-shard-0&authSource=admin&retryWrites=true&w=majority"
    cluster = pymongo.MongoClient(mongodb_link)
    db = cluster["2FACAUTH"]
    collection = db["2FACAUTH"]
    while True:
        for result in collection.find({}):
            time = result["time"]  # getting the databases object time started
            time = time.split(
                " "
            )  # splitting the time so it is like [2020,05,03,05,etc..] [year,month,date,hour,etc..]
            time[4] = str(
                int(time[4]) + 15
            )  # in the min section it adds 15 mins becuase the time that is allowed for codes in 2 factor authentication is 15 min
            if int(time[4]) > 60:  # these are excpetion
                time[4] = str(int(time[4]) - 60)  # these are excpetion
                time[3] = str(int(time[3]) + 1)  # these are excpetion
            if int(time[3]) > 24:  # these are excpetion
                time[3] = str(int(time[3]) - 24)  # these are excpetion
                time[2] = str(int(time[2]) + 1)  # these are excpetion
            now_time = (
                str(datetime.datetime.now().year)
                + " "
                + str(datetime.datetime.now().month)
                + " "
                + str(datetime.datetime.now().day)
                + " "
                + str(datetime.datetime.now().hour)
                + " "
                + str(datetime.datetime.now().minute)
            )  # getting the current time
            now_time = now_time.split(
                " "
            )  # splitting the time to a list so the time and now_time is in same format
            if time == now_time:  # if time is now_time then
                collection.delete_one(
                    result
                )  # the code sets are deleted from the collections so the person will need to create a new set of codes


two_fac_auth_checking()
