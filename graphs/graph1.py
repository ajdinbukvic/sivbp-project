import matplotlib.pyplot as plt
import numpy as np

queries = ["Q1-1", "Q1-2", "Q2-1", "Q2-2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8-1", "Q8-2"]
execution_times = [0.0677, 0.1618, 0.0782, 0.1968, 1.5029, 0.1071, 0.0819, 0.0229, 0.0199, 0.1720, 0.8819]
execution_times_cached = [0.0401, 0.0370, 0.0379, 0.0308, 0.1570, 0.0244, 0.0333, 0.0121, 0.0313, 0.0882, 0.6390]

x = np.arange(len(queries))
width = 0.4 

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(x - width/2, execution_times, width, label='Bez keširanja', color='blue')
ax.bar(x + width/2, execution_times_cached, width, label='Keširano', color='orange')

ax.set_xlabel('Upiti')
ax.set_ylabel('Vrijeme izvršavanja (s)')
ax.set_xticks(x)
ax.set_xticklabels(queries, rotation=45)
ax.legend()

plt.tight_layout()
plt.show()
