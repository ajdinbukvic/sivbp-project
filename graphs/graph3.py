import matplotlib.pyplot as plt

num_data = [50000, 100000, 150000, 200000, 250000]

index_1_shard_1_node = [19.10, 46.90, 72.13, 97.91, 115.13]
index_2_shard_1_node = [18.07, 35.53, 53.11, 71.63, 89.36]
index_3_shard_1_node = [15.10, 30.70, 49.96, 71.52, 84.32]

index_1_shard_2_node = [16.81, 33.62, 58.31, 83.82, 116.37]
index_2_shard_2_node = [15.96, 34.10, 54.47, 77.67, 106.57]
index_3_shard_2_node = [19.41, 46.49, 57.34, 73.14, 80.28]

plt.figure(figsize=(10, 6))

plt.plot(num_data, index_1_shard_1_node, label="Index - 1 Shard - 1 Node", marker='o')
plt.plot(num_data, index_2_shard_1_node, label="Index - 2 Shards - 1 Node", marker='o')
plt.plot(num_data, index_3_shard_1_node, label="Index - 3 Shards - 1 Node", marker='o')

plt.plot(num_data, index_1_shard_2_node, label="Index - 1 Shard - 2 Nodes", marker='s')
plt.plot(num_data, index_2_shard_2_node, label="Index - 2 Shards - 2 Nodes", marker='s')
plt.plot(num_data, index_3_shard_2_node, label="Index - 3 Shards - 3 Nodes", marker='s')

for i, txt in enumerate(index_1_shard_1_node):
    plt.text(num_data[i], txt, f'{txt:.4f}', ha='center', va='bottom', fontsize=9)
for i, txt in enumerate(index_2_shard_1_node):
    plt.text(num_data[i], txt, f'{txt:.4f}', ha='center', va='bottom', fontsize=9)
for i, txt in enumerate(index_3_shard_1_node):
    plt.text(num_data[i], txt, f'{txt:.4f}', ha='center', va='bottom', fontsize=9)
for i, txt in enumerate(index_1_shard_2_node):
    plt.text(num_data[i], txt, f'{txt:.4f}', ha='center', va='bottom', fontsize=9)
for i, txt in enumerate(index_2_shard_2_node):
    plt.text(num_data[i], txt, f'{txt:.4f}', ha='center', va='bottom', fontsize=9)
for i, txt in enumerate(index_3_shard_2_node):
    plt.text(num_data[i], txt, f'{txt:.4f}', ha='center', va='bottom', fontsize=9)

plt.xticks(num_data)

plt.xlabel("Broj podataka")
plt.ylabel("Vrijeme (sekunde)")
plt.legend()

plt.grid(True)
plt.show()
