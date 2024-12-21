def chatbot():
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ").strip().lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm functioning perfectly. How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a rule-based chatbot. You can call me Chatbot!")
        elif "time" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {now}.")
        elif "date" in user_input:
            from datetime import datetime
            today = datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {today}.")
        elif "joke" in user_input:
            print("Chatbot: Why don't skeletons fight each other? Because they don't have the guts!")
        elif "weather" in user_input:
            print("Chatbot: I'm not connected to the internet, but it's always sunny in my virtual world!")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "help" in user_input:
            print("Chatbot: Sure! I can help you with simple questions like 'What's your name?', 'What's the time?', or 'Tell me a joke!'.")
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: You're welcome! I'm here to help.")
        elif "who made you" in user_input:
            print("Chatbot: I was created by a programmer to assist with simple tasks and conversations.")
        elif "quote" in user_input:
            print("Chatbot: Here's a quote for you: 'The only limit to our realization of tomorrow is our doubts of today.' - Franklin D. Roosevelt")
        elif "math" in user_input:
            print("Chatbot: Sure! Give me a simple math problem like '2 + 2' or '10 / 2'.")
            math_input = input("You: ").strip()
            try:
                result = eval(math_input)
                print(f"Chatbot: The result is {result}.")
            except Exception:
                print("Chatbot: Sorry, I couldn't calculate that. Make sure it's a simple math problem.")
        elif "story" in user_input:
            print("Chatbot: Once upon a time, there was a curious user who talked to a friendly chatbot. They had a great conversation and lived happily ever after!")
        elif "facts" in user_input:
            print("Chatbot: Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!")
        elif "game" in user_input:
            print("Chatbot: Let's play a quick game of rock-paper-scissors. Type 'rock', 'paper', or 'scissors'!")
            from random import choice
            options = ["rock", "paper", "scissors"]
            user_choice = input("You: ").strip().lower()
            bot_choice = choice(options)
            print(f"Chatbot: I chose {bot_choice}.")
            if user_choice == bot_choice:
                print("Chatbot: It's a tie!")
            elif (user_choice == "rock" and bot_choice == "scissors") or \
                 (user_choice == "paper" and bot_choice == "rock") or \
                 (user_choice == "scissors" and bot_choice == "paper"):
                print("Chatbot: You win! Great job!")
            else:
                print("Chatbot: I win! Better luck next time.")
        elif "riddle" in user_input:
            print("Chatbot: Here's a riddle for you: 'What has keys but can't open locks?'")
            answer = input("You: ").strip().lower()
            if "piano" in answer:
                print("Chatbot: That's correct! Great thinking.")
            else:
                print("Chatbot: The answer is 'a piano'. Better luck next time!")
        elif "color" in user_input:
            print("Chatbot: My favorite color is blue, like the vast sky of the virtual world. What's yours?")
        elif "animal" in user_input:
            print("Chatbot: I like cats. They're independent yet affectionate. How about you?")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you try rephrasing?")

if __name__ == "__main__":
    chatbot()