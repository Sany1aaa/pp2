def func(n):
    for i in range(n, 0, -1):
        yield i

n = int(input())
x = func(n)
for i in x:
    print(i)
    