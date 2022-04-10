from rdflib import URIRef, Graph
from rdflib.plugins.stores import sparqlstore
import Helper

def saveGraph(path):

    store = sparqlstore.SPARQLUpdateStore()
    store.open((Helper.getQueryEndpoint(), Helper.getUpdateEndpoint()))


    alkis_graph = URIRef('http://example.org/alkis_graph')
    store = Graph(store, identifier=alkis_graph)

    store.load(path, format="ttl")


def queryDB():
    graph = Graph()
    response = graph.query(
        """
            select * where {
    graph ?g {
        ?s ?p ?o .
    } 
}
            """
    )
    for row in response:
        print(row)








