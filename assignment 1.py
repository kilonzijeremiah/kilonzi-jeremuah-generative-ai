import random

def kilonzi_chatbot():
    # Pre-defined responses for basic conversation
    responses = {
        "hi": ["Hey there! Ready to chat or calculate? 😎", "Yo, what's up? Want a math joke?"],
        "hello": ["Hi! I'm your friendly chatbot, part calculator, part comedian!", "Hello, math wizard! What's on your mind?"],
        "how are you": ["I'm just a bundle of code, but I'm feeling *prime*! How about you?", "Doing great, thanks for asking! Want to hear a joke?"],
        "bye": ["Catch ya later, mathlete!", "Goodbye, my friend—keep calculating!"],
        "joke": ["Why did the number go to therapy? It had an identity crisis! 😄 Want another?", "What did zero say to eight? Nice belt! Another one?"],
        "calculate": ["Sure thing! Give me two numbers and an operator (+, -, *, /). E.g., 'calculate 2 + 3'."],
        "who are you": ["I'm Grok's fun cousin, here to chat, joke, and calculate! What's your vibe?"]
    }

    print("Welcome to the Special Chatbot! 😄 Type 'quit' to exit, 'joke' for a laugh, or 'calculate' for math! (Case-insensitive)")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if not user_input:
            print("Bot: Whoops, you didn't type anything! Try 'hi', 'joke', or 'calculate'.")
            continue
        
        if user_input == "quit":
            print("Bot: See ya, math and joke lover! 😎")
            break
        
        # Check for calculation request
        if user_input.startswith("calculate"):
            try:
                # Expect input like "calculate 5 + 3"
                parts = user_input.split()
                if len(parts) == 4 and parts[2] in ["+", "-", "*", "/"]:
                    num1, op, num2 = float(parts[1]), parts[2], float(parts[3])
                    if op == "/" and num2 == 0:
                        print("Bot: Error: Can't divide by zero!")
                    else:
                        if op == "+":
                            result = num1 + num2
                        elif op == "-":
                            result = num1 - num2
                        elif op == "*":
                            result = num1 * num2
                        elif op == "/":
                            result = num1 / num2
                        print(f"Bot: Result = {result}")
                else:
                    if len(parts) == 4:
                        print("Bot: Invalid operator! Use +, -, *, or /.")
                    else:
                        print("Bot: Please use format 'calculate <num1> <op> <num2>' (e.g., 'calculate 5 + 3').")
            except ValueError:
                print("Bot: Invalid numbers! Try again, like 'calculate 2 + 3' or 'calculate 5.5 * 2'.")
            continue
        
        # Look for matching response by checking whole words
        words = user_input.split()
        response = None
        for key in responses:
            if key in words:
                response = random.choice(responses[key])
                break
        
        # Default response if no match
        if response:
            print(f"Bot: {response}")
        else:
            print("Bot: Hmm, not sure what you mean! Try 'hi', 'joke', 'calculate', or 'bye'.")

# Run the chatbot
if __name__ == "__main__":
    kilonzi_chatbot()