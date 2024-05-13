import streamlit as st
import openai
from streamlit_option_menu import option_menu

# Set API key through Streamlit's secrets management
openai.api_key = "sk-proj-Hw0n8BkpRA46UhyFotzXT3BlbkFJ1iszdKVZzOmEjTwhqmfY"

# Use existing Assistant ID and Vector Store ID
assistant_id = "yasst_2Jd132ACrJGpF6QDtwFYexgG" 
vector_store_id = "asst_2Jd132ACrJGpF6QDtwFYexgG" 

# Function to send a message to a specific thread and receive a response
def send_message(assistant_id, user_message):
    try:
        # Create a thread with the user message
        thread = openai.beta.threads.create(
            assistant_id=assistant_id,
            messages=[{"role": "user", "content": user_message}]
        )
        
        # Retrieve the response from the newly created thread
        # Assuming the last message in the thread is the assistant's response
        if thread.messages:
            assistant_response = thread.messages[-1].content
        else:
            assistant_response = "No response generated."

        return assistant_response
    except Exception as e:
        st.error(f"Error while getting response: {e}")
        return "Error in processing your request."

# Streamlit UI to interact with the assistant
def main():
    st.title("AI Central - AI Adoption Manager")

    department = st.selectbox("Select your department:", ["IT", "HR", "Finance", "Marketing"])
    function = st.text_input("Enter your function or role:")
    user_question = st.text_input("Ask a question about Microsoft tools or resources:")

    if st.button("Submit"):
        # Create a detailed question incorporating user's department and function
        detailed_question = f"As a {function} in {department}, {user_question}"
        response = send_message(detailed_question)
        st.text_area("AI Response:", value=response, height=300, key="response_area")

if __name__ == "__main__":
    main()
