import streamlit as st
from streamlit_chat import message
from langchain.llms import CTransformers

# Loading the model
def load_llm():
    llm = CTransformers(
        model="llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5
    )
    return llm

st.title("Chat with Llama2 🦙🦜")
st.markdown(
    "<h3 style='text-align: center; color: white;'>Built by <a href='https://github.com/AIAnytime'>AI Anytime with ❤️ </a></h3>",
    unsafe_allow_html=True
)

llm = load_llm()

# Initialize the conversation history
if 'history' not in st.session_state:
    st.session_state['history'] = []

if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hello! Feel free to start our chat! 🤗"]

if 'past' not in st.session_state:
    st.session_state['past'] = ["Hey! 👋"]

def conversational_chat(query):
    # Combine history into a single conversation context
    context = "\n".join([f"User: {msg[0]}\nAssistant: {msg[1]}" for msg in st.session_state['history']])
    prompt = f"{context}\nUser: {query}\nAssistant:"
    # Generate response from the model, passing prompt as a list
    result = llm.generate([prompt])
    answer = result.generations[0][0].text  # Accessing the generated text
    # Store the new interaction in history
    st.session_state['history'].append((query, answer))
    return answer

# container for the chat history
response_container = st.container()
# container for the user's text input
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_input("Query:", placeholder="Start our conversation here!", key='input')
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        output = conversational_chat(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="big-smile")
            message(st.session_state["generated"][i], key=str(i), avatar_style="thumbs")