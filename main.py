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
            fileToMap = input("Enter path to the .xml you want to transform\n")
            try:
                rdfTransformer.nameFileToMap("/TestData/NRW/NAS-konform.xml")
                file = input("Enter which mappingfile you want to use!\n Options: alkis_nas_konform, alkis_aaa_basiert OR alkis_vereinfacht\n")
                rdfTransformer.yarrrmlToRML("alkis_nas_konform")
                rdfTransformer.callRDFTransformer(outputPathFolder="NRW")
            except Exception as exception:
                print(exception)
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
