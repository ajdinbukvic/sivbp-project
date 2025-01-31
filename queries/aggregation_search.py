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