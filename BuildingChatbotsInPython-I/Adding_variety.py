# Import the random module
import random
import time

bot_template = "BOT : {0}"

name = "Bot"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
    "what's your name?": [
        "my name is {0}".format(name),
        "they call me {0}".format(name),
        "I am {0}".format(name)
    ],

    "what's today's weather?": [
        "the weather is {0}".format(weather),
        "it's {0} today".format(weather)
    ],

    'statement': [
        'tell me more!',
        'why do you think that?',
        'how long have you felt this way?',
        'I find that extremely interesting',
        'can you back that up?', 'oh wow!',
        ':)'
    ],

    'question': [
        "I don't know :(",
        'you tell me!'
    ],

     'xxxn': [
        ":(",
        'you tell me!'
    ],

    "default": ["คือระ ?"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = random.choice(responses["default"])

    return bot_message

def send_message():
    print(bot_template.format("Hi!"))

    while True:
        message = input("USER: ")

        if message.lower() == 'bye':
                print("BOT: Goodbye!")
                break
        
        time.sleep(1)

        response1 = respond(message)

        print(bot_template.format(response1))



# Send a message to the bot
send_message()