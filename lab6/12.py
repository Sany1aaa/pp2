
string = input()
cntL = 0
cntU = 0
for i in string:
    if(ord(i) >= 65 and ord(i) <= 90):
         cntU += 1
    elif(ord(i) >= 97 and ord(i) <= 122):
         cntL += 1
print("Upper:", cntU,"\n"+"Lower:", cntL)
