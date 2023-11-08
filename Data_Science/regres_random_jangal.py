import pandas as pd

# Given data
data = {
    "cat": {
        "frequencies": [1, 5],
        "distances": [[10], [29.33]]
    },
    "fish": {
        "frequencies": [3],
        "distances": [[3]]
    },
    "dog": {
        "frequencies": [2, 4],
        "distances": [[41.33], [17.21]]
    },
    "turtle": {
        "frequencies": [10, 12, 78],
        "distances": [[34.77], [98.88], [17.32]]
    }
}


rows = []
for category, details in data.items():
    for frequency, distance_list in zip(details["frequencies"], details["distances"]):
        for distance in distance_list:
            rows.append({"category": category, "frequency": frequency, "distance": distance})


df = pd.DataFrame(rows)


df
