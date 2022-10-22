from os.path import abspath, curdir,exists
from os import chdir, remove, rename, mkdir
from shutil import move

chdir("D:\\")
drive= "D:\\"
path= "chromeDownloads\\files\\"
choice = int(input('How many folders do you need?'))

while choice != 0:
    folder = input(str('Enter the name of the folder '))
    full_path = drive + path + folder
    choice = choice - 1
    if exists(full_path):
        print(full_path)
        print('Folder exists')
    else:
        mkdir(full_path)
        if exists(full_path):
            print('The folder is now made')

