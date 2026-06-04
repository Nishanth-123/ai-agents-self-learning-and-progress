# Day 5 — Agent Loop

Part of [ai-agents-self-learning-and-progress](../README.md).

A sophisticated multi-step agent system for expense tracking with automatic tool orchestration and decision-making.

## What I Learned

- How to build autonomous agent systems
- Multi-step tool orchestration and execution
- Agent loop design with step limits
- Complex task decomposition
- Error handling in agent workflows

## Concepts Covered

- **Agent Architecture**: Designing autonomous AI systems
- **Tool Orchestration**: Automatic tool selection and execution
- **Agent Loop**: Multi-step reasoning and execution cycles
- **Task Decomposition**: Breaking complex tasks into tool calls
- **State Management**: Maintaining conversation state across steps
- **Error Recovery**: Handling tool failures gracefully

## Files and Purpose

- `agent.py`: Core agent implementation
  - Defines agent loop with step limits
  - Manages tool execution and result handling
  - Implements message history management
  - Handles tool errors and retries

- `tools.py`: Tool definitions and implementations
  - `calculate_expenses`: Computes total and highest spending
  - `categorize_expenses`: Categorizes expenses by type
  - `save_report`: Saves final report to file

- `main.py`: Entry point
  - Defines user prompt
  - Initiates agent execution

## Key Learnings

1. **Agent Autonomy**: Agents can autonomously decide which tools to use
2. **Step Limits**: Prevent infinite loops with max step constraints
3. **Tool Chaining**: Agents can chain multiple tool calls for complex tasks
4. **Error Handling**: Graceful error handling prevents agent failure
5. **State Management**: Maintaining conversation history is critical
6. **Task Decomposition**: Agents break complex requests into tool calls

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
python main.py
```

### Usage

1. Run the script
2. Agent processes the expense tracking request
3. Watch the step-by-step execution:
   - Step 1: Agent decides to extract expenses
   - Step 2: Agent calculates totals
   - Step 3: Agent categorizes expenses
   - Step 4: Agent saves report
4. Final answer is displayed
5. Report is saved to `expense_report.txt`

## Future Improvements

- Add more expense categories
- Implement expense date tracking
- Add budget comparison features
- Support file input for expense data
- Add expense visualization
- Implement multi-user support
- Add expense history and trends
- Support currency conversion
- Add receipt image processing
- Implement expense approval workflow

## Dependencies

- `ollama`: Python library for Ollama API
- `json`: Built-in Python library

## Technical Notes

### Agent Architecture

```
User Input → Agent Loop → Tool Selection → Tool Execution → Result Processing
                ↑                                              ↓
                └────────────── Message History ←──────────────┘
```

### Tool Definitions

1. **calculate_expenses**: 
   - Input: Expense dictionary
   - Output: Total, highest spending item
   - Used for: Computing expense summaries

2. **categorize_expenses**:
   - Input: Expense dictionary
   - Output: Categorized expenses (food, transport, entertainment, other)
   - Used for: Organizing expenses by type

3. **save_report**:
   - Input: Report text
   - Output: File save confirmation
   - Used for: Persisting results

### Agent Loop Features

- Maximum 10 steps to prevent infinite loops
- Automatic tool selection based on user request
- Error handling for tool failures
- Step-by-step execution logging
- Final answer generation after tool completion

## Example Workflow

Input: "I spent a lot on food this week"

Agent Execution:
1. Extracts expense data from natural language
2. Calls `calculate_expenses` with extracted data
3. Calls `categorize_expenses` for organization
4. Calls `save_report` to persist results
5. Provides final summary to user

## Output Files

- `expense_report.txt`: Generated expense report
