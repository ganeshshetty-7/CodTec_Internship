import nltk
import random
import string
from nltk.corpus import wordnet
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download necessary data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Question-Answer Pairs
pairs = [
    [
        r"(hi|hello|hey|hii|heyy)",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am your friendly chatbot.", "You can call me NLP Bot!"]
    ],
   
    [
        r"how are you ?",
        ["I'm doing great, thank you!", "All good! How about you?"]
    ],
    [
        r"(.*)(help|support)(.*)",
        ["Sure, I'm here to help! What do you need support with?"]
    ],
    [
        r"(.*)(your name|who are you)(.*)",
        ["I'm an AI chatbot created with Python and NLTK."]
    ],
    [
        r"what is python ?",
        ["Python is a high-level, interpreted programming language known for its simplicity and readability."]
    ],
    [
        r"what is nltk ?",
        ["NLTK stands for Natural Language Toolkit. It's a Python library used for working with human language data."]
    ],
    [
        r"what is pandas ?",
        ["Pandas is a Python library used for data manipulation and analysis. It provides DataFrames and Series objects."]
    ],
    [
        r"what is numpy ?",
        ["NumPy is a Python library for numerical computing. It supports large, multi-dimensional arrays and matrices."]
    ],
    [
        r"what is machine learning ?",
        ["Machine learning is a field of artificial intelligence that allows computers to learn from data and make decisions."]
    ],
    [
        r"what is spaCy ?",
        ["spaCy is a modern NLP library in Python, known for its fast and accurate processing of large text data."]
    ],
    [
        r"what is the use of pip ?",
        ["pip is the package installer for Python. You can use it to install libraries from the Python Package Index."]
    ],
    [
        r"how to install a library in python ?",
        ["You can install a library using pip, for example: pip install numpy"]
    ],
    [
        r"(.*)python(.*)used for ?",
        ["Python is used for web development, data science, AI, machine learning, automation, and more."]
    ],
    [
        r"(.*)you can code in python(.*)",
        ["Yes, Python supports many domains including web, data science, AI, and scripting."]
    ],
    [
        r"how to create a function in python ?",
        ["You can define a function using the 'def' keyword. Example:\ndef greet():\n    print('Hello!')"]
    ],
    [
        r"what is a list in python ?",
        ["A list is a collection of items in a particular order. It's defined using square brackets, e.g., my_list = [1, 2, 3]"]
    ],
    [
        r"what is the difference between list and tuple ?",
        ["Lists are mutable, whereas tuples are immutable. That means you can change a list after creation, but not a tuple."]
    ],
    [
        r"what is a dictionary in python ?",
        ["A dictionary is a collection of key-value pairs. Example: my_dict = {'name': 'Alice', 'age': 25}"]
    ],
    [
        r"how to handle errors in python ?",
        ["You can handle errors using try-except blocks. Example:\ntry:\n    x = 10/0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')"]
    ],
    [
        r"what is indentation in python ?",
        ["Indentation is the space at the beginning of a line. Python uses it to define blocks of code. It's very important!"]
    ],
    [
        r"how to read a file in python ?",
        ["You can use open() function. Example:\nwith open('file.txt', 'r') as f:\n    data = f.read()"]
    ],
    [
        r"what is pip install ?",
        ["'pip install' is used to install Python packages from the Python Package Index (PyPI)."]
    ],
    [
        r"how to install nltk ?",
        ["You can install it by running: pip install nltk"]
    ],
    [
        r"what is an IDE ?",
        ["IDE stands for Integrated Development Environment. Examples: PyCharm, VS Code, Jupyter Notebook."]
    ],
    [
        r"what is jupyter notebook ?",
        ["Jupyter Notebook is an open-source tool that allows you to write and run Python code in your browser."]
    ],
    [
        r"how to import a library in python ?",
        ["Use the import keyword. Example: import numpy as np"]
    ],
    [
        r"what is recursion ?",
        ["Recursion is a function that calls itself. It's useful for problems that can be broken into similar sub-problems."]
    ],
    [
        r"how to write comments in python ?",
        ["Use '#' for single-line comments. For multi-line, use triple quotes: ''' your comment '''"]
    ],
    [
        r"what are python data types ?",
        ["Common data types: int, float, str, list, tuple, dict, set, bool"]
    ],
    [
        r"quit",
        ["Bye! Have a great day.", "See you later!"]
    ]
]

# Chatbot initialization
chatbot = Chat(pairs, reflections)

# Optional input cleaner (not currently used by nltk.chat but good to have)
def preprocess_input(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    return [word for word in tokens if word not in stop_words and word not in string.punctuation]

# Main chatbot loop
def run_chatbot():
    print("🤖 Hi! I am your AI chatbot made using Python + NLTK.")
    print("💬 Type 'quit' to exit or 'suggest' to see sample questions.")
    
    print("\n💡 Try asking questions like:")
    print("- What is Python?")
    print("- How to install a library in Python?")
    print("- What is machine learning?")
    print("- What is recursion?")
    print("- What is the use of pip?\n")

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Bot: Goodbye!")
            break
        elif user_input.lower() == 'suggest':
            print("\n💡 Here are some example questions you can try:")
            print("- What is pandas?")
            print("- How to create a function in Python?")
            print("- What is the difference between list and tuple?")
            print("- What is an IDE?")
            print("- How to handle errors in Python?\n")
            continue
        else:
            response = chatbot.respond(user_input)
            if response:
                print("Bot:", response)
            else:
                print("Bot: I'm not sure how to respond to that. Type 'suggest' for ideas.")

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
