import rdfTransformer
import AlkisDataService
import FusekiConnection
import Neo4jConnection

def endOrRepeatProgram():
    userinput = input("Close Program? Press 'Y' or 'N' \n")
    if userinput == ("N" or "n"):
        start()
    else:
        print("closing programm..\n")

def start():
    userInput = input(
        "Press a number: \n 1: Download ALKIS DATA \n 2: Transform existing ALKIS Data \n 3: SAVE .ttl file to fuseki \n"
        " 4: Enter SPARQL Query\n")
    if userInput == "1":
        bundeslandToMap = input(
            "Enter state you want to download the data from.\n All available data sources are listed here:" + AlkisDataService.outputDic() + "\n")
        try:
            AlkisDataService.getDataFromWFS(bundeslandToMap)
        except Exception:
            print("Something went wrong, try again!\n")
        print("Download was successful! the file can be found under /TestData")
        endOrRepeatProgram()
    elif userInput == "2":
        try:
            fileToMap = input("Enter path to the .xml you want to transform\n")
            rdfTransformer.nameFileToMap(fileToMap)
            rdfTransformer.yarrrmlToRML(fileToMap)
            rdfTransformer.callRDFTransformer(fileToMap)
        except Exception as exception:
            print(exception)
        endOrRepeatProgram()
    elif userInput == "3":
        print("case3\n")
        endOrRepeatProgram()
    elif userInput == "4":
        print("case4\n")
        endOrRepeatProgram()
    else:
        print("Wrong input try again!\n")
        start()


start()