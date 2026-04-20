from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

# Define the template — {topic} and {level} are variables
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert teacher. Always explain things with a real-world analogy."),
    ("human", "Explain {topic} to someone who is a {level} in programming in {language}.")
])

# Fill in the variables — this produces the final messages list
filled_prompt = prompt.invoke({
    "topic": "recursion",
    "level": "beginner",
    "language": "hindi"
})

print(filled_prompt)   # See what the template produced
print("---")

response = model.invoke(filled_prompt)
print(response.content)