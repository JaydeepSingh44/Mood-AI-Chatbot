import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI


load_dotenv()


model = ChatMistralAI(model="mistral-small-2506")


st.set_page_config(page_title="Movie Info Extractor", page_icon="🎬")
st.title("🎬 Movie Information Extraction Assistant")


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful structured information from a movie paragraph and present it in a clean re

Rules:
Do NOT add explanations
Do NOT add extra commentary
Follow the exact format
If information is missing - write NULL
Keep summary short (2-3 lines max)
Do NOT guess unknown facts

Output Format:
Movie Title:
Release Year:
Genre:
Setting/Location:
Plot:
Themes:
Rating:
Notable Features:
Short Summary:
"""
        ),
        (
            "human",
            """
Extracted infor from paragraph :

{paragraph}

"""
        )
    ]
)


para = st.text_area("Paste your movie paragraph here:")


if st.button("Extract Information"):
    if para.strip():
        final_prompt = prompt.invoke({"paragraph": para})
        response = model.invoke(final_prompt)
        st.text_area("Extracted Information:", value=response.content, height=300)
    else:
        st.warning("Please enter a movie paragraph first.")
