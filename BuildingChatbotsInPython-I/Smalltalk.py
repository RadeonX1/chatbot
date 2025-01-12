responses = {
"what's your name?": "my name is EchoBot",
"what's the weather today?": "it's sunny!"
}

def respond(message):
    if message in responses:
        return responses[message]

print(respond("what's your name?"))