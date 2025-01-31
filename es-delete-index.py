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
    
index_name = "documents"
    
# if es.indices.exists(index=index_name):
#     es.indices.delete(index=index_name, ignore=[400, 404])
#     print(f"Index '{index_name}' deleted successfully.")
# else:
#     print(f"Index '{index_name}' doesn't exist.")
    
response = es.count(index=index_name)
print("Number of indexed documents:", response['count'])