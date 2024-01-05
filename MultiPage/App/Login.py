import streamlit as st

# Define hardcoded username and password
correct_username = "user"
correct_password = "password"

st.sidebar.image("/GenAi/MyApp/logo.png", use_column_width=True)

# Streamlit app title
st.title("Welcome to Lumoscribe")

# Initialize authentication status
if 'authenticated' not in st.session_state:
    st.session_state["authenticated"] = False

# User input for login
st.header("Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Check for login
if st.button("Login"):
    if username == correct_username and password == correct_password:
        st.success("Logged in as {}".format(username))
        st.session_state['authenticated']=True
    else:
        error_message = "Incorrect username or password"
        st.error(error_message)


# Redirect to homepage if authenticated:
if st.session_state['authenticated']:
    st.write("Login successful. Please head to the Homepage")
    
    # Redirect to a new page (homepage)
    # st.markdown('<meta http-equiv="refresh" content="URL=MyApp/pages/1_Homepage.py">', unsafe_allow_html=True)

# Display menu options if authenticated
# if st.session_state['authenticated']:

#     # st.session_state.runpage = homepage
#     st.empty()
#     st.header("Welcome to Lumoscribe")
    

#     st.sidebar.header("Menu Options")
#     if st.sidebar.button("Option 1"):
#         st.write("You selected Option 1")
#     if st.sidebar.button("Option 2"):
#         st.write("You selected Option 2")
#     if st.sidebar.button("Option 3"):
#         st.write("You selected Option 3")


