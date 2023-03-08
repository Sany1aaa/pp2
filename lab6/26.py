import os

for i in range(65, 90):
      path = r"C:\Users\Сания\pp2\pp2\lab6"
      name = os.path.join(path, chr(i) +".txt")
      f = open(name, "a")
for i in os.listdir(path):
     print(i)
