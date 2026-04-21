import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/data.csv")

# Title
st.title("Book Analysis Dashboard")

st.sidebar.header("Filter Options")

rating_range = st.sidebar.slider("Select Rating", 1, 5, (1,5))
price_range = st.sidebar.slider("Select Price", 0, 60, (0,60))

# Filter data
filtered_df = df[
    (df["RATING"] >= rating_range[0]) & (df["RATING"] <= rating_range[1]) &
    (df["PRICE"] >= price_range[0]) & (df["PRICE"] <= price_range[1])
]

# Show data
st.subheader("Filtered Data")
st.dataframe(filtered_df)

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button(
    label=" Download CSV",
    data=csv,
    file_name="filtered_books.csv",
    mime="text/csv"
)

# Chart 1: Rating count
st.subheader(" Rating Distribution")
fig1, ax1 = plt.subplots()
sns.countplot(x="RATING", data=filtered_df, ax=ax1)
st.pyplot(fig1)

# Chart 2: Price distribution
st.subheader("Price Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df["PRICE"], bins=20, ax=ax2)
st.pyplot(fig2)

# Chart 3: Price vs Rating
st.subheader("Price vs Rating")
fig3, ax3 = plt.subplots()
sns.boxplot(x="RATING", y="PRICE", data=filtered_df, ax=ax3)
st.pyplot(fig3)