import os

path1 = r"C:\Users\Сания\pp2\pp2\lab6\test.txt"

if os.access(path1, os.F_OK) and os.access(path1, os.R_OK) and os.access(path1, os.W_OK) and os.access(path1, os.X_OK):
    os.remove(path1)
    print("File has been removed")
else:
    print("File does not exist")