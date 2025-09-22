import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

@st.cache_data
def load_data():
    df = pd.read_csv("metadata.csv")
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

# Year filter
year_range = st.slider("Select year range:", 2010, 2025, (2019, 2021))
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.write("Sample data:", filtered_df[['title', 'journal', 'year']].head())

# Publications per year
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top journals
top_journals = filtered_df['journal'].value_counts().head(5)
st.subheader("Top 5 Journals")
st.bar_chart(top_journals)
