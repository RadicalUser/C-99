import shutil
import os

path = '/Users/username5629/Desktop/C-99'

print("Before copying files")
print(os.listdir(path))


showSequel = '/Users/username5629/Desktop/C-99/main.py'
destination = '/Users/username5629/Desktop/C-99/test1.txt'

dest = shutil.move(showSequel, destination)

print("After copying files")
print(os.listdir(path))


