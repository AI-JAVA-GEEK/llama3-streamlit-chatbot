from ollama import chat
import streamlit as st

st.title("🤖 Build Your Own Local AI Chatbot with Ollama & Streamlit")

if "llama3.2" not in st.session_state:
    st.session_state["llama3.2"] = "llama3.2"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Prompt input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        full_response = ""
        stream = chat(
            model='llama3.2',
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        placeholder = st.empty()
        for chunk in stream:
            content = chunk['message']['content']
            full_response += content
            placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
