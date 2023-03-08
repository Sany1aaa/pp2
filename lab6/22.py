import os

first = 'built-in.py'
first_path = os.path.abspath(first)
second = 'directories.py'
second_path = os.path.abspath(second)

files_path = [first_path, second_path]

for i in files_path:
    print('Exist:', os.access(i, os.F_OK))
    print('Readable:', os.access(i, os.R_OK))
    print('Writable:', os.access(i, os.W_OK))
    print('Executable:', os.access(i, os.X_OK))
