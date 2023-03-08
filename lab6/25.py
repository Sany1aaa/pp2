l = ["apple", "banana", "orange", "melon"]
with open("text.txt", 'w') as fp:
    for i in l:
       fp.write(i)
