queries = [
    {
        "query": {
            "multi_match": {
                "query": "deep learning",
                "fields": ["title", "abstract", "content"]
            }
        }
    },
    {
        "size": 0,
        "query": {
            "bool": {
                "filter": [{"term": {"category.keyword": "cs.AI"}}]
            }
        },
        "aggs": {
            "avg_word_count": {"avg": {"field": "word_count"}}
        }
    },
    {
        "query": {
            "bool": {
                "must": [
                    {"match_phrase": {"content": "computer vision"}}
                ],
                "filter": [
                    {"range": {"update_date": {"gte": "2023-01-01"}}}
                ]
            }
        },
        "sort": [{"update_date": "desc"}],
        "size": 10
    },
    {
        "query": {
            "bool": {
                "must": [
                    {"match": {"title": {"query": "autonomous", "fuzziness": "AUTO"}}},
                    {"match_phrase": {"abstract": "reinforcement learning"}}
                ]
            }
        },
        "size": 5
    }
]