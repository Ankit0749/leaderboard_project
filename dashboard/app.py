import streamlit as st
import sqlite3
import pandas as pd

# Refresh button
if st.button("🔄 Refresh"):
    st.rerun()

# Connect DB
conn = sqlite3.connect("db/leaderboard.db")
df = pd.read_sql("SELECT * FROM leaderboard", conn)

# Title
st.title("🏆 Online Gaming Leaderboard")

# Sort data
df = df.sort_values(by="total_score", ascending=False)

# Top 3 Players
st.subheader("🔥 Top Players")

col1, col2, col3 = st.columns(3)

if len(df) >= 3:
    col1.metric("🥇 1st", df.iloc[0]["username"], df.iloc[0]["total_score"])
    col2.metric("🥈 2nd", df.iloc[1]["username"], df.iloc[1]["total_score"])
    col3.metric("🥉 3rd", df.iloc[2]["username"], df.iloc[2]["total_score"])

# Full table
st.subheader("📊 Leaderboard")
st.dataframe(df)

# Chart
st.subheader("📈 Score Chart")
st.bar_chart(df.set_index("username")["total_score"])