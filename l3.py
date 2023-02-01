thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()

thislist.sort(key = str.lower) #to sort small letters first
print(thislist) 

mylist = thislist.copy() # копировать лист
#одно и то же
  #   mylist = list(thislist)
print(mylist)  

list1 = ["a", "b", "c", 3]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
print(list3.count(3))
