import sqlite3
import pandas as pd

conn = sqlite3.connect("db/leaderboard.db")

query = """
SELECT username, SUM(score) as total_score
FROM scores
GROUP BY username
ORDER BY total_score DESC
"""

df = pd.read_sql(query, conn)

print("🏆 Leaderboard:")
print(df)

df.to_sql("leaderboard", conn, if_exists="replace", index=False)