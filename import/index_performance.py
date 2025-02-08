from es_connection import es
import requests

ES_URL = "http://localhost:9200"

index_names = ["new_documents_1_shards", "new_documents_2_shards", "new_documents_3_shards"]

def get_index_stats():
    for index_name in index_names:
      stats = es.indices.stats(index=index_name)
      print(f"Stats for index {index_name}:")
      print(f"Number of documents: {int(stats['_all']['primaries']['docs']['count'] / 3)}")
      print(f"Total size: {int(stats['_all']['primaries']['store']['size_in_bytes'] / 1e6 / 1000)} GB")

get_index_stats()

def analyze_shards(index_name):
    res = es.cat.shards(index=index_name, format="json")

    stats = es.indices.stats(index=index_name, level="shards")

    print(f"\nShard analysis for index {index_name}:")

    for shard in res:
        shard_id = shard["shard"]
        node = shard["node"]
        store = shard["store"]
        state = shard["state"]

        doc_count = 0
        
        if "indices" in stats and index_name in stats["indices"]:
            index_stats = stats["indices"][index_name]

            if "shards" in index_stats and shard_id in index_stats["shards"]:
                shard_info = index_stats["shards"][shard_id][0]

                if "docs" in shard_info:
                    doc_count = int(int(shard_info["docs"].get("count", "N/A")) / 3)

        print(f"Shard: {shard_id}, Node: {node}, Docs: {doc_count}, Store: {store}, State: {state}")

for num_shards in [1, 2, 3]:
    index_name = f"new_documents_{num_shards}_shards"
    analyze_shards(index_name)

def analyze_disk_usage():
    res = es.cat.indices(v=True, format="json")
    print("\nDisk Usage for all indices:")
    for index in res:
        print(f"Index: {index['index']}, Docs: {int(int(index['docs.count']) / 3)}, Store Size: {index['store.size']}")

analyze_disk_usage()

def get_es_stats():
    response = requests.get(f"{ES_URL}/_nodes/stats")
    if response.status_code == 200:
        data = response.json()
        for node_id, node_stats in data['nodes'].items():
            print(f"\nNode ID: {node_id}")
            print(f"CPU Usage: {node_stats['os']['cpu']['percent']}%")
            print(f"Heap Memory Used: {node_stats['jvm']['mem']['heap_used_percent']}%")
    else:
        print("Error getting data from ES!")

get_es_stats()