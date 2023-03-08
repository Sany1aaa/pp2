cnt = 0
x = ("Hello", "World", 1, 2, 3, True, "jfngd", "sigsh", "")

for i in x:
    if bool(i):
         cnt += 1

print(cnt) 
if cnt == len(x):
     print(True)
else:
     print(False)
