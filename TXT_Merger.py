import os
import glob


path = input('Enter the path you want to search: ')
os.chdir(path)
files = glob.glob('*.txt')
merged = open('Merged.txt', 'w')
for file in files:
    f = open(file, 'r')
    data = f.read()
    f.close()
    merged.write(f'''\n\n===============================================================================================================
{file}\n\n{data}\n\n==============================================================================================================''')

merged.close()