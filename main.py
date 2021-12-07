from rdfTransformer import jarWrapper
from Neo4jConnection import createTestGraph
import rdflib
import neo4j

# rdfTransformer wird aufgerufen
# testmapping filePath wird übergeben
# ouput .ttl wird gespeichert

fileName = "D://repos/Uni/BA/rmlmapper-java/target/rmlmapper-4.12.0-r358-all.jar"
arg1 = "-m"
arg2 = "D://repos/Uni/BA/pythonProject/Input/example-json-mapping.ttl"

arg3 = "-o"
arg4 = "D://repos/Uni/BA/pythonProject/Output/test.ttl"

#result = jarWrapper(fileName, arg1, arg2, arg3, arg4)



result = createTestGraph()