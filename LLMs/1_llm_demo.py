from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# load environment variables
load_dotenv()

# 1. Create the model — this is your "LLM handle"
model = ChatGroq(
    model="llama-3.1-8b-instant",  # fast & free on Groq
    temperature=0.7                # 0 = deterministic, 1 = creative
)
# 2. Build a list of messages
messages = [
    SystemMessage(content="You are a joker."),
    HumanMessage(content="Explain debugging.")
]
# 3. Invoke the model
response = model.invoke(messages)

# 4. Read the response
print(response.content)
# print(type(response))  # AIMessage