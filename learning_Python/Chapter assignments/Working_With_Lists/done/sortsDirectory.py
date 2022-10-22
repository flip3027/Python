import shutil
import os
import re

folder = str(input('What folder would you like to clean'))
path = 'd:\\' + folder + '\\'

list = []
vendorMap = {'zip': '.zip',
             'jpg': '.jpg',
             'pdf': '.pdf',
             'exe': '.exe',
             'html': '.html',
             'txt': '.txt',
             'png': '.png'
             }

files = os.listdir(path)

for f in files:
    for key, value in vendorMap.items():
        if key in f.lower():
            shutil.move(path + f, 'd:\\chromedownloads\\files\\' + key )
        else:
            pass

