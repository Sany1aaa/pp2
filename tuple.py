thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) 

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry")) 
print(type(mytuple))

print(thistuple[1])

print(thistuple[0:2])

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#adding elements
  y = ("orange",)
thistuple += y

print(thistuple)
#removing
y = list(thistuple)
y.remove("apple")
print(thistuple)


#unpacking
fruits = ("apple", "banana", "cherry")

mytuple = fruits * 2 # умножаем 

print(mytuple)


(green, yellow, *red) = fruits
 # *red добавляет значение остальных элементов и становится tuple
print(green)
print(yellow)
print(red)





