import shutil
import os

a = input('Enter the name of Direcory to be sorted ')
list_all_files = os.listdir(a)


for file in list_all_files :
    name,ext= os.path.splitext(file)
    ext = ext[1:]

    if ext == '': continue
    if os.path.exists(a + '/' + ext):
        shutil.move(a + '/' + file, a + '/' + ext + '/' + file)
    else :
        os.makedirs(a + '/' + ext )
        shutil.move(a + '/' + file, a + '/' + ext + '/' + file)
