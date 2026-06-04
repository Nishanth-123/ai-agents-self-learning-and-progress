# Day 2 — Structured Output

Part of [ai-agents-self-learning-and-progress](../README.md).

A resume parsing application that demonstrates structured JSON output generation from unstructured text using LLMs.

## What I Learned

- How to prompt LLMs for structured JSON output
- JSON schema design and validation
- Error handling for malformed LLM responses
- The importance of clear schema definitions

## Concepts Covered

- **Structured Output**: Generating valid JSON from unstructured text
- **Schema Design**: Defining clear JSON schemas for LLMs
- **Prompt Engineering**: Crafting prompts for reliable JSON generation
- **Error Handling**: Gracefully handling parsing failures

## Files and Purpose

- `day2.py`: Resume parser implementation
  - Defines resume text input
  - Creates JSON schema prompt
  - Calls Ollama for parsing
  - Validates and displays JSON output

## Key Learnings

1. **Schema Clarity is Critical**: Clear, well-defined schemas improve LLM accuracy
2. **Prompt Constraints Matter**: Explicitly requesting "ONLY valid JSON" reduces errors
3. **Error Handling is Essential**: LLMs can produce invalid JSON; always validate
4. **Complex Nested Structures**: LLMs can handle complex nested JSON schemas
5. **Real-world Applications**: Resume parsing is a practical use case for structured output

## Run Instructions

### Prerequisites

- Python 3.8+
- Ollama installed and running
- Llama 3.2 model pulled: `ollama pull llama3.2`

### Installation

```bash
pip install ollama
```

### Running the Application

```bash
python day2.py
```

### Usage

1. The application uses a hardcoded resume (modify `resume_text` variable)
2. It sends the resume to Llama 3.2 with JSON schema instructions
3. Displays raw output and parsed JSON
4. Shows parsing errors if JSON is invalid

## Future Improvements

- Add file input for resume text
- Implement retry logic for failed JSON parsing
- Add schema validation library (e.g., pydantic)
- Support multiple resume formats
- Add batch processing for multiple resumes
- Implement output to file
- Add more sophisticated error recovery

## Dependencies

- `ollama`: Python library for Ollama API
- `json`: Built-in Python library for JSON handling

## Technical Notes

- Uses Llama 3.2 for JSON generation
- Includes comprehensive resume example
- Demonstrates nested JSON structure parsing
- Shows both raw output and parsed result
- Handles JSON parsing exceptions gracefully

## Resume Schema

The parser extracts:
- Name
- Skills (array)
- Experience (array with company and role)
- Education (school, degree, course, passed out)
- Projects (array with name, summary, tech stack, features)
