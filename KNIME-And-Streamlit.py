import streamlit as st
import pandas as pd

st.title("Cleaned Data Viewer")

# Load your cleaned KNIME data
df = pd.read_csv("CleanedData.csv")

# Show the data
st.dataframe(df)

# Optional: Add filters
if st.checkbox("Show only users with credit > 0"):
    df = df[df["Credit"] > 0]
    st.dataframe(df)
