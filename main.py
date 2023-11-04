import streamlit as st
import pandas as pd
from pymongo import MongoClient
from urllib.request import urlopen
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import json
import requests
from streamlit_lottie import st_lottie
import pydeck as pdk
import streamlit as st
import pandas as pd
from pymongo import MongoClient
from moviepy.editor import VideoFileClip
from streamlit_option_menu import option_menu
from mutagen.mp3 import MP3
from bson import ObjectId
import gridfs
import io

# Establish a connection to the MongoDB server
client = MongoClient('localhost', 27017)

# Create or access a database called 'sample_database'
db = client['sample_database']

# Create or access a collection called 'users'
collection = db['users']

# Sample data to insert into the collection
users = [
    {"AudioPath": "/Users/sveerisetti/Desktop/Hackathon/Sample/similo_beta2-main/audio_files_dir/NN_Video.mp3", "FileType": "mp3", "DateOfUpload": '2021-01-01', "Format": 10, "Length": "This is a transcript summary", "Link":"Link"},
]

# Insert the data into the collection
collection.insert_many(users)

# MongoDB Database Fetching Functions
def get_data():
    client = MongoClient('localhost', 27017)
    db = client['sample_database']  # Replace with your actual database name
    collection = db['users']  # Replace with your actual collection name
    data = pd.DataFrame(list(collection.find()))

    # If data is empty, return it before trying to access '_id'
    if data.empty:
        return data

    # Convert ObjectId to string for compatibility
    data['_id'] = data['_id'].astype(str)
    
    # Optional: Remove duplicates if you want to keep only unique AudioPath entries
    data = data.drop_duplicates(subset='AudioPath')
    
    return data

def show_audio_details(row):
    st.audio(row['AudioPath'])
    st.write(f"Transcript Summary: {row.get('Transcript_Summary', '')}")
    st.write(f"MultipleChoice: {row.get('MultipleChoice', '')}")
    st.write(f"Short Answer: {row.get('ShortAnswer', '')}")
    st.write(f"TrueFalse: {row.get('TrueFalse', '')}")

# Set page config
st.set_page_config(
    page_title="SimiLo",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define functions for lottie
@st.cache(allow_output_mutation=True)
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.cache(suppress_st_warning=True)
def pull_clean():
    master_zip = pd.read_csv('MASTER_ZIP.csv', dtype={'ZCTA5': str})
    master_city = pd.read_csv('MASTER_CITY.csv', dtype={'ZCTA5': str})
    return master_zip, master_city

# Add additional CSS styles
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Company', ["Audio Upload/History", 'Flash Cards', 'Quiz', 'About', 'MongoDB Data Viewer'], 
        icons=['play-btn', 'search', 'info-circle', 'intersect'], default_index=0)
    lottie = load_lottiefile("similo3.json")
    st_lottie(lottie, key='loc')

# Pages
if selected == "Intro":
    # Your existing Intro page code
    pass
elif selected == "Audio Upload/History":
     # File uploader
    uploaded_file = st.file_uploader("Choose an MP3 or MP4 file", type=["mp3", "mp4"])
    if uploaded_file is not None:
        file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type}
        st.write(file_details)

elif selected == "MongoDB Data Viewer":
    st.title('MongoDB Data Viewer')
    # Fetch data from the database
    data = get_data()
    # Check if the details of a specific file need to be shown
    query_params = st.experimental_get_query_params()
    if 'audio_id' in query_params:
        # Fetch the specific row
        audio_id = query_params['audio_id'][0]
        row = data.loc[data['_id'] == audio_id].iloc[0]
        show_audio_details(row)
    else:
        # If not showing details, display the original dataframe with links
        if not data.empty:
            # Generate links for the details of each audio file
            data['Link'] = data.apply(lambda row: f"<a href='?audio_id={row['_id']}' target='_blank'>View Details</a>", axis=1)
            st.write(data[['AudioPath', 'DateOfUpload', 'Format', 'Length', 'Link']].to_html(escape=False), unsafe_allow_html=True)

