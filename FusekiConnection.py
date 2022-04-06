from rdflib import URIRef, Graph
from rdflib.plugins.stores import sparqlstore


def saveGraph(path):
    query_endpoint = 'http://localhost:3030/ds/query'
    update_endpoint = 'http://localhost:3030/ds/update'

    store = sparqlstore.SPARQLUpdateStore()
    store.open((query_endpoint, update_endpoint))


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








