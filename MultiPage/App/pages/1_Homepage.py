import streamlit as st


if 'authenticated' not in st.session_state:
    st.session_state["authenticated"] = False

if st.session_state['authenticated'] == False:
    st.title("Please tell us who you are")

# st.write(st.session_state['authenticated'])

# Display menu options if authenticated

if st.session_state['authenticated']==True:

    

    #replace with sris code
    st.title("Upload Your Video")
    st.sidebar.header("Menu Options")
    if st.sidebar.button("Option 1"):
        st.write("You selected Option 1")
    if st.sidebar.button("Option 2"):
        st.write("You selected Option 2")
    if st.sidebar.button("Option 3"):
        st.write("You selected Option 3")