import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
)

# Create a prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 3 simple bullet points."
)

# Create the output parser
parser = StrOutputParser()

# Connect prompt -> model -> parser
chain = prompt | model | parser

# Run the chain
response = chain.invoke({"topic": "LangChain"})

print(response)
print(type(response))
