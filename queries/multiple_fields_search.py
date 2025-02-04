from es_connection import es

def search_multiple_fields(query):
    index_name = "documents"
    body = {
        "query": {
            "bool": {
                "should": {
                    "multi_match": {
                        "query": query,
                        "type": "phrase",
                        "fields": ["content", "title", "abstract"]
                    }
                }
            }
        }
    }
    res = es.search(index=index_name, body=body)
    # for hit in res['hits']['hits']:
    #     print(hit['_id'])
    total_hits = res['hits']['total']['value']
    print(f"Number of documents found: {total_hits}")
    
def search_by_date():
    index_name = "documents"
    body = {
        "query": {
            "range": {
                "update_date": {
                    "gte": "2024-09-01",
                    "format": "yyyy-MM-dd"
                }
            }
        }
    }
    res = es.search(index=index_name, body=body)
    # for hit in res['hits']['hits']:
    #     print(hit['_id'])
    total_hits = res['hits']['total']['value']
    print(f"Number of documents found: {total_hits}")
   