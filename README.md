# ALKIS-transform
Projekt zur Bachelorarbeit - Transformation von ALKIS Daten in semantische Formate 

## geplante Funktionsweise des Programms 
aktuelle ALKIS-Daten an Schnittstellen abrufen

diese anhand des richtigen RML-Mapping mithilfe rmlmapper umwandeln

transformierte Daten in Neo4j GraphDb speichern

Daten nach gewissen Gesichtspunkten über SPARQL Schnittstelle zur Verfügung stellen 

## Demo über Funktionsweise
- Download raw alkis Data von gewünschten Bundesland und Gemeindenummer 
![image](https://user-images.githubusercontent.com/40140980/156211143-0e53fde8-bfae-4495-bd66-1e0ac9b2a357.png)
Auszug aus alkis_vereinfacht.xml (nrw)



## genutzte Technologien

rmlmapper: https://github.com/RMLio/rmlmapper-java 

Neo4j mit neosemantics als GraphDB : https://github.com/neo4j-labs/rdflib-neo4j 

RDFLib: https://github.com/RDFLib/rdflib
