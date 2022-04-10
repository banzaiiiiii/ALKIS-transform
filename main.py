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
        path = input("Enter path to .tll file you want to save!\n")
        try:
            FusekiConnection.saveGraph(path)
        except Exception as exception:
            print(exception, "Something went wrong!")
        endOrRepeatProgram()
    elif userInput == "4":
        print("Here you can enter Sparql Queries!\n Not yet implemented\n")
        endOrRepeatProgram()
    else:
        print("Wrong input try again!\n")
        start()


start()