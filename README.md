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

- Regeln zur Transformation in .yarrrml Format
![image](https://user-images.githubusercontent.com/40140980/156211423-5ccef6a5-e0cd-46a0-9439-5fdb9c8f5768.png)
Enthält Regeln zur Umwandlung von .xml Dokumenten die das Schema alkis_vereinfacht abbilden

-Transformationsregeln in .ttl Format (erstellt mithilfe yarrrml-parser) 
![image](https://user-images.githubusercontent.com/40140980/156211592-e0071400-f49a-4984-bb73-0f088f431f30.png)

Triples die vom rmlMapper ausgegeben werden im .ttl Format 
![image](https://user-images.githubusercontent.com/40140980/156211675-7d06fa78-e229-472d-bd64-c96ec0048106.png)

- Triples werden in neo4j Db gespeichert und können über Abfragen wieder ausgegeben werden 
## genutzte Technologien

rmlmapper: https://github.com/RMLio/rmlmapper-java 

Neo4j mit neosemantics als GraphDB : https://github.com/neo4j-labs/rdflib-neo4j 

RDFLib: https://github.com/RDFLib/rdflib
