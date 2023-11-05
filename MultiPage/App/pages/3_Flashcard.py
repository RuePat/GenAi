import streamlit as st

# Define your flashcards as a list of dictionaries with 'question' and 'answer' keys
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
]

# Streamlit app
st.title("Flashcard App")

# Create a session state to store the current flashcard index, show_answer flag, and review state
if 'flashcard_index' not in st.session_state:
    st.session_state.flashcard_index = 0
    st.session_state.show_answer = False
    st.session_state.review_flashcards = set()
    st.session_state.show_only_review = False
    st.session_state.show_review_options = False

# Add a "Next" button to cycle through flashcards
if st.button("Next"):
    st.session_state.flashcard_index = (st.session_state.flashcard_index + 1) % len(flashcards)
    st.session_state.show_answer = False  # Reset show_answer flag

# Define CSS to make the flashcard box a square and center text vertically
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
    justify-content: center;
    align-items: center;
}
"""
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Checkbox at the top to show only flashcards marked for review
st.session_state.show_only_review = st.checkbox("Show only flashcards marked for review")

# Display the flashcard (question or answer)
st.write("Question:")
current_flashcard = flashcards[st.session_state.flashcard_index]
if st.session_state.show_answer:
    st.markdown(f"<div class='flashcard'>{current_flashcard['answer']}</div>", unsafe_allow_html=True)
else:
    if st.session_state.show_only_review and current_flashcard['question'] not in st.session_state.review_flashcards:
        # Skip displaying non-review flashcards if "Show only flashcards marked for review" is selected
        st.markdown("<div class='flashcard'>No flashcards marked for review</div>", unsafe_allow_html=True)
    else:
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
