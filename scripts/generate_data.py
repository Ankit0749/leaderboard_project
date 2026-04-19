import pandas as pd
import random
from datetime import datetime

usernames = ["John", "Alice", "Bob", "Charlie", "David", "Eva"]
games = ["PUBG", "FreeFire", "COD"]

data = []

# Generate 20 rows per run
for i in range(20):
    data.append({
        "player_id": random.randint(1, 20),
        "username": random.choice(usernames),
        "score": random.randint(500, 2000),
        "game": random.choice(games),
        "timestamp": datetime.now()
    })

df = pd.DataFrame(data)

# Append to CSV
df.to_csv("data/game_data.csv", mode='a', header=False, index=False)

print("✅ New batch data added")