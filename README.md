# LangChain Output Parser Examples

Small Python examples showing how to turn Gemini responses into plain text,
JSON objects, dictionaries, and validated Pydantic models with LangChain.

## Contents

| File | Description |
| --- | --- |
| [`strOutputParser.py`](./strOutputParser.py) | Uses `StrOutputParser` to return a model response as a string. |
| [`jsonOutputParser.py`](./jsonOutputParser.py) | Uses `JsonOutputParser` to request and parse a JSON object containing a topic and bullet points. |
| [`structuredOutputParserOP.py`](./structuredOutputParserOP.py) | Uses `StructuredOutputParser` and `ResponseSchema` to extract student details into a dictionary. |
| [`pydanticOP.py`](./pydanticOP.py) | Uses `PydanticOutputParser` to extract and validate student details with a `Student` model. |
| [`requirements.txt`](./requirements.txt) | Python packages required by the examples. |

## Requirements

- Python 3.9 or newer
- A Google Gemini API key
- Network access to the Gemini API

The examples use the `gemini-2.5-flash` model. If that model is unavailable for
your account, update the `model` value in the scripts.

## Setup

From this directory, create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create a `.env` file in this directory and add your API key:

```dotenv
GEMINI_API_KEY=your_gemini_api_key
```

The scripts load this variable with `python-dotenv`. Keep `.env` private; it is
excluded by [`.gitignore`](./.gitignore).

## Run an example

Run the scripts from the `output` directory:

```powershell
python strOutputParser.py
python jsonOutputParser.py
python structuredOutputParserOP.py
python pydanticOP.py
```

Each script prints the parsed response and, where relevant, demonstrates access
to individual fields.

## What the examples demonstrate

- **String output**: use `StrOutputParser` when the application needs the
  model's response as plain text.
- **JSON output**: use `JsonOutputParser` when the response should be a JSON
  object that can be accessed by keys.
- **Structured output**: use `StructuredOutputParser` with response schemas to
  describe expected fields and parse the result into a dictionary.
- **Pydantic output**: use `PydanticOutputParser` when runtime validation and
  typed model fields are needed.

These scripts are educational examples. They send requests directly to Gemini
and do not include retries, persistence, or production secret management.