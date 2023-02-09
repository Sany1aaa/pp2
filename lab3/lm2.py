def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #double the value
mytripler = myfunc(3)

print(mydoubler(11))