import fileinput
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


def convertStateNamesForDBpedia(FileName):
    with fileinput.FileInput(FileName,
                             inplace=True) as f:
        for line in f:
            if (line.contains("Nordrhein-Westfalen") == True):
                print("North_Rhine_Westphalia", end='\n')
            else:
                print(line, end='')

