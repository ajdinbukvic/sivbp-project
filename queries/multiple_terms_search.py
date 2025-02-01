from es_connection import es

def search_terms(must_terms, should_terms, must_not_terms):
    index_name = "documents"
    body = {
        "query": {
            "bool": {
                "must": [{"match_phrase": {"content": term}} for term in must_terms],
                "should": [{"match_phrase": {"content": term}} for term in should_terms],
                "must_not": [{"match_phrase": {"content": term}} for term in must_not_terms]
            }
        }
    }
    res = es.search(index=index_name, body=body)
    # for hit in res['hits']['hits']:
    #     print(hit['_id'])
    total_hits = res['hits']['total']['value']
    print(f"Number of documents found: {total_hits}")
    
def search_wildcard(pattern):
    index_name = "documents"
    body = {
        "query": {
            "wildcard": {
                "content": pattern
            }
        }
    }
    res = es.search(index=index_name, body=body)
    # for hit in res['hits']['hits']:
    #     print(hit['_id'])
    total_hits = res['hits']['total']['value']
    print(f"Number of documents found: {total_hits}")
