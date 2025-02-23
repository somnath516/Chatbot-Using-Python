import random
import time

class CreativeChatbot:
    def __init__(self):
        self.responses = {
            "greeting": ["Hey there! 👋", "Hello, human! 😄", "What’s up, rockstar? 🎸"],
            "farewell": ["Catch you later! 🐊", "Goodbye! 👋", "See you, space cowboy! 🚀"],
            "default": ["Can you say that again? 🤔", "Oops, I didn’t get that. 🧐", "Hmmm... not sure. 😅"],
            "joke": ["Why don’t skeletons fight each other? They don’t have the guts! 😂", 
                     "Why did the computer go to the doctor? It had a virus! 🦠", 
                     "I told my computer I needed a break... now it won’t stop sending me Kit-Kats! 😆"],
            "compliment": ["You’re awesome! ✨", "You’re a legend! 😎", "You must be a wizard! 🧙‍♂️"],
            "how_are_you": ["I’m doing great, thanks for asking! 😊", "I’m fantastic, how about you?", "I’m living the dream! 🚀"],
            "weather": ["It’s coding weather! ☀️", "I think it’s raining pixels! ☔️", "It’s always sunny in code land! 🌞"]
        }

    def chat(self):
        print("Chatbot: Welcome! Type 'bye' to exit. Let’s chat! 🎉")
        while True:
            user_input = input("You: ").lower()
            if 'bye' in user_input:
                print(f"Chatbot: {random.choice(self.responses['farewell'])}")
                break
            response = next((self.responses[key] for key in self.responses if key in user_input), self.responses['default'])
            print(f"Chatbot: {random.choice(response)}")
            time.sleep(1)

if __name__ == "__main__":
    CreativeChatbot().chat()
