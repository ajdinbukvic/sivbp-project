from es_connection import es

def search_fuzzy(query):
    index_name = "documents"
    body = {
        "query": {
            "fuzzy": {
                "content": {
                    "value": query,
                    "fuzziness": "AUTO"
                }
            }
        }
    }
    res = es.search(index=index_name, body=body)
    # for hit in res['hits']['hits']:
    #     print(hit['_id'])
    total_hits = res['hits']['total']['value']
    print(f"Number of documents found: {total_hits}")