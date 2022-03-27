import rdfTransformer
import AlkisDataService
import FusekiConnection
import Neo4jConnection

while True:
    try:
        inputNumber = input(
            "Press a number: \n 1: Download ALKIS DATA \n 2: Transform existing ALKIS Data \n 3: SAVE .ttl file to fuseki \n"
            " 4: Enter SPARQL Query\n type 'CLOSE' for closing the program \n")
        print(inputNumber)
        if inputNumber == "1":  # Download and MAP ALKIS Data
            bundeslandToMap = input("Enter state you want to download the data from.\n")
            if bundeslandToMap == ("Sachsen" or "Saxony" or "sachsen" or "saxony"):
                AlkisDataService.getDataAsDownload("Sachsen", "14522490")
            if (bundeslandToMap == "Caps"):
                AlkisDataService.getCapabilities()
            else:
                AlkisDataService.getDataFromWFS(bundeslandToMap)
            break
        if inputNumber == "2":  # Map existing .xml file
            defaultFile = "/TestData/dataFromWFS.xml"
            fileToMap = input("Enter path to the .xml you want to transform\n")
            try:
                rdfTransformer.nameFileToMap(fileToMap)
                rdfTransformer.yarrrmlToRML()
                rdfTransformer.callRDFTransformer(outputPathFolder="NRW")
            except Exception as exception:
                print(exception)
            else:
                print("default file has been picked for transformation")
                rdfTransformer.nameFileToMap(defaultFile)
                rdfTransformer.yarrrmlToRML()
                rdfTransformer.callRDFTransformer(outputPathFolder="NRW")
            break
        if inputNumber == "3":  # save .ttl to db
            path = input("Enter path to .tll file you want to save!\n")
            defaultPath = "D://repos/Uni/BA/ALKIS-transform/Output/nrw/2022-03-09.ttl"
            try:
                FusekiConnection.saveGraph(path)
            except Exception as exception:
                print(exception, "Something went wrong!")
            break
        if inputNumber == "4":  # Sparql Query
            print("Querys are not implemented yet!")
            break
        if inputNumber == "close" or "CLOSE" or "exit":
            break
        else:
            print("Input a valid number!")
    except Exception as exception:
        print(exception)

'''
text abfrage: welche gemeindenummer wollen sie mappen? 
input gemeindenummer.
try download gemeindenummer!
pic yarrml file
map and transform to ttl and save to db 
beispiel abfrage! 

'''
