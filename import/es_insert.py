from elasticsearch import helpers
import time
from generate_data import generate_fake_documents
from es_mapping import create_index
from es_connection import es

def insert_data(index_name, docs, bulk_size=5000):
    total_success = 0
    total_failed = 0

    start_time = time.time()
    batch = []

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

    end_time = time.time()
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
    
# for num_shards in [1, 2, 3]:
#     index_name = f"new_documents_{num_shards}_shards"
#     create_index(index_name, num_shards)

#     for size in [50_000, 100_000, 150_000, 200_000, 250_000]:
#         docs = generate_fake_documents(size)
#         insert_data(index_name, docs)