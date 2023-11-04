import streamlit as st
import pandas as pd
from pymongo import MongoClient
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
import os
import openai

# Set OpenAI API Key (use an environment variable for security)
os.environ['OPENAI_API_KEY'] = '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'

# OpenAI Whisper model transcription functions
def transcribe_audio(audio_file):
    # Set OpenAI API Key
    openai.api_key = os.getenv('OPENAI_API_KEY')
    # Transcribe the audio file
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        # Convert the transcript to text
        text = dict(transcript)['text']
        return text
    except Exception as e:
        st.error(f"An error occurred while transcribing the audio: {e}")
        return None
# Establish a connection to the MongoDB server
client = MongoClient('localhost', 27017)

# Create or access a database called 'sample_database'
db = client['sample_database']

# Create or access a collection called 'users'
collection = db['users']

# Insert data into the collection if not already present (for demonstration purposes)
if collection.count_documents({}) == 0:
    users = [
        {"AudioPath": "/path/to/audio.mp3", "FileType": "mp3", "DateOfUpload": '2021-01-01', "Format": 10, "Length": "This is a transcript summary", "Link":"Link"},
    ]
    collection.insert_many(users)

# MongoDB Database Fetching Functions
def get_data():
    client = MongoClient('localhost', 27017)
    db = client['sample_database']
    collection = db['users']
    data = pd.DataFrame(list(collection.find()))

    if data.empty:
        return data

    data['_id'] = data['_id'].astype(str)
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

# Add additional CSS styles
st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

# Check for query parameters to set the selected page
query_params = st.experimental_get_query_params()

# Sidebar for navigation
with st.sidebar:
    st.image("logo.png", use_column_width=True)
    # Determine the selection based on the query parameters
    selected = query_params.get("selected", ["Audio Upload"])[0]
    # Use the selection to set the default index for the sidebar menu
    selected = option_menu('Company', ["Audio Upload", 'Flash Cards', 'Quiz', 'About', 'MongoDB Data Viewer'], 
        icons=['play-btn', 'search', 'info-circle', 'intersect'],
        menu_icon="cast", default_index=["Audio Upload", 'Flash Cards', 'Quiz', 'About', 'MongoDB Data Viewer'].index(selected))
    
    lottie = load_lottiefile("similo3.json")
    st_lottie(lottie, key='loc')

# Pages
if selected == "MongoDB Data Viewer":
    st.title('MongoDB Data Viewer')
    data = get_data()
    if 'audio_id' in query_params:
        audio_id = query_params['audio_id'][0]
        row = data.loc[data['_id'] == audio_id].iloc[0]
        show_audio_details(row)
    else:
        if not data.empty:
            data['Link'] = data.apply(lambda row: f"<a href='/?selected=MongoDB%20Data%20Viewer&audio_id={row['_id']}'>View Details</a>", axis=1)
            st.write(data[['AudioPath', 'DateOfUpload', 'Format', 'Length', 'Link']].to_html(escape=False), unsafe_allow_html=True)

elif selected == "Audio Upload":
    uploaded_file = st.file_uploader("Choose an MP3 or MP4 file", type=["mp3", "mp4"])
    if uploaded_file is not None:
        file_details = {"Filename": uploaded_file.name, "FileType": uploaded_file.type}
        st.write(file_details)
        # Transcribe the audio file using OpenAI's API
        transcript_text = transcribe_audio(uploaded_file)
        
        if transcript_text:
            # Display the transcription
            st.text_area("Transcription Result:", transcript_text, height=250)