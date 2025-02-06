from typing import Optional
from dotenv import load_dotenv,dotenv_values
from langchain_core.prompts import ChatPromptTemplate,MessagePlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.utils.function_calling import convert_to_openai_tool
import os


class LLMService:
    def __init__(self):
        load_dotenv()
        self.prompt= ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert extraction algorithm. "
                    "Only extract relevant information from the text. "
                    "If you do not know the value of an attribute askrd to extract, "
                    "return null for the attribut's value. "
                
                ),
                ("human","{text}")
            ]
        )
        self.apiKey=os.getenv('OPENAI_API_KEY')
        self.llm=ChatMistralAI(api_key=self.apiKey,model="mistral-large-latest")
        self.runnable=self.prompt | self.llm.with_structered_output(schema=Expense)

    def runLLM(self,message):
        return self.runnable.invoke({"text": message})

