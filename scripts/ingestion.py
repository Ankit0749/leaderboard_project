import pandas as pd
import sqlite3

df = pd.read_csv("data/game_data.csv")

conn = sqlite3.connect("db/leaderboard.db")

df.to_sql("scores", conn, if_exists="replace", index=False)

print("✅ Data inserted into database!")