import re

# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

responses = {
    'greet': 'Hello you! :)',
    'goodbye': 'Goodbye for now',
    'thankyou': 'You are very welcome',
    'default': 'Default message'
}

# Define a dictionary 'keywords'.
keywords = {
    'greet': ['hello', 'hi', 'hey'],
    'goodbye': ['bye', 'farewell'],
    'thankyou': ['thank', 'thx']
}

# Define a dictionary of patterns
patterns = {}

# Iterate over the keywords dictionary
for intent, words in keywords.items():
    # Create a regular expression and compile it into a pattern object
    pattern = re.compile(r'\b(' + '|'.join(words) + r')\b')
    patterns[intent] = pattern

# Define a function to find the intent of a message
def match_intent(message):
    matched_intent = None
    for intent, pattern in patterns.items():
        # Check if the pattern occurs in the message
        if pattern.search(message):
            matched_intent = intent
            break
    return matched_intent

# Define a respond function
def respond(message):
    # Call the match_intent function
    intent = match_intent(message)
    # Fall back to the default response
    key = "default"
    if intent in responses:
        key = intent
    return responses[key]

# Define a function that sends a message to the bot
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response
    print(bot_template.format(response))

# Send messages
send_message("hello!")
send_message("bye byeee")
send_message("thank you much!")
