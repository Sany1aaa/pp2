import re

string = input("Enter the string: ")
new_string = ' '.join(re.findall('[A-Z][a-z]*', string))
print("Modified string: ", new_string)