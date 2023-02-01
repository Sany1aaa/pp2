thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020, # no dublicates
  "colors": ["red", "white", "blue"]
}


print(thisdict)
print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
x = thisdict.keys()  #ключи
x = thisdict.values() # их значения
x = thisdict.items() # ключ + значение 

x = thisdict.get("model")
print(x)

#remove
thisdict.pop("model")
print(thisdict)
#remove last item
thisdict.popitem()
print(thisdict) 
# есть del и clear (удаляет и очищает)

     # циклично выводит элементы 1 by 1

for x in thisdict:
  print(x) #keys
  print(thisdict[x]) #values(значения)

mydict = thisdict.copy()
print(mydict)


#NESTED DICTIONARIES
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
