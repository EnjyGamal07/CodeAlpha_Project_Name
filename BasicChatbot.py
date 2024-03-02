import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you", ["I'm doing well, thank you!", "I'm good. How about you?"]),
    (r"what is your name", ["I'm a chatbot created with Python!"]),
    (r"quit|exit", ["Goodbye!", "Bye!", "See you later!"]),
    # Add your own patterns and responses here
]

# Create a chatbot using the patterns
chatbot = Chat(patterns, reflections)

def run_chatbot():
    print("Chatbot: Hi! I'm a simple chatbot. You can start a conversation with me. Type 'quit' to exit.")
    
    # Start the conversation loop
    while True:
        user_input = input("You: ")
        
        # Check for user exit
        if user_input.lower() in ["quit", "exit"]:
            print("Chatbot: Goodbye!")
            break

        # Get the chatbot's response based on user input
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    # Download NLTK data (if not already downloaded)
    nltk.download("punkt")
    
    # Run the chatbot
    run_chatbot()
