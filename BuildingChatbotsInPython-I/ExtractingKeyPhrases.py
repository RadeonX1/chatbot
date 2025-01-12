import re
pattern = "if (.*)"
message = "what would happen if bots took over the world"
match = re.search(pattern, message)

print(match.group(0))

print(match.group(1))