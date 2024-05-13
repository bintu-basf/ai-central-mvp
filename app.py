import streamlit as st
import openai
from streamlit_option_menu import option_menu

# Assuming you will set API key through Streamlit's secrets management
openai.api_key = st.secrets["openai_api_key"]

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response['choices'][0]['message']['content']

def main():
    st.title('AI Chatbot with Pre-set Prompts')
    with st.sidebar:
        selected_prompt = option_menu("Choose a prompt", [
            "Describe AI",
            "Benefits of AI in business",
            "Challenges of AI implementation",
            "Future of AI technology",
            "Custom Prompt"],
            icons=['book', 'briefcase-fill', 'exclamation-triangle-fill', 'cpu-fill', 'pencil'],
            menu_icon="cast", default_index=0, orientation="vertical")

    if selected_prompt == "Custom Prompt":
        user_prompt = st.text_input("Enter your prompt:", "")
        if st.button("Get Response"):
            response = get_response(user_prompt)
            st.text_area("Response:", value=response, height=300)
    else:
        prompt_dict = {
            "Describe AI": "Describe artificial intelligence and its core technologies.",
            "Benefits of AI in business": "Explain the benefits of using AI in business.",
            "Challenges of AI implementation": "Discuss the challenges associated with implementing AI in an organization.",
            "Future of AI technology": "Predict the future developments in AI technology over the next decade."
        }
        response = get_response(prompt_dict[selected_prompt])
        st.text_area("Response:", value=response, height=300)

if __name__ == "__main__":
    main()
