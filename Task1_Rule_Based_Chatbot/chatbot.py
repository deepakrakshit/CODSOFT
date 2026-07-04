from datetime import datetime

print("=" * 50)
print("          CodBot AI Chatbot")
print("=" * 50)
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.\n")

greetings = [
    "hi",
    "hello",
    "hey",
    "good morning",
    "good evening"
]

while True:

    user = input("You: ").strip().lower()

    # Greetings
    if any(word in user for word in greetings):
        print("Bot: Hello! Nice to meet you.")

    # Asking how the bot is
    elif "how are you" in user or "how's it going" in user:
        print("Bot: I'm doing great! Hope you're having a wonderful day.")

    # Bot name
    elif "your name" in user or "who are you" in user:
        print("Bot: I'm CodBot, a simple rule-based chatbot.")

    # Creator
    elif "who made you" in user or "creator" in user:
        print("Bot: I was created by Deepak as part of a CodSoft AI internship project.")

    # Time
    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Bot: Current time is {current_time}")

    # Date
    elif "date" in user or "today" in user:
        current_date = datetime.now().strftime("%d %B %Y")
        print(f"Bot: Today's date is {current_date}")

    # Help
    elif user == "help":
        print("\nAvailable commands:")
        print("- hi / hello")
        print("- how are you")
        print("- what is your name")
        print("- who made you")
        print("- time")
        print("- date")
        print("- thanks")
        print("- bye / exit\n")

    # Thanks
    elif "thank" in user:
        print("Bot: You're welcome!")

    # Bye
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    # Empty input
    elif user == "":
        print("Bot: Please type something.")

    # Unknown
    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")