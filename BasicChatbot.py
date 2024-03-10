import nltk
from nltk.chat.util import Chat, reflections


patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you.', 'I\'m good. How about you?']),
    (r'fine|good', ['That\'s great!', 'Good to hear.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye. Take care.']),
    (r'(.*) your name', ['I am a chatbot.', 'You can call me ChatGPT.']),
    (r'what can you do\?', ['I can have conversations with you.']),
    (r'quit', ['Goodbye!', 'It was nice chatting with you.']),
]

chatbot = Chat(patterns, reflections)

print("Hello! I'm your chatbot. Type 'quit' to end the conversation.")
while True:
    user_input = input('You: ')
    response = chatbot.respond(user_input)
    print('Chatbot:', response)

    if user_input.lower() == 'quit':
        break
