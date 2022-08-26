# ALKIS-transform
Projekt for bachelor thesis - Transformation von ALKIS Daten in semantische Formate 

## How to install 
clone this repo 

install latest python version

install yarrrml-parser https://github.com/RMLio/yarrrml-parser

install rmlmapper https://github.com/RMLio/rmlmapper-java 

install the needed libraries:

python -m pip install requests

pip install rdflib

change Paths in config.json to match your folders

execute the programm from commandline with: 

python main.py

## Information for using the programm
Downloaded Data is in /Testdata

MappingFiles in /MappingFiles

Transformed Data in /Output

press 1 to use the automated transformation

the functions AlkisDataService.executeShowCaseDownload(), rdfTransformer.executeShowCaseTransformation(), FusekiConnection.executeShowCaseSave(), 
FusekiConnection.queryDB() are getting executed

you could comment out the ones you dont want to use

the automated transformation is for the states in germany(Bra, Ham, Hes, NRW, Sac) if you want more or less you need to ajust the functions 

## used technologies

rmlmapper: https://github.com/RMLio/rmlmapper-java 

Yarrrml Parser: https://github.com/RMLio/yarrrml-parser

Apache Jena Fuseki als GraphDB : https://jena.apache.org/documentation/fuseki2/

RDFLib: https://github.com/RDFLib/rdflib
