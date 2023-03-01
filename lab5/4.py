import re 

string = 'Abbbbab ABb ab a' # или сделай простой инпут
y = r"[A-Z][a-z]"
x = re.findall(y, string) #по сути находит сабстр по условию 
print(x)