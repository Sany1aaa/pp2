path1 = r"C:\Users\Сания\pp2\pp2\lab6\text.txt"
path2 = r"C:\Users\Сания\pp2\pp2\lab6\text.txt"

fp1 = open(path1, "r")
fp2 = open(path2, "w")

for i in fp1:
    fp2.write(i)

fp1.close()
fp2.close()

fp2 = open(path2, "r")

for i in fp2:
    print(i)
