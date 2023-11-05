import streamlit as st
import hydralit_components as hc
from gen_data import gen_data
import pandas as pd
import streamlit_tags as st_tags
import random

def show_text(text, name):
    key = f"{name}_text_area"
    st.text_area(f"{name.capitalize()}:", text, height=150, key=key)
    # Convert summary to a string to be able to download it

def get_data(collection):
    data = pd.DataFrame(list(collection.find()))
    
    if data.empty:
        return data

    data['_id'] = data['_id'].astype(str)
    data = data.drop_duplicates(subset='_id')

    return data

def show_audio_details(row):

    st.title(f"Lecture Title: {row.get('title', '')} - Created on {row.get('created', '')}")

    st.audio(row['audio_path'])

    st.write(f"Subject: {row.get('subject', '')}", size="large")

    gen_navbar(row)

def make_api_call(audio_path):
    st.session_state.api_results = gen_data(audio_path)

# Displaying team member headshots and descriptions
def display_team(team_members):
    cols = st.columns(len(team_members))  # Create a column for each team member
    for idx, member in enumerate(team_members):
        with cols[idx]:
            # Display the image
            st.image(member["image_path"], width=300)  # Adjust the width as needed
            # Display the name and description below the image
            st.write(member["name"])
            st.write(member["description"])


def gen_navbar(record):

        show_text(record['transcript'], 'transcript')

        show_text(record['summary'], 'summary')

        option_data = [
        {'icon': "bi bi-hand-thumbs-up", 'label':"FlashCards"},
        {'icon':"fa fa-question-circle",'label':"True/False"},
        {'icon': "bi bi-hand-thumbs-down", 'label':"MCQs"},
        {'icon': "bi bi-hand-thumbs-down", 'label':"Fill in The Blanks"},
        ]

        # override the theme, else it will use the Streamlit applied theme
        over_theme = {'txc_inactive': 'white','menu_background':'#B79100','txc_active':'yellow','option_active':'#0E1117'}
        font_fmt = {'font-class':'h2','font-size':'150%'}

        # display a horizontal version of the option bar
        op = hc.option_bar(option_definition=option_data,title='Test Yourself',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)

        latest_record = record

        if op == "FlashCards":
            flashcards = latest_record['questions']['flashcards']
            if 'flashcard_index' not in st.session_state:
                st.session_state.flashcard_index = 0
                st.session_state.show_answer = False
                st.session_state.review_flashcards = set()
                st.session_state.iterate_review = False

            # Add a "Next" button to cycle through flashcards
            if st.button("Next"):
                if st.session_state.iterate_review:
                    review_flashcards = [i for i, flashcard in enumerate(flashcards) if flashcard['question'] in st.session_state.review_flashcards]
                    if review_flashcards:
                        st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % len(review_flashcards)
                    else:
                        st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % len(flashcards)
                else:
                    st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % len(flashcards)
                st.session_state.show_answer = False  # Reset show_answer flag

            # Define CSS to style the flashcard box
            custom_css = """
            .flashcard {
                background-color: #B79100;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
                margin: 10px;
                text-align: center;
                font-size: 20px;
                box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                width: 300px; /* Set the width to create a square */
                height: 300px; /* Set the height to match the width */
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            """

            st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

            # Checkbox to automatically iterate over review cards
            st.session_state.iterate_review = st.checkbox("Iterate over review cards")

            current_flashcard = flashcards[st.session_state.flashcard_index]

            if st.session_state.show_answer:
                st.write("Answer:")
                st.markdown(f"<div class='flashcard'>{current_flashcard['answer']}</div>", unsafe_allow_html=True)
            else:
                st.write("Question:")
                st.markdown(f"<div class='flashcard'>{current_flashcard['question']}</div>", unsafe_allow_html=True)

            # Create "Flip," "Add to Review," and "Remove from Review" buttons
            if st.button("Flip"):
                st.session_state.show_answer = not st.session_state.show_answer

            if current_flashcard['question'] in st.session_state.review_flashcards:
                if st.button("Remove from Review"):
                    st.session_state.review_flashcards.remove(current_flashcard['question'])
            else:
                if st.button("Add to Review"):
                    st.session_state.review_flashcards.add(current_flashcard['question'])

            # Display the list of review questions
            st.write("Review Flashcards:")
            for question in st.session_state.review_flashcards:
                st.write(question)

        elif op == "True/False":
            score = 0

            questions = record['questions']['tfs']

            try:

                with st.form("T/F"):
                    for idx, q in enumerate(questions):
                        user_answer = st.radio(f"Question {idx + 1}: {q['statement']}", ["True", "False"])

                        if str(user_answer) == str(q['sentiment']):
                            score += 1
                
                    submitted = st.form_submit_button(label='Submit')

                    if submitted:
                        st.write(f"You scored {score} out of {len(questions)} questions.")
            except:
                st.write("Please try again")
        
        elif op == "MCQs":
            score = 0
            
            questions = record['questions']['mcqs']

            st.write(questions[0])

            try:

                with st.form("MCQs"):

                    for idx, q in enumerate(questions):

                        options = q["options"]

                        user_answer = st.radio(f"Question {idx + 1}: {q['question_text']}", options)

                        if user_answer == options[q["correct_answer"]]:
                            score += 1
                    
                    submitted = st.form_submit_button(label='Submit')

                    if submitted:
                            st.write(f"You scored {score} out of {len(questions)} questions.")
            except:
                st.write("Please try again")

        
        elif op == "Fill in The Blanks":
            score = 0

            questions = record['questions']['fibs']

            try:

                with st.form("FIBs"):

                    for idx, q in enumerate(questions):
                        user_answer = st.text_input(f"Question {idx + 1}: {q['question_text']}")

                        if user_answer.lower() == q["correct_answer"][0].lower():
                            score += 1

                    submitted = st.form_submit_button(label="Submit")

                    if submitted:
                        st.write(f"You scored {score} out of {len(questions)} questions.")
            except:
                st.write("Please try again")
