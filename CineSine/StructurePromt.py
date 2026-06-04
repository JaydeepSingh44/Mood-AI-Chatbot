from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List,Optional
from langchain_core.output_parsers import PydanticOutputParser

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-2506")


class Movie(BaseModel):
    title:str
    release_date:Optional[int]
    genre:List[str]
    director:Optional[str]
    cast:List[str]
    rating:Optional[float]
    short_summary:str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ("system","""
Extract movi info from paragraph 
     {format_instruction}
"""),
      
      ("human","""
       {paragraph}
        
       """) 
])


para = input("give your paragraph: ")

final_prompt = prompt.invoke(
    {"paragraph":para,
     "format_instruction": parser.get_format_instructions()
     }
)

response =model.invoke(final_prompt)



# Print structured output
print(response.content)