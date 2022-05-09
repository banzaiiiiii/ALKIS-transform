import Helper
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
        "Press a number: \n 1: Automatically transform data for all available states and output all graph triples!\n "
        "2: Download ALKIS DATA \n 3: Transform existing ALKIS Data \n 4: SAVE .ttl file to fuseki \n"
        " 5: Enter SPARQL Query\n "
        "Type: close to exit!\n ")
    if userInput =="test":
        FusekiConnection.queryDB()
    if userInput == "1":
        userInput = input("How many 'Flurstuecke' per state you want to download? type 'all' or a number!\n")
        if userInput == 'all':
            AlkisDataService.executeShowCaseDownload()
            rdfTransformer.executeShowCaseTransformation()
        else:
            try:
                #AlkisDataService.executeShowCaseDownload(int(userInput))
                # transform .xml files for bra, ham, hes, nrw, sac in .ttl
                #rdfTransformer.executeShowCaseTransformation(int(userInput))
                 # save all the transformed files to fuseki
                #FusekiConnection.executeShowCaseSave(int(userInput))
                 FusekiConnection.queryDB()
            except ValueError:
                print("number must be an int! try again")
                start()
    elif userInput == "2":
        bundeslandToMap = input(
            "Enter state you want to download the data from.\n All available data sources are listed here:" + AlkisDataService.outputDic() + "\n")

        if filter_download():
            try:
                gemarkung = str(input("Optional: Enter gemarkung or gemarkungsnummer!\n"))
                AlkisDataService.getDataFromWFS(bundeslandToMap, gemarkung)
            except Exception:
                print("Something went wrong, try again!\n")
            print("Download was successful! the file can be found under /TestData")
            endOrRepeatProgram()
        else:
            try:
                AlkisDataService.getDataFromWFS(bundeslandToMap)
                print("Download was successful! the file can be found under /TestData")
            except Exception:
                print("Something went wrong, try again!\n")
            endOrRepeatProgram()
    elif userInput == "3":
        try:
            fileToMap = input("Enter path to the .xml you want to transform\n")
            rdfTransformer.nameFileToMap(fileToMap)
            rdfTransformer.yarrrmlToRML(fileToMap)
            rdfTransformer.callRDFTransformer(fileToMap)
        except Exception as exception:
            print(exception)
        endOrRepeatProgram()
    elif userInput == "4":
        path = input("Enter path to .tll file you want to save!\n")
        try:
            FusekiConnection.saveGraph(path)
        except Exception as exception:
            print(exception, "Something went wrong!")
        endOrRepeatProgram()
    elif userInput == "5":
        print("Here you can enter Sparql Queries!\n Not yet implemented\n")
        endOrRepeatProgram()
    elif userInput == "Close" or userInput == "CLOSE" or userInput == "close":
        endProgramm()
    else:
        print("Wrong input try again!\n")
        start()


def endProgramm():
   print("closing programm..\n")


def filter_download():
    filter = input("Do want to specify which data is getting downloaded?(yes or no)")
    if filter == "yes":
        return True
    else:
        return False


start()