import json


def getProjektPath():
    configFile = open("config.json")
    configDic = json.load(configFile)
    value = str(configDic["ProjektFolder"])
    return value


def getRmlMapperPath():
    configFile = open("config.json")
    configDic = json.load(configFile)
    value = str(configDic["rmlmapper"])
    return value