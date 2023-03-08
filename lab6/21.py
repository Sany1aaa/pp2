import os

directories = os.listdir()
files = list()

#only directories
for i in directories:
    if not os.path.isfile(i):
        print(i)

print()
 #only files
for i in directories:
    if os.path.isfile(i):
      print(i)

#files and directories
for i in directories:
    print(i, end=" ")
