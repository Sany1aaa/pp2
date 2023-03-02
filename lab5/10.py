import re

def camel_to_snake(string):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()

string = input("Enter the camel case string: ")
snake_string = camel_to_snake(string)
print("Snake case string: ", snake_string)