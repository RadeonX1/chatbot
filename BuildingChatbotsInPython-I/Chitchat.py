bot_template = "BOT : {0}"

# Define variables
name = "Bot"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
"what's your name?": "my name is {0}".format(name),
"what's today's weather?": "the weather is {0}".format(weather),
"default": "default message"
}

# Return the matching response if there is one, default otherwise
def response(message):
    # Check if the message is in the responses
    if message in responses:
    # Return the matching message
        bot_message = responses[message]
    else:
    # Return the "default" message
        bot_message = responses["default"]
    return bot_message

def send_message():
    while True:
        message = input("USER: ")

        if message.lower() == 'bye':
                print("BOT: Goodbye!")
                break
        
        response1 = response(message)

        print(bot_template.format(response1))

# Send a message to the bot
send_message()