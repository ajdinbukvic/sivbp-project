import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()
api_key = os.getenv("ELASTIC_API_KEY")

if not api_key:
    raise ValueError("API key not found. Set ELASTIC_API_KEY in environment variables.")

es = Elasticsearch(
    "http://localhost:9200",
    api_key=api_key,
)

if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Could not connect!")

def close_connection():
    es.close()
    print("Elasticsearch connection closed.")
