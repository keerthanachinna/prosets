import re
print re.sub(r'(.)(.)', r'\2\1', "abcd")
