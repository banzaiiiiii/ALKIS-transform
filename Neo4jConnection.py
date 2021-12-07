import rdflib


def createTestGraph():
    # erstelle neo4j graph
    graph = rdflib.Graph(store='Neo4j')

    # set the configuration to connect to your Neo4j DB
    theconfig = {'uri': "neo4j://localhost:7687", 'database': 'neo4j', 'auth': {'user': "neo4j", 'pwd': "1234"}}

    graph.open(theconfig, create=False)

    graph.load("D://repos/Uni/BA/ALKIS-transform/Output/test.ttl", format= "ttl")

    # For each foaf:Person in the store, print out their mbox property's value.
    print("--- printing band's names ---")
    for band in graph.subjects(rdflib.RDF.type, rdflib.URIRef("http://neo4j.com/voc/music#Band")):
        for bandName in graph.objects(band, rdflib.URIRef("http://neo4j.com/voc/music#name")):
            print(bandName)



