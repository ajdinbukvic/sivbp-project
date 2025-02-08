import matplotlib.pyplot as plt

queries = ['query1', 'query2', 'query3', 'query4', 'query5']

index_1_shard_1_node = [0.0599, 0.0134, 0.0037, 0.0115, 0.0104]
index_2_shard_1_node = [0.0635, 0.0090, 0.0030, 0.0090, 0.0090]
index_3_shard_1_node = [0.0756, 0.0100, 0.0038, 0.0106, 0.0120]

index_1_shard_2_node = [0.7571, 0.0855, 0.0446, 0.0822, 0.0634]
index_2_shard_2_node = [0.8043, 0.0971, 0.0751, 0.0735, 0.1008]
index_3_shard_2_node = [4.7471, 0.0337, 0.0069, 0.0466, 0.0643]

plt.figure(figsize=(10, 6))

plt.plot(queries, index_1_shard_1_node, label="Index - 1 Shard - 1 Node", marker='o')
plt.plot(queries, index_2_shard_1_node, label="Index - 2 Shards - 1 Node", marker='o')
plt.plot(queries, index_3_shard_1_node, label="Index - 3 Shards - 1 Node", marker='o')

plt.plot(queries, index_1_shard_2_node, label="Index - 1 Shard - 2 Nodes", marker='s')
plt.plot(queries, index_2_shard_2_node, label="Index - 2 Shards - 2 Nodes", marker='s')
plt.plot(queries, index_3_shard_2_node, label="Index - 3 Shards - 2 Nodes", marker='s')

plt.yscale("log") 
plt.xlabel("Upiti")
plt.ylabel("Vrijeme (sekunde)")
plt.legend()

plt.grid(True)
plt.show()
