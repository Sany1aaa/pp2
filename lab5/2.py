import re 

string = 'abbbbab abb ab a' # или сделай простой инпут
y = r"ab{2,3}" # c{a,b} значит c встречается а или б раз

x = re.findall(y, string) #по сути находит сабстр по условию 
print(x)