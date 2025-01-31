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

body = {
    "settings": {
        "number_of_replicas": 0,
        "analysis": {
            "analyzer": {
                "case_sensitive_analyzer": {
                    "type": "custom",
                    "tokenizer": "whitespace",
                    "filter": []
                }
            }
        }
    },
    "mappings": {
      "properties": {
        "abstract": { "type": "text", "analyzer": "english" },
        "authors": { "type": "text" },
        "authors_parsed": {
          "type": "nested",
          "properties": {
            "affiliation": { "type": "text" },
            "name": { "type": "text" },
            "surname": { "type": "text" }
          }
        },
        "categories": { "type": "keyword" },
        "comments": { "type": "text", "index": False },
        "content": {
          "type": "text",
          "fields": {
            "case_sensitive": {
              "type": "text",
              "analyzer": "case_sensitive_analyzer"
            }
          },
          "analyzer": "standard"
        },
        "doi": { "type": "keyword", "index": False },
        "id": { "type": "keyword" },
        "journal-ref": { "type": "text", "index": False },
        "journal_ref": {
          "type": "text",
          "fields": { "keyword": { "type": "keyword", "ignore_above": 256 } }
        },
        "license": { "type": "keyword" },
        "report-no": { "type": "keyword" },
        "report_no": {
          "type": "text",
          "fields": { "keyword": { "type": "keyword", "ignore_above": 256 } }
        },
        "submitter": { "type": "text" },
        "title": {
          "type": "text",
          "fields": { "keyword": { "type": "keyword", "ignore_above": 256 } }
        },
        "update_date": { "type": "date" },
        "versions": {
          "type": "nested",
          "properties": {
            "created": { "type": "date" },
            "version": { "type": "keyword" }
          }
        }
      }
    }
}
    
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=body)
    print(f"Index '{index_name}' created successfully.")
else:
    print(f"Index '{index_name}' already exists.")