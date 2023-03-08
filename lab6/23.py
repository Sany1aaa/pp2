import os

p1 = ('c:\Users\Сания\pp2\pp2\lab6')
print(os.path.exists(p1))
p2 = os.path.abspath('22.py')
print(os.path.exists(p2))
print(os.path.basename(p2))
print(os.path.dirname(p2))
