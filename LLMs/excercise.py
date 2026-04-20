from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# Schema enforces EXACT keys and types
class ConceptExplanation(BaseModel):
    concept_name: str = Field(description="Name of the programming concept")
    one_line_definition: str = Field(description="One sentence definition")
    real_world_analogy: str = Field(description="A real world analogy")
    difficulty: Literal["beginner", "intermediate", "advanced"] = Field(
        description="Difficulty level — pick exactly one"
    )

parser = JsonOutputParser(pydantic_object=ConceptExplanation)
model = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Always respond in valid JSON only. No explanation, no markdown."),
    ("human", "Explain this programming concept: {topic}\n{format_instructions}")
]).partial(format_instructions=parser.get_format_instructions())

chain = prompt | model | parser

for concept in ["recursion", "pointers", "transformers"]:
    result = chain.invoke({"topic": concept})
    print(f"\n--- {concept.upper()} ---")
    print(f"Definition : {result['one_line_definition']}")
    print(f"Analogy    : {result['real_world_analogy']}")
    print(f"Difficulty : {result['difficulty']}")