import re
import random

bot_template = "BOT : {0}"

rules = {
    'do you think (.*)': [
        'if {0}? Absolutely.',
        'No chance'
    ],
    'do you remember (.*)': [
        'Did you think I would forget {0}?',
        "Why haven't you been able to forget {0}?",
        'What about {0}?',
        'Yes .. and?'
    ],
    'I want (.*)': [
        'What would it mean if you got {0}?',
        'Why do you want {0}?',
        "What's stopping you from getting {0}?"
    ],
    'if (.*)': [
        "Do you really think it's likely that {0}?",
        'Do you wish that {0}?',
        'What do you think about {0}?',
        'Really--if {0}'
    ]
}

# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None
    
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.match(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
            break  # Exit loop after the first match
    
    # Return the response and phrase
    return response.format(phrase)

# Test match_rule
# print(match_rule(rules, "do you remember your last birthday"))
# print(match_rule(rules,"do you remember my last birthday"))
# print(match_rule("do you think humans should be worried about AI"))
# print(match_rule("I want a robot friend"))
# print(match_rule("what if you could be anything you wanted"))

def replace_pronouns(message):
    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my', 'your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you', 'me', message)
    return message

def send_message():
    while True:
        message = input("USER: ")

        if message.lower() == 'bye':
                print("BOT: Goodbye!")
                break
        
        print(bot_template.format(replace_pronouns(match_rule(rules, message))))

# Send a message to the bot
send_message()