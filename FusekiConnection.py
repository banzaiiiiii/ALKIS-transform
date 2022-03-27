from rdflib import URIRef, Graph
from rdflib.plugins.stores import sparqlstore


def saveGraph(pathToGraph):
    query_endpoint = 'http://localhost:3030/ds/query'
    update_endpoint = 'http://localhost:3030/ds/update'

    store = sparqlstore.SPARQLUpdateStore()
    store.open((query_endpoint, update_endpoint))



    # Graph to add
    alkis_graph = URIRef('http://example.org/alkis_graph')
    store = Graph(store, identifier=alkis_graph)

    store.load(pathToGraph, format="ttl")



# store.remove_graph(graph)
# store.query(...)







