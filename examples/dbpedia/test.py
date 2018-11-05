import quepy3
from SPARQLWrapper import SPARQLWrapper, JSON


dbpedia = quepy3.install("dbpedia")
target, query, metadata = dbpedia.get_query("Who is Michael Jordan?")

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["x1"]["value"])
    print()