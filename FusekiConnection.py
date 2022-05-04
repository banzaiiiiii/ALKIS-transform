from rdflib import URIRef, Graph
from rdflib.plugins.stores import sparqlstore
import Helper

def saveGraph(path):

    store = sparqlstore.SPARQLUpdateStore()
    store.open((Helper.getQueryEndpoint(), Helper.getUpdateEndpoint()))

    alkis_graph = URIRef('http://example.org/alkis_graph')
    store = Graph(store, identifier=alkis_graph)

    store.load(path, format="ttl")


def executeShowCaseSave():
    store = sparqlstore.SPARQLUpdateStore()
    store.open((Helper.getQueryEndpoint(), Helper.getUpdateEndpoint()))

    alkis_graph = URIRef('http://example.org/alkis_graph')
    store = Graph(store, identifier=alkis_graph)

    #filesList = ["Output/Bra/showCaseFile10.ttl",
   #              "Output/Ham/showcaseFile10.ttl",
    #             "Output/Hes/showcaseFile10.ttl",
    #             "Output/NRW/showcaseFile10.ttl",
    #            # "Output/Sac/showcaseFile0.ttl",
     #            ]
   # for file in filesList:
    file = "Output/Bra/showCaseFile0.ttl"
    store.load(file, format="ttl")
    print("the file " + file + " got saved to the fuseki server!")

def openStore():
    store = sparqlstore.SPARQLUpdateStore()
    store.open((Helper.getQueryEndpoint(), Helper.getUpdateEndpoint()))
    alkis_graph = URIRef('http://example.org/alkis_graph')
    store = Graph(store, identifier=alkis_graph)
    return store

def queryDB():

    test_query = """
    SELECT $s $p $o
    WHERE { 
        $s $p $o
    }
    LIMIT 100
    """

    response = openStore().query(test_query)
    for triple in response:
        print(triple.s, triple.p, triple.o)


def queryTest():
    test_query = """
    PREFIX ex: <http://example.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX alkis: <https://w3id.org/alkis/>

select ?flurstueck ?flaeche ?gemarkung
where {
graph ?g {
?flurstueck alkis:amtlicheFlaeche ?flaeche .
    FILTER(?flaeche > 1000.0)
} 
     }
     """
    return test_query





