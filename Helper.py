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


def getQueryEndpoint():
    configFile = open("config.json")
    configDic = json.load(configFile)
    value = str(configDic["fuseki_query_endpoint"])
    return value


def getUpdateEndpoint():
    configFile = open("config.json")
    configDic = json.load(configFile)
    value = str(configDic["fuseki_update_endpoint"])
    return value