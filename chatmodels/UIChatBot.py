import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


load_dotenv()

model = init_chat_model("mistral-small-2603")

st.set_page_config(page_title="Funny AI Chatbot", page_icon="🤖")
st.title("🤖 Funny AI Agent")

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content="you are funny AI Agent")]

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)


if prompt := st.chat_input("Type your message (enter 0 to quit)..."):
    
    if prompt == "0":
        st.write("Chat ended. Here’s the full conversation:")
        st.write(st.session_state.messages)
    else:
        
        st.session_state.messages.append(HumanMessage(content=prompt))
        st.chat_message("user").write(prompt)

        
        response = model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
        st.chat_message("assistant").write(response.content)
