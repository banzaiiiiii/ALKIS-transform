from rdfTransformer import *
from Neo4jConnection import *
from AlkisDataService import *
from FusekiConnection import *

#download alkis data, with "gemeindenummer"
#apiResponse = getDataAsDownload("Sachsen", "14522490")

#getDataFromWFS()



# input which .xml file you want to map
#nameFileToMap("/TestData/Sachsen/14522490/147602.xml")

# Umwandlung von yaaarml rules to rml rules
#yarrrmlToRML()

#Umwandlung der Daten zu .ttl
#callRDFTransformer(outputPathFolder="NRW")
# speicherung in neo4j db
#saveToNeo4j()




#example output from neo4j
#outPutFromNeo4j()

fusekiConnection()


'''
text abfrage: welche gemeindenummer wollen sie mappen? 
input gemeindenummer.
try download gemeindenummer!
pic yarrml file
map and transform to ttl and save to db 
beispiel abfrage! 

'''