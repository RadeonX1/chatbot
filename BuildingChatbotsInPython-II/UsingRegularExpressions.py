import re

print(re.search(r"\b(hello|hey|hi)\b", "hey there!") is not None)

print(re.search(r"\b(hello|hey|hi)\b", "which one?") is not None)