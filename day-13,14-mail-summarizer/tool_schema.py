READ_INBOX_TOOL = {
    "type": "function",
    "function": {
        "name": "read_inbox",
        "description": (
            "Read emails from Gmail. "
            "The 'query' parameter must be a single Gmail search string "
            "such as 'from:user@example.com newer_than:7d'. "
            "Do not pass objects for 'query' or 'max_results'."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "max_results": {
                    "type": "integer"
                },
                "query": {
                    "type": "string"
                }
            },
            "required": ["max_results", "query"]
        }
    }
}