from es_connection import es

def search_case_sensitive_single_word(query):
    index_name = "documents"
    body = {
        "query": {
            "match": {
                "content.case_sensitive": query
            }
        }
    }
    res = es.search(index=index_name, body=body)
    for hit in res['hits']['hits']:
        print(hit['_id'])
    total_hits = res['hits']['total']['value']
    print(f"Number of documents found: {total_hits}")
    
def search_case_sensitive_multiple_words(keywords):
    index_name = "documents"
    query_clauses = []
    for keyword in keywords:
        query_clauses.append({
            "match_phrase": {
                "content.case_sensitive": keyword 
            }
        })
    body = {
        "query": {
            "bool": {
                "should": query_clauses
            }
        }
    }
    res = es.search(index=index_name, body=body)
    for hit in res['hits']['hits']:
        print(hit['_id'])
    total_hits = res['hits']['total']['value']
    print(f"Number of documents found: {total_hits}")    
