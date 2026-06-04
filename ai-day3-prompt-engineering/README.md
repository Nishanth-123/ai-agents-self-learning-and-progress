# Day 3 — Prompt Engineering

Part of [ai-agents-self-learning-and-progress](../README.md).

An email generator demonstrating advanced prompt engineering techniques with constraints and specific output formatting.

## What I Learned

- How to write effective prompts with specific constraints
- The importance of clear output format specifications
- Balancing creativity with constraints
- Role-based prompting for context setting

## Concepts Covered

- **Prompt Constraints**: Limiting output length, tone, and content
- **Output Formatting**: Specifying exact output structure
- **Role Prompting**: Setting AI persona for better results
- **CTA Integration**: Including call-to-action in generated content

## Files and Purpose

- `day3_email_writer.py`: Email generator implementation
  - Defines role-based system prompt
  - Specifies constraints (word count, tone, content)
  - Requests specific output format (Subject/Body)
  - Generates recruiter outreach email

## Key Learnings

1. **Constraints Improve Quality**: Specific constraints lead to more focused outputs
2. **Role Setting Matters**: Defining the AI's role improves relevance
3. **Format Specifications**: Explicit output format reduces post-processing
4. **Word Count Limits**: LLMs can respect length constraints when clearly stated
5. **Professional Tone**: Tone specifications dramatically change output style

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
python day3_email_writer.py
```

### Usage

1. Run the script
2. It generates a recruiter outreach email
3. Output includes both Subject and Body
4. Email is under 120 words with professional tone
5. Includes React and TypeScript mentions as specified

## Future Improvements

- Add input parameters for customization (company, role, skills)
- Implement multiple email templates
- Add A/B testing capability
- Include recipient name personalization
- Add email validation
- Support different email types (follow-up, thank you, etc.)
- Add output to file functionality

## Dependencies

- `ollama`: Python library for Ollama API

## Technical Notes

- Single-shot generation (no conversation history)
- Uses role-based prompting for context
- Demonstrates multiple constraint types:
  - Professional tone
  - Word count limit (under 120 words)
  - Required content (React, TypeScript)
  - Call-to-action requirement
- Specifies exact output format (Subject/Body)

## Prompt Engineering Techniques Used

1. **Role Definition**: "You are a person applying for a frontend engineer role"
2. **Constraint List**: Bullet points for clear requirements
3. **Format Specification**: "Return: Subject: Body:"
4. **Context Setting**: MAANg company reference for tone
5. **Skill Requirements**: Specific technology mentions

## Example Output Structure

```
Subject: [Compelling subject line]

Body: [Professional email content under 120 words with CTA]
```
