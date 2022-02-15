import rdflib


def saveToNeo4j():
    # erstelle neo4j graph
    graph = rdflib.Graph(store='Neo4j')

    # set the configuration to connect to your Neo4j DB
    theconfig = {'uri': "neo4j://localhost:7687", 'database': 'rdfstore', 'auth': {'user': "neo4j", 'pwd': "1234"}}

    graph.open(theconfig, create=False)

    graph.load("D://repos/Uni/BA/ALKIS-transform/Output/Hamburg/hamburgtest.ttl", format="ttl")


def saveExample():
    graph = rdflib.Graph(store='Neo4j')
    theconfig = {'uri': "neo4j://localhost:7687", 'database': 'neo4j', 'auth': {'user': "neo4j", 'pwd': "1234"}}
    graph.open(theconfig, create=False)
    graph.load("D://repos/Uni/BA/ALKIS-transform/Output/example.nt", format="nt")
    print("--- printing band's names ---")
    for band in graph.subjects(rdflib.RDF.type, rdflib.URIRef("http://neo4j.com/voc/music#Band")):

            print(band)


def outPutFromNeo4j():
    graph = rdflib.Graph(store='Neo4j')
    theconfig = {'uri': "neo4j://localhost:7687", 'database': 'rdfstore', 'auth': {'user': "neo4j", 'pwd': "1234"}}
    graph.open(theconfig, create=False)

    print("--- printing flurstueck id's ---")
    for flurstueckId in graph.subjects(rdflib.RDF.type, rdflib.URIRef("https://w3id.org/alkis/AX_Flurstueck")):
            print(flurstueckId)
