# ALKIS-transform
Projekt for bachelor thesis - Transformation von ALKIS Daten in semantische Formate 

## How to use 
clone this repo 

install yarrrml-parser https://github.com/RMLio/yarrrml-parser

install rmlmapper https://github.com/RMLio/rmlmapper-java 

if you want to query or save data you need to setup a apache jena fuseki server  

change Paths in config.json 
	
  
## geplante Funktionsweise des Programms 
aktuelle ALKIS-Daten an Schnittstellen abrufen

diese anhand des richtigen RML-Mapping mithilfe rmlmapper und yarrrml-parser umwandeln

transformierte Daten in fuseki GraphDb speichern

Daten nach gewissen Gesichtspunkten über SPARQL Schnittstelle zur Verfügung stellen 


## genutzte Technologien

rmlmapper: https://github.com/RMLio/rmlmapper-java 

Yarrrml Parser: https://github.com/RMLio/yarrrml-parser

Neo4j mit neosemantics als GraphDB : https://github.com/neo4j-labs/rdflib-neo4j 

RDFLib: https://github.com/RDFLib/rdflib
