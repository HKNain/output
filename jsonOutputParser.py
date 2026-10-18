
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
)

# Create JSON output parser
parser = JsonOutputParser()

# Create prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in 3 simple bullet points. "
    "Return the result as a JSON object with a 'topic' "
    "field and a 'points' field containing a list of strings.\n"
    "{format_instructions}"
)

# Create one chain
chain = prompt | model | parser

# Invoke the chain
response = chain.invoke({
    "topic": "LangChain",
    "format_instructions": parser.get_format_instructions(),
})

print(response)
print(type(response))
print(response["topic"])
print(response["points"])
