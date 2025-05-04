import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("honeypot_logs_geo.csv")

st.title("📊 Honeypot Intrusion Detection Dashboard")
st.write("Overview of login attempts captured by the honeypot.")

# Most frequent IPs
st.subheader("Top 5 Attacker IPs")
st.bar_chart(df['ip'].value_counts().head(5))

# Common Usernames
st.subheader("Most Tried Usernames")
st.bar_chart(df['username'].value_counts().head(5))

# Countries
st.subheader("Top Countries by Attack Count")
st.bar_chart(df['country'].value_counts().head(5))

# Data Table
st.subheader("Full Attack Log")
st.dataframe(df)
