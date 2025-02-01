from es_connection import es

def create_index(index_name, shard_count):

    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    body = {
    "settings": {
        "number_of_replicas": 0,
        "number_of_shards": shard_count
    },
    "mappings": {
      "properties": {
        "abstract": { "type": "text", "analyzer": "standard" },
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
          "analyzer": "standard"
        },
        "doi": { "type": "keyword", "index": False },
        "id": { "type": "keyword" },
        "journal-ref": { "type": "text", "index": False },
        "journal_ref": { "type": "keyword", "ignore_above": 512 },
        "license": { "type": "keyword" },
        "report-no": { "type": "keyword" },
        "report_no": { "type": "keyword", "ignore_above": 512 },
        "submitter": { "type": "text" },
        "title": { "type": "text", "analyzer": "standard" },
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
    
    es.indices.create(index=index_name, body=body)
    print(f"Index {index_name} created with {shard_count} shards.")
