import re 

string = 'abbbbaab_abb_ab_a' # или сделай простой инпут
y = r"[a-z]_[a-z]" 

x = re.findall(y, string) #по сути находит сабстр по условию 
print(x)