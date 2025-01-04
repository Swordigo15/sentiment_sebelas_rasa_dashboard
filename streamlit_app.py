import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from collections import Counter
import re
import nltk
import json

nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

st.set_page_config(page_title='Survey Dashboard', layout='wide', page_icon="📊")

@st.cache_data
def load_data(file_path, separator=',', encoding='utf-8'):
    try:
        df = pd.read_csv(file_path, sep=separator, encoding=encoding)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()
    
# Sidebar
st.sidebar.title("Sidebar Options")
st.sidebar.header("Pie Chart Filters")

post_data_df_path = 'data/post_data_df.csv'
sentiment_df_path = 'data/sentiment_df.csv'

post_data_df = load_data(post_data_df_path)
sentiment_df = load_data(sentiment_df_path)

# filtered_post_data_df = post_data_df[['username', 'post_link', 'likes_count', 'comments_count']]

# # Rename columns if needed
# filtered_post_data_df.rename(columns={
#     'likes_count': 'likes',
#     'comments_count': 'comments_count'
# }, inplace=True)

st.title("Post Data Table")
st.dataframe(post_data_df)
st.dataframe(sentiment_df)

# post_username = post_data_df[0]

posts = st.sidebar.multiselect(
    "Choose post to display:",
    filtered_post_data_df,
    default=filtered_post_data_df
)

# # Create a Plotly pie chart
# fig = px.pie(
#     names=labels,
#     values=values,
#     title="Comment Sentiment Distribution",
#     color_discrete_sequence=px.colors.qualitative.Set3
# )

# # Display in Streamlit
# st.title("Comment Sentiment Analysis")
# st.plotly_chart(fig)

# Additional Note in Sidebar
st.sidebar.info("Use the filters to adjust the pie chart data.")