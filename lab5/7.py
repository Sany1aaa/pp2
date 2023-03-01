def snake_to_camel(string):
    return ''.join(word.capitalize() for word in string.split('_'))

string = input("Enter the snake case string: ")
camel_string = snake_to_camel(string)
print("Camel case string: ", camel_string)