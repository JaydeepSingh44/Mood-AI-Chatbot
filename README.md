Mood AI Chatbot is a LangChain + Streamlit application that lets users interact with an AI agent whose responses change based on selected moods (Sad, Happy, Angry).
It demonstrates how to combine prompt engineering with a simple UI to create dynamic conversational experiences.

## Tech Stack

-Python 3.10+

-LangChain (chat models, prompt templates)

-Mistral AI (LLM backend)

-Streamlit (web UI)

## Features

🎭 Mood Selection → Choose between Sad, Happy, or Angry modes.

💬 Dynamic System Prompts → AI behavior changes based on selected mood.

🖥️ Streamlit UI → Clean browser interface with sidebar mood selector.

📜 Conversation History → Preserves chat context using st.session_state.

🛑 Exit Option → Type 0 to end the chat and view the full conversation.


MoodAIChatbot/
│── .env                  # API keys
│── requirements.txt      # Dependencies
│── mood_chatbot.py       # Main Streamlit app
