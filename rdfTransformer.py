from subprocess import *
from datetime import datetime
import fileinput
import Helper


def yarrrmlToRML(file):
    mappingFileFolderPath = Helper.getProjektPath() + "MappingFiles/"
    mappingFile = pickMappingFile(file)
    #og = 'yarrrml-parser -i "D://repos/Uni/Ba/ALKIS-transform/MappingFiles/'+mappingFile+'"'+' -o "D://repos/Uni/BA/ALKIS-transform/MappingFiles/R2RML-Mapping.ttl" --pretty'
    callToYarrrmlParser = 'yarrrml-parser -i "' + mappingFileFolderPath + mappingFile + '"' + ' -o "' + mappingFileFolderPath + "R2RML-Mapping.ttl" + '"' + ' --pretty'
    process = Popen(
        callToYarrrmlParser,
        stdout=PIPE, stderr=PIPE, shell=True)
    result = process.communicate()
    print(result)

def callRDFTransformer(fileToMap, outputFile=None):
    bundesland = fileToMap[9:12]
    outputFolderPath = Helper.getProjektPath() + "Output/" + bundesland
    if not outputFile:
        outputFile = outputFolderPath + "/" + str(
            datetime.now().strftime("%Y-%m-%d-%I-%M-%S")) + ".ttl"
    process = Popen(['java', '-jar', Helper.getRmlMapperPath(), "-m", Helper.getProjektPath() + "MappingFiles/R2RML-Mapping.ttl", "-o", outputFile, "-s", "turtle"], stdout=PIPE,
                    stderr=PIPE)
    result = process.communicate()
    print(result)


def pickMappingFile(FileName):
    mappingFile = ""
    if "NAS" in FileName:
        mappingFile = "alkis_nas_konform.yml"
    elif "AAA" in FileName:
        mappingFile = "alkis_aaa_basiert.yml"
    elif ("vereinfacht" in FileName):
        mappingFile = "alkis_vereinfacht.yml"
    return mappingFile


# changes the .xml file that is getting accessed in the .yarrrml mapping file
def nameFileToMap(FileName):
    mappingFilePath = Helper.getProjektPath() + "MappingFiles/" + pickMappingFile(FileName)
    with fileinput.FileInput(mappingFilePath,
                             inplace=True) as f:
        for line in f:
            if (line.startswith("      - access:") == True):
                print("      - access: " + FileName, end='\n')
            elif(line.startswith("      access:") == True):
                print("      access: " + FileName, end='\n')
            else:
                print(line, end='')


def executeShowCaseTransformation(maxIndex=None):
    # für Bra/Ham/Hes/NRW/Sac .xml umwandeln
    StartIndex = 0
    filesToTransform = [
                        "TestData/Bra/vereinfachtes-schema" + str(StartIndex) + ".xml",
                        "TestData/Ham/vereinfachtes-schema" + str(StartIndex) + ".xml",
                        "TestData/Hes/vereinfachtes-schema" + str(StartIndex) + ".xml",
                        "TestData/NRW/vereinfachtes-schema" + str(StartIndex) + ".xml",
                        "TestData/Sac/vereinfachtes-schema" + str(StartIndex) + ".xml"
                        ]

    for file in filesToTransform:
        StartIndex = 0
        while (True):
            if maxIndex is not None and StartIndex >= maxIndex:
                print("Transformation finished!\n")
                break
            try:
                fileWithIndex = file
                outputPath = Helper.getProjektPath() + "Output/" + file[9:12] + "/showCaseFile" + str(StartIndex) + ".ttl"
                nameFileToMap(fileWithIndex)
                yarrrmlToRML(fileWithIndex)
                callRDFTransformer(fileWithIndex, outputPath)
                #Helper.convertStateNamesForDBpedia(file)
                print("the file " + fileWithIndex + " got transformed successfully!")
                StartIndex += 1000
            except Exception as e:
                print(e)
                break