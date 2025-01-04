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

data_path = 'data/data.json'
df_path = 'data/comments_result_df.csv'

# Data for Pie Chart
with open(data_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# post_username = [[index + 1, item['username']] for index, item in enumerate(data)]

# usernames = st.sidebar.multiselect(
#     "Choose post to display:",
#     post_username,
#     default=post_username
# )

# filtered_data = [item for index, item in enumerate(data) if index + 1 in usernames]

# # Main Page Title
# st.title("Streamlit Sidebar and Pie Chart with Plotly")

# labels = ['positive', 'neutral', 'negative']
# positive_count = sum(1 for item in filtered_data if item['comments']['label'] == labels[0])
# neutral_count = sum(1 for item in filtered_data if item['comments']['label'] == labels[1])
# negative_count = sum(1 for item in filtered_data if item['comments']['label'] == labels[2])

# values = [positive_count, neutral_count, negative_count]

# Create a Plotly pie chart
fig = px.pie(
    names=labels,
    values=values,
    title="Comment Sentiment Distribution",
    color_discrete_sequence=px.colors.qualitative.Set3
)

# Display in Streamlit
st.title("Comment Sentiment Analysis")
st.plotly_chart(fig)

# Additional Note in Sidebar
st.sidebar.info("Use the filters to adjust the pie chart data.")