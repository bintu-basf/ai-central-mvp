import streamlit as st
import openai
from streamlit_option_menu import option_menu

# Set API key through Streamlit's secrets management
openai.api_key = st.secrets["openai_api_key"]

import openai
import streamlit as st

# Assuming API key is set in Streamlit's secrets
openai.api_key = st.secrets["openai_api_key"]

assistant_id = "asst_2Jd132ACrJGpF6QDtwFYexgG"  # Actual Assistant ID

# Function to start a new conversation thread with the Assistant
def create_thread(assistant_id):
    response = openai.Thread.create(assistant_id=assistant_id)
    return response.id  # Returns the newly created Thread ID

# Function to send a message to the Assistant within a thread
def send_message(thread_id, message):
    response = openai.Message.create(
        thread_id=thread_id,
        message={"role": "user", "content": message}
    )
    return response.choices[0].text.strip() if response.choices else "No response generated."

# Streamlit UI components
def main():
    st.title("AI Central - AI Adoption Assistant")
    
    # Initialize or retrieve an existing Thread ID
    if 'thread_id' not in st.session_state:
        st.session_state.thread_id = create_thread(assistant_id)  # Create a new thread at the start

    # Sidebar for pre-populated prompts
    with st.sidebar:
        st.header("Try Pre-populated Queries")
        prompt = st.radio(
            "Select a prompt",
            ("What are the latest trends in AI?", 
             "How can AI enhance HR functions?", 
             "Generate a report on recent AI innovations in Finance", 
             "What AI tools are recommended for marketing?"),
            index=0
        )

        if st.button("Ask"):
            response = send_message(st.session_state.thread_id, prompt)
            st.text_area("AI Response:", value=response, height=300, key="response_area")

    # Allow users to type their own questions
    user_input = st.text_input("Or ask your own question:")
    if st.button("Submit"):
        response = send_message(st.session_state.thread_id, user_input)
        st.text_area("AI Response:", value=response, height=300, key="custom_response_area")

if __name__ == "__main__":
    main()
