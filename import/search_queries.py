from es_connection import es
import time
import subprocess

def get_es_container():
    try:
        result = subprocess.run(["docker", "ps", "--format", "{{.ID}} {{.Image}} {{.Names}}"], capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "elasticsearch" in line.lower():
                container_id = line.split()[0]
                return container_id
    except Exception as e:
        print(f"Error with ES container: {e}")
    
    return None

container_id = get_es_container()

def get_es_stats(container_id):
    result = subprocess.run(
        ["docker", "stats", "--no-stream", "--format", "{{.CPUPerc}} {{.MemUsage}}", container_id],
        capture_output=True, text=True
    )
    return result.stdout.strip()

def search_with_monitoring(index_name, query, i):
    
    start_time = time.time()
    response = es.search(index=index_name, body=query)
    end_time = time.time()
    
    total_docs = response["hits"]["total"]["value"]
    
    print(f"Search Query {i} for {index_name} took {end_time - start_time:.4f} seconds. Total results: {total_docs}")

query_1 = {
    "query": {
        "bool": {
            "must": [
                {
                    "multi_match": {
                        "query": "Challenge tax word morning over important election",
                        "fields": ["title", "abstract", "content"],
                        "fuzziness": "AUTO",
                        "operator": "and"
                    }
                }
            ]
        }
    }
}

query_2 = {
    "query": {
        "range": {
            "update_date": {
                "gte": "2023-01-01",
                "lte": "2023-06-30"
            }
        }
    },
    "sort": [
        {"update_date": "asc"}
    ]
}

query_3 = {
    "size": 0,
    "query": {
        "bool": {
            "filter": [
                { "term": { "category.keyword": "cs.LG" } }
            ]
        }
    },
    "aggs": {
        "avg_length": {
            "avg": {
                "field": "word_count"
            }
        }
    }
}

query_4 = {
    "query": {
        "bool": {
            "should": [
                {"match_phrase": {"abstract": "computer science"}},
                {"match": {"category": "cs.AI"}}
            ]
        }
    },
    "sort": [
        {"update_date": "desc"}
    ]
}

query_5 = {
    "query": {
        "bool": {
            "must": [
                {"match": {"abstract": "full"}},
                {"match_phrase": {"content": "old task"}}
            ],
            "should": [
                {"match": {"keywords": "AI"}},
                {"match": {"keywords": "optimization"}}
            ],
            "must_not": [
                {"match": {"category": "physics.optics"}}
            ]
        }
    }
}

queries = [query_1, query_2, query_3, query_4, query_5]

index_names = ["new_documents_1_shards", "new_documents_2_shards", "new_documents_3_shards"]

for index_name in index_names:
    for i, query in enumerate(queries, 1):
        search_with_monitoring(index_name, query, i)
    print()
