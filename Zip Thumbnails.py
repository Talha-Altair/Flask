import os
import zipfile
os.chdir('D:\PROJECTS')
list_files = ['THUMB1.png','THUMB2.png']

with zipfile.ZipFile('final.zip', 'w') as zipF:
    for file in list_files:
        zipF.write(file, compress_type=zipfile.ZIP_DEFLATED)

os.rename("D:\PROJECTS\Final.zip", "D:\PROJECTS\static\Final.zip")        
