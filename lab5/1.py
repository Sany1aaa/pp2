import re 

string = 'abbbbbab abb ab a' # или сделай простой инпут
y = r"ab*" # (*) значит zero or more

x = re.findall(y, string) #по сути находит сабстр по условию 
print(x)