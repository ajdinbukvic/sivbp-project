from es_connection import es

def aggregate_by_category():
    index_name = "documents"
    body = {
        "size": 0,
        "aggs": {
            "categories_count": {
                "terms": {
                    "field": "categories",
                    "size": 10
                }
            }
        }
    }
    res = es.search(index=index_name, body=body)
    return res["aggregations"]["categories_count"]["buckets"]

def aggregate_title_length():
    body = {
        "size": 0,
        "aggs": {
            "title_length_histogram": {
                "histogram": {
                    "script": {
                        "source": "return doc['title.keyword'].value.length();"
                    },
                    "interval": 50
                }
            }
        }
    }
    res = es.search(index="documents", body=body)
    for bucket in res["aggregations"]["title_length_histogram"]["buckets"]:
        print(f"Length: {bucket['key']} - {bucket['key'] + 50}, Number of documents: {bucket['doc_count']}")