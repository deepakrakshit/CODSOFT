print("=" * 40)
print("      Welcome to CodBot")
print("=" * 40)

while True:
    user = input("\nYou: ").lower()

    if user == "hi":
        print("Bot: Hello!")

    elif user == "hello":
        print("Bot: Hi there!")

    elif user == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is CodBot.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")