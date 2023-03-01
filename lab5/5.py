import re 

string = 'abbbbab abb ab a' 
y = r"a.*b$"
x = re.findall(y, string) #по сути находит сабстр по условию 
print(x)