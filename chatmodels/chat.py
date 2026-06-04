from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("mistral-small-2603")

response= model.invoke("what is cricket?")
print(response.content)