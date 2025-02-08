import matplotlib.pyplot as plt
import numpy as np

queries = ["query1", "query2", "query3", "query4"]
num_users = [1, 10, 100, 1000]

# vrijeme_izvrsavanja = {
#     "query1": [(0.0315, 0.0315, 0.0315), (0.0604, 0.1962, 0.332), (0.0922, 0.87, 1.5537), (None, None, None)],
#     "query2": [(0.0064, 0.0064, 0.0064), (0.0064, 0.0081, 0.0125), (0.0265, 0.075, 0.2735), (0.1567, 0.6543, 0.4372)],
#     "query3": [(0.1745, 0.1745, 0.1745), (0.1326, 0.2199, 0.3076), (0.09, 0.3803, 0.6591), (0.2369, 3.3152, 6.3946)],
#     "query4": [(0.0187, 0.0187, 0.0187), (0.0394, 0.1576, 0.2755), (0.0447, 0.3108, 0.526), (0.1957, 2.5, 4.7028)]
# }

execution_times = {
    "query1": [0.0315, 0.1962, 0.87, None],
    "query2": [0.0064, 0.0081, 0.075, 0.6543],
    "query3": [0.1745, 0.2199, 0.3803, 3.3152],
    "query4": [0.0187, 0.1576, 0.3108, 2.5]
}

query_colors = {
    "query1": "blue",
    "query2": "red",
    "query3": "green",
    "query4": "purple"
}

tag = "avg"
style = "o-"

plt.figure(figsize=(12, 6))

for query in queries:
    color = query_colors[query]
    
    y_values = [execution_times[query][k] if execution_times[query][k] is not None else np.nan for k in range(len(num_users))]
        
    plt.plot(num_users, y_values, style, color=color, label=f"{query} - {tag}")
    
    for i, y in enumerate(y_values):
        if not np.isnan(y):
            plt.text(num_users[i], y, f'{y:.4f}', ha='center', va='bottom', fontsize=9, color=color)

plt.xscale("log")  
plt.xlabel("Broj korisnika")
plt.ylabel("Vrijeme izvršavanja (s)")
plt.xticks(num_users, labels=[str(n) for n in num_users]) 
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.show()
