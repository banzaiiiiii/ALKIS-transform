from subprocess import *
import os.path
from datetime import date
import fileinput

rmlMapperPath = "D://repos/Uni/BA/rmlmapper-java/target/rmlmapper-4.12.0-r358-all.jar"
arg1 = "-m"
mappingRules = "D://repos/Uni/BA/ALKIS-transform/MappingFiles/yarrrml.ttl"
arg3 = "-o"

def yarrrmlToRML():
    process = Popen('yarrrml-parser -i "D://repos/Uni/Ba/ALKIS-transform/MappingFiles/AlkisXMLMapping.yml" -o "D://repos/Uni/BA/ALKIS-transform/MappingFiles/yarrrml.ttl" ', stdout=PIPE, stderr=PIPE, shell=True)
    result = process.communicate()
    print(result[0].decode('utf-8'))


def callRDFTransformer(outputPathFolder):
    fileName = "D://repos/Uni/BA/ALKIS-transform/Output/" + outputPathFolder + "/" + str(date.today()) + ".ttl"
    process = Popen(['java', '-jar', rmlMapperPath, arg1, mappingRules, arg3, fileName], stdout=PIPE, stderr=PIPE)
    result = process.communicate()
    print(result[0].decode('utf-8'))
    print(process)


# changes the .xml file that is getting accessed in the .yarrrml mapping file
def nameFileToMap(FileName):
    with fileinput.FileInput("D://repos/uni/ba/alkis-transform/input/alkisxmlmapping.yml", inplace=True) as f:
        for line in f:
            if (line.startswith("      - access:") == True):
                print("      - access: " + FileName, end='\n')
            else:
                print(line, end='')


''' 
def nameFile(outputPathFolder):
    standartFileName = "D://repos/Uni/BA/ALKIS-transform/Output/" + outputPathFolder + "/outputFile"
    doesFileExist = os.path.isfile(standartFileName)
    if doesFileExist == True:
        filename = standartFileName + "1.ttl"
    else:
        filename = standartFileName + ".ttl"
    return filename
'''

# output path         -o "D://repos/Uni/BA/ALKIS-transform/Output/test3.ttl"