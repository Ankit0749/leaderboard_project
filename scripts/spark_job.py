from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Leaderboard").getOrCreate()

df = spark.read.csv("data/game_data.csv", header=True, inferSchema=True)

leaderboard = df.groupBy("username").sum("score")

leaderboard.show()