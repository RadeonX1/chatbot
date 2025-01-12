# Create templates
bot_template = "BOT : {0}"
user_template = "USER : {0}"

def respond(message):
    # Concatenate the user's message to the end of a standard bot response
    bot_message = "I can hear you! You said: " + message
# Return the result
    return bot_message

# Define a function that sends a message to the bot: send_message
def send_message():
    while True:
        message = input("USER: ")

        if message.lower() == 'bye':
                print("BOT: Goodbye!")
                break
        
        response = respond(message)

        print(bot_template.format(response))

# Send a message to the bot
send_message()