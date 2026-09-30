import re
from datetime import datetime


def get_reply(message):
    text = message.lower().strip()

    if re.search(r"\b(hi|hello|hey)\b", text):
        return "Hello! How can I help you?"

    if "your name" in text:
        return "I am a simple rule-based chatbot."

    if "help" in text:
        return "You can ask me about my name, time, date, or say hello."

    if "time" in text:
        return "The current time is " + datetime.now().strftime("%I:%M %p")

    if "date" in text or "today" in text:
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    if re.search(r"\b(thank you|thanks)\b", text):
        return "You're welcome!"

    if re.search(r"\b(bye|exit|quit)\b", text):
        return "Goodbye! Have a nice day."

    return "I didn't understand that. Type 'help' to see what I can answer."


print("Simple Chatbot")
print("Type 'bye' to stop the chat.\n")

while True:
    user_input = input("You: ")
    reply = get_reply(user_input)
    print("Bot:", reply)

    if user_input.lower().strip() in {"bye", "exit", "quit"}:
        break
