from es_connection import es
import time
import subprocess
import psutil
from es_queries import queries

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


def execute_query_with_monitoring(index_name, query, i):
    cpu_usage = []
    memory_usage = []

    start_time = time.time()

    while True:
        cpu_usage.append(psutil.cpu_percent(interval=0.1))
        memory_usage.append(psutil.virtual_memory().percent)

        if len(cpu_usage) == 1:
            response = es.search(index=index_name, body=query)
            total_docs = response["hits"]["total"]["value"]
            break

    end_time = time.time()
    exec_time = end_time - start_time
    
    print(f"\nSearch Query {i} for {index_name} took: {exec_time:.4f} seconds. Total results: {total_docs}")
    print(f"CPU usage: {cpu_usage}%")
    print(f"RAM usage: {memory_usage}MB")

index_names = ["new_documents_1_shards", "new_documents_2_shards", "new_documents_3_shards"]

for index_name in index_names:
    for i, query in enumerate(queries, 1):
        execute_query_with_monitoring(index_name, query, i)
    print()
