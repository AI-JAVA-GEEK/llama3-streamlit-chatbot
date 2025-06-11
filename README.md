# 🤖 Build Your Own Local AI Chatbot with Ollama & Streamlit

## Environment
- **Windows Desktop**
- **Languages**: Python
- **Application Type**: LLM Examples

## About Ollama

https://github.com/ollama/ollama

Ollama is opensource application that will helps to create and run the Large Language Models in local machines. We can install the software in any of the location desktops and can run models in local and can use it.

Ollama support many models and we simply can pull the model into local machine and can start the specific model. Below is github repository of Ollama and can explore more about the models.

Current Example will shows how to develop simple chatbot that interact with OLLAMA models that will provide two way interaction chat.

## Technologies Used

Python is primary language used for the use case and to build chatbot, I have used the streamlit Python GUI library.

Streamlit open source GUI library and it can build User Interface applications very rapid. It has more documentation that help to build easy to complex gui applications.

## Installation

### Install Ollama In Local Machine

Download Ollama here https://ollama.com/download/windows

Open window powershell and run the model with following command:
```powershell
ollama run llama3.2
```

We can also can choose plenty of models for available list.

### Few Important Commands

```powershell
ollama stop llama3.2
ollama ps
ollama serve  # used when you want to start ollama without running the desktop application
```

### Install Python

Download python for windows and install: https://www.python.org/downloads/

### Install Streamlit

Install streamlit using pip command:
```powershell
pip install streamlit
```

## Setup Application

### Create Directory and App File

Create directory and create app.py

Use below code in the app.py:

```python
from ollama import chat
import streamlit as st

st.title("Riyanshika Hayansh Chatbot")

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
```

### Start Chatbot

Start chatbot from powershell:
```powershell
streamlit run app.py
```

**Local URL**: http://localhost:8501

## Documentation

Go through streamlit documentation and understand the streamlit libraries and its build in functions.

Follow below Streamlit docs that will help us build chatbot like regular LLM chat bots:
https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps

## Source Code

https://github.com/AI-JAVA-GEEK/llama3-streamlit-chatbot

![Chatbot Screenshot](images/1.png)