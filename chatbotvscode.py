import streamlit as st
import ollama

st.title("JAY")

# Initialize session state keys if they don't exist
if "model" not in st.session_state:
    st.session_state["model"] = "Jay"  # Replace with your actual default model if needed

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def word_per_word():
        stream = ollama.chat(
            model=st.session_state["model"],
            messages=st.session_state["messages"],
            stream=True,
        )
        for chunk in stream:
            yield chunk["message"]["content"]

# Display chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input and chat messages
if prompt := st.chat_input("Hello There! Aske me anything!"):
    st.session_state["messages"].append({"role": "user", "content": prompt})

    with st.chat_message(name="user", avatar="😎"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message = st.write_stream(word_per_word())
        st.session_state["messages"].append({"role": "assistant", "content": message})
