n = int(input())
x = (i for i in range(1, n + 1))
for num in x:
    if num % 2 == 0:
        print(num,end=", ")

