import os
import re 

entries_folders = os.scandir(r"C:\Users\azama\Desktop\pp2-assignments\Prac06")

for entry in entries_folders:
    print('Name:', entry.name)
    print('Full path:', entry.path)
    print('Is file:', entry.is_file())
    print('Is folder:', entry.is_dir())
    print('-----------------')

entries_files1 = os.scandir(r"C:\Users\azama\Desktop\pp2-assignments\Prac06\file_handling")

for entry in entries_files1:
    print('Name:', entry.name)
    print('Full path:', entry.path)
    print('Is file:', entry.is_file())
    print('Is folder:', entry.is_dir())
    print('-----------------')

entries_files2 = os.scandir(r"C:\Users\azama\Desktop\pp2-assignments\Prac06\file_handling")

for entry in entries_files2:
    if entry.is_file() and re.match(r".*\.py$", entry.name):
        print('Python file found:', entry.name)