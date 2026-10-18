
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# 1. Define the output structure
class Student(BaseModel):
    name: str = Field(description="Student's full name")
    age: int = Field(description="Student's age")
    skills: list[str] = Field(description="Student's skills")

# 2. Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0,
)

# 3. Create the parser
parser = PydanticOutputParser(pydantic_object=Student)

# 4. Create the prompt
prompt = ChatPromptTemplate.from_template(
    "Extract student details from this text:\n{text}\n\n"
    "{format_instructions}"
)

# 5. Create the chain
chain = prompt | model | parser

# 6. Invoke the chain
response = chain.invoke({
    "text": "John Doe is 21 years old and knows Python, Go, and SQL.",
    "format_instructions": parser.get_format_instructions(),
})

print(response)
print(type(response))

# Access individual fields
print(response.name)
print(response.age)
print(response.skills)
