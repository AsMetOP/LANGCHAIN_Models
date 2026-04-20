# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# model = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
# parser = StrOutputParser()

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant."),
#     ("human", "{question}")
# ])

# chain = prompt | model | parser  # template → model → parser

# response = chain.invoke({"question": "What is LangChain in one line?"})

# print(response)        # plain string, no .content needed
# print(type(response))  # <class 'str'>

# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import JsonOutputParser

# load_dotenv()

# model = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
# parser = JsonOutputParser()

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant. Always respond in valid JSON only. No explanation, no markdown."),
#     ("human", "Give me 3 facts about {topic}. Return as: {{\"facts\": [\"fact1\", \"fact2\", \"fact3\"]}}")
# ])

# chain = prompt | model | parser

# result = chain.invoke({"topic": "black holes"})

# print(result)            # Python dict
# print(result["facts"])   # List of facts
# print(result["facts"][0]) # First fact

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import List

load_dotenv()

# 1. Define your expected output shape
class MovieRecommendation(BaseModel):
    title: str = Field(description="Movie title")
    year: int = Field(description="Release year")
    reason: str = Field(description="Why this movie is recommended")

class MovieList(BaseModel):
    movies: List[MovieRecommendation]

# 2. Create parser from the schema
parser = JsonOutputParser(pydantic_object=MovieList)

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a movie expert."),
    ("human", "Recommend 2 movies about {theme}.\n{format_instructions}")
]).partial(format_instructions=parser.get_format_instructions())

chain = prompt | model | parser

result = chain.invoke({"theme": "artificial intelligence"})

print(result)
for movie in result["movies"]:
    print(f"{movie['title']} ({movie['year']}) — {movie['reason']}")