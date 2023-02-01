thisset = {"apple", "banana", "cherry", "apple"} # no dublicates
print(thisset)
print(len(thisset))
# Set items are unordered, unchangeable, and do not allow duplicate values.
print(type(thisset))

# loop through the set
for x in thisset:
  print(x)

#checking
print("banana" in thisset)


#adding
thisset.add("orange")
print(thisset)

#updating
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#removing
thisset.remove("banana")
print(thisset)
# or discard
thisset.discard("apple")
print(thisset)

#remove random item
x = thisset.pop()
print(x)
print(thisset)

#clear the set
thisset.clear()
print(thisset)

#delete completely
#   del thisset

#JOin sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1.intersection_update(set3)
print(set1)



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

a = {"a", "b", "c"}
b = {"f", "e", "d", "c", "b", "a"}
c = a.issubset(b)
print(c)
