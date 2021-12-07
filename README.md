# ALKIS-transform
Projekt zur Bachelorarbeit - Transformation von ALKIS Daten in semantische Formate 

## geplante Funktionsweise des Programms 
aktuelle ALKIS-Daten an Schnittstellen abrufen

diese anhand des richtigen RML-Mapping mithilfe rmlmapper umwandeln

transformierte Daten in Neo4j GraphDb speichern

Daten nach gewissen Gesichtspunkten über SPARQL Schnittstelle zur Verfügung stellen 

## Demo Video über Funktionsweise
todo

## Programmfunktionsweise bis jetzt 

Aufruf von rmlmapper Anwendung mit Argumenten(mappingfile und output path)

Speicherung von output in Neo4J DB

Ausgabe von Testdaten aus Neo4J DB

## genutzte Technologien

rmlmapper: https://github.com/RMLio/rmlmapper-java 

Neo4j mit neosemantics als GraphDB : https://github.com/neo4j-labs/rdflib-neo4j 

RDFLib: https://github.com/RDFLib/rdflib
