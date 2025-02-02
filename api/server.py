import time
import asyncio
from fastapi import FastAPI
from elasticsearch import AsyncElasticsearch
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()
api_key = os.getenv("ELASTIC_API_KEY")

if not api_key:
    raise ValueError("API key not found. Set ELASTIC_API_KEY in environment variables.")
  
app = FastAPI()

ES_URL = "http://localhost:9200"
INDEX_NAME = "documents"
es = AsyncElasticsearch(
    [ES_URL],
    api_key=api_key
)

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
                    {"match": {"content": "computer vision"}}
                ],
                "filter": [
                    {"range": {"published_date": {"gte": "2023-01-01"}}}
                ]
            }
        },
        "sort": [{"published_date": "desc"}],
        "size": 10
    },
    {
        "query": {
            "bool": {
                "must": [
                    {"match": {"title": {"query": "autonomous systems", "fuzziness": "AUTO"}}},
                    {"match": {"abstract": "reinforcement learning"}}
                ]
            }
        },
        "size": 5
    }
]

async def search_es(query):
    start_time = time.time()
    response = await es.search(index=INDEX_NAME, body=query)
    end_time = time.time()
    
    return {
        "hits": response["hits"]["total"]["value"],
        "time_taken": end_time - start_time
    }


async def simulate_query(n_clients: int, query: dict):
    user_times = []  
    tasks = []

    for i in range(n_clients):
        user = f"user_{i + 1}"  
        tasks.append(search_es(query))

    query_results = await asyncio.gather(*tasks)

    total_time = sum(r["time_taken"] for r in query_results)
    avg_time = total_time / len(query_results) if query_results else 0
    total_hits = sum(r["hits"] for r in query_results)

    for r in query_results:
        user_times.append(r["time_taken"])

    min_time = min(user_times)
    max_time = max(user_times)

    return {
        "user_times": {f"user_{i + 1}": round(user_times[i], 4) for i in range(n_clients)},
        "min_time": round(min_time, 4),
        "max_time": round(max_time, 4),
        "total_hits": total_hits,
        "avg_time_per_search": round(avg_time, 4),
        "total_execution_time": round(total_time, 4)
    }


@app.get("/simulate/query1/{clients}")
async def simulate_query1(clients: int):
    return await simulate_query(clients, queries[0])


@app.get("/simulate/query2/{clients}")
async def simulate_query2(clients: int):
    return await simulate_query(clients, queries[1])


@app.get("/simulate/query3/{clients}")
async def simulate_query3(clients: int):
    return await simulate_query(clients, queries[2])


@app.get("/simulate/query4/{clients}")
async def simulate_query4(clients: int):
    return await simulate_query(clients, queries[3])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
