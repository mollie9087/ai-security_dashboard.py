
import streamlit as st
import pandas as pd

# Load AI security news from Google Sheets
sheet_url = "YOUR_GOOGLE_SHEET_URL"
csv_url = sheet_url.replace("/edit?usp=sharing", "/gviz/tq?tqx=out:csv")

# Load data
df = pd.read_csv(csv_url)

# Streamlit Dashboard UI
st.title("🔒 AI Security & Vendor Updates")
st.write("Live updates on AI security risks, compliance, and technology changes.")

# Add filters
vendors = st.sidebar.multiselect("Filter by Vendor", df["Source"].unique(), default=df["Source"].unique())
df_filtered = df[df["Source"].isin(vendors)]

# Display Data
for index, row in df_filtered.iterrows():
    st.subheader(row["Title"])
    st.write(f"📅 Date: {row['Date']}")
    st.write(f"🔗 [Read More]({row['Link']})")
    st.write("---")

# Refresh every hour
st.cache_data(ttl=3600)
