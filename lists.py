thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)
print(len(thislist))
print(type(thislist))
thislist = list(("a", "b", "c"))
print(thislist[1])
print(thislist[2:4])
print(thislist[2:])
print(thislist[:3])
print(thislist[-4:-1])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
thislist[1] = "blackcurrant"
print(thislist)
thislist[1:3] = ["watermelon"] # 1ден 3ке дейын(не ыключительно) заменяет 
print(thislist)
thislist.insert(2, "watermelon") # добавляет со втрого ничего не удаляя
print(thislist)
thislist.append("orange") #добавляет в конец
print(thislist)

tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical) #добавляет второй лист в первый
print(thislist)
#удаление
thislist.remove("banana")
thislist.pop(1) # удалить первыйй элемент
thislist.pop() #удалить last item
del thislist[0] #delete 



