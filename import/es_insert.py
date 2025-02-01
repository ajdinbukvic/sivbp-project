from elasticsearch import helpers
import time
from generate_data import generate_fake_documents
from es_mapping import create_index
from es_connection import es

def insert_data(index_name, docs, bulk_size=1000):
    total_success = 0
    total_failed = 0
    batch = []

    start_time = time.perf_counter()

    for doc in docs:
        batch.append({"_op_type": "index", "_index": index_name, "_source": doc})
        if len(batch) >= bulk_size:
            success, failed = bulk_insert(batch)
            total_success += success
            total_failed += failed
            batch = [] 

    if batch:
        success, failed = bulk_insert(batch)
        total_success += success
        total_failed += failed

    es.indices.refresh(index=index_name)
    end_time = time.perf_counter() 
    print(f"Inserted {total_success} documents in {end_time - start_time:.2f} seconds. Failed: {total_failed}")
    
def bulk_insert(actions):
    success, failed = 0, 0
    try:
        response = helpers.bulk(es, actions)
        success = response[0]
    except Exception as e:
        print(f"Bulk insert error: {e}")
        failed = len(actions)

    return success, failed

doc_sizes = [50_000, 100_000, 150_000, 200_000, 250_000]
docs_dict = {size: generate_fake_documents(size) for size in doc_sizes}
    
for num_shards in [1, 2, 3]:
    index_name = f"new_documents_{num_shards}_shards"
    create_index(index_name, num_shards)

    for size in doc_sizes:
        insert_data(index_name, docs_dict[size])