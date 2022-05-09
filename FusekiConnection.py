from rdflib import URIRef, Graph
from rdflib.plugins.stores import sparqlstore
import Helper


def saveGraph(path):
    store = sparqlstore.SPARQLUpdateStore()
    store.open((Helper.getQueryEndpoint(), Helper.getUpdateEndpoint()))

    alkis_graph = URIRef('http://example.org/alkis_graph')
    store = Graph(store, identifier=alkis_graph)

    store.load(path, format="ttl")


def executeShowCaseSave(maxIndex=None):
    store = sparqlstore.SPARQLUpdateStore()
    store.open((Helper.getQueryEndpoint(), Helper.getUpdateEndpoint()))
    alkis_graph = URIRef('http://example.org/alkis_graph')
    store = Graph(store, identifier=alkis_graph)

    filesList = ["Output/Bra/showCaseFile",
                 "Output/Ham/showcaseFile",
                 "Output/Hes/showcaseFile",
                 "Output/NRW/showcaseFile",
                 "Output/Sac/showcaseFile",
                 ]
    for file in filesList:
        StartIndex = 0
        while True:
            if maxIndex is not None and StartIndex >= maxIndex:
                print("Saving data finished!")
                break
            fileWithIndex = file + str(StartIndex) + ".ttl"
            store.load(fileWithIndex, format="ttl")
            print("the file " + fileWithIndex + " got saved to the fuseki server!")
            StartIndex += 1000



def openStore():
    store = sparqlstore.SPARQLUpdateStore()
    store.open((Helper.getQueryEndpoint(), Helper.getUpdateEndpoint()))
    alkis_graph = URIRef('http://example.org/alkis_graph')
    store = Graph(store, identifier=alkis_graph)
    return store


def queryDB():
    test_query = """
    SSELECT $s $p $o
FROM <http://example.org/alkis_graph>
WHERE {
  <http://example.com/DESNALK05e0000cC> $p $o
}
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
