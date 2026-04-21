import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests   

# -----------------------------
# Load Data FROM API (with caching)
# -----------------------------
API_URL = "http://127.0.0.1:5000/books"

@st.cache_data
def load_data():
    response = requests.get(API_URL)
    data = response.json()
    df = pd.DataFrame(data)

    # FIX: Convert data types properly
    rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}

    # Convert PRICE safely
    df["PRICE"] = pd.to_numeric(df["PRICE"], errors="coerce")

    # Convert RATING safely
    if df["RATING"].dtype == "object":
        df["RATING"] = df["RATING"].map(rating_map)

    return df

df = load_data()

# -----------------------------
# Theme Toggle
# -----------------------------
theme = st.sidebar.radio("Theme", ["Dark", "Light"])

if theme == "Light":
    st.markdown(
        """
        <style>
        .stApp {background-color: white; color: black;}
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Title
# -----------------------------
st.title(" Book Analysis Dashboard")

# -----------------------------
# Metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Books", len(df))
col2.metric("Avg Price", round(df["PRICE"].mean(), 2))
col3.metric("Max Price", df["PRICE"].max())

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filter Options")

rating_range = st.sidebar.slider("Select Rating", 1, 5, (1,5))
price_range = st.sidebar.slider("Select Price", 0, 60, (0,60))

# -----------------------------
# Search
# -----------------------------
search = st.text_input(" Search Book Title")

# -----------------------------
# Filtering
# -----------------------------
filtered_df = df[
    (df["RATING"] >= rating_range[0]) & (df["RATING"] <= rating_range[1]) &
    (df["PRICE"] >= price_range[0]) & (df["PRICE"] <= price_range[1])
]

# Apply search
if search:
    filtered_df = filtered_df[
        filtered_df["TITLE"].str.contains(search, case=False, na=False)
    ]

# -----------------------------
# Show Data
# -----------------------------
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# -----------------------------
# Download CSV
# -----------------------------
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_books.csv",
    mime="text/csv"
)

# -----------------------------
# Charts
# -----------------------------
st.subheader("Visual Insights")

# Rating count
fig1, ax1 = plt.subplots()
sns.countplot(x="RATING", data=filtered_df, ax=ax1)
st.pyplot(fig1)

# Price distribution
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df["PRICE"], bins=20, ax=ax2)
st.pyplot(fig2)

# -----------------------------
# Top 10 Expensive Books
# -----------------------------
st.subheader("Top 10 Most Expensive Books")

top_books = df.sort_values(by="PRICE", ascending=False).head(10)
st.dataframe(top_books)