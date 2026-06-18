from agent import run_agent


def main():
    print("📧 Inbox Summarizer Agent (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        try:
            response = run_agent(user_input)

            print("\nAssistant:")
            print(response)
            print("-" * 60)

        except Exception as e:
            print(f"\nError: {e}")
            print("-" * 60)


if __name__ == "__main__":
    main()