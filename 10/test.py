import os

name_direc='etc1'
name_bin='python'

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)
        print(files)


