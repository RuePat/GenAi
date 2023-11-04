import streamlit as st
import pandas as pd
from pymongo import MongoClient
from pathlib import Path

# Function to connect to the database and fetch data
def get_data():
    client = MongoClient('localhost', 27017)
    db = client['sample_database']
    collection = db['users']
    data = pd.DataFrame(list(collection.find()))

    # If data is empty, return it before trying to access '_id'
    if data.empty:
        return data

    # Convert ObjectId to string for compatibility
    data['_id'] = data['_id'].astype(str)
    
    # Optional: Remove duplicates if you want to keep only unique AudioPath entries
    data = data.drop_duplicates(subset='AudioPath')
    
    return data

# Function to display the details of a specific audio file
def show_audio_details(row):
    st.audio(row['AudioPath'])
    # Display the additional details for the specific audio file
    st.write(f"Transcript Summary: {row.get('Transcript_Summary', '')}")
    st.write(f"MultipleChoice: {row.get('MultipleChoice', '')}")
    st.write(f"Short Answer: {row.get('ShortAnswer', '')}")
    st.write(f"TrueFalse: {row.get('TrueFalse', '')}")

# Function to display the interactive table using Streamlit
def main():
    # Title of the app
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
        return

    # If not showing details, display the original dataframe with links
    if not data.empty:
        # Generate links for the details of each audio file
        data['Link'] = data.apply(lambda row: f"<a href='?audio_id={row['_id']}' target='_blank'>View Details</a>", axis=1)
        # Use the .style to apply the HTML to the Link column for clickable links
        st.write(data[['AudioPath', 'DateOfUpload', 'Format', 'Length', 'Link']].to_html(escape=False), unsafe_allow_html=True)

# Run the app
if __name__ == '__main__':
    main()
