
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import (StructuredOutputParser, ResponseSchema)

load_dotenv()

# Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7,
)

# Define the expected response fields
response_schemas = [
    ResponseSchema(
        name="name",
        description="The student's full name",
        type="string",
    ),
    ResponseSchema(
        name="age",
        description="The student's age in years",
        type="int",
    ),
    ResponseSchema(
        name="skills",
        description="A list of the student's skills",
        type="list",
    ),
]

# Create the output parser
parser = StructuredOutputParser.from_response_schemas(
    response_schemas
)

# Get formatting instructions
format_instructions = parser.get_format_instructions()

# Create the prompt
prompt = ChatPromptTemplate.from_template(
    "Extract student information from this text: {text}\n\n"
    "{format_instructions}"
)

# Connect everything into one chain
chain = prompt | model | parser

# Run the chain
response = chain.invoke({
    "text": (
        "John Doe is 21 years old and knows Python, Go, "
        "and SQL."
    ),
    "format_instructions": format_instructions,
})

print(response)
print(type(response))
print(response["name"])
print(response["skills"])
