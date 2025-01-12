import re

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

# Print the patterns
print(patterns)
