import os
import shutil

FD = "C:/Users/ADMIN/Downloads"
TD = "F:/Document_Files"

lof = os.listdir(FD)
# print(lof)

for file_name in lof:

    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)


if extension in ['.txt', '.doc', '.docx', '.pdf']:
    path1 = FD+'/'+file_name
    path2 = TD+'/'+"Document_files"
    path3 = TD+'/'+"Document_Files"+'/'+file_name

if os.path.exists(path2):
    print("Moving"+file_name+".....")
    shutil.move(path1, path3)
    
else:
    os.makedirs(path2)
    print("Moving"+file_name+".....")
    shutil.move(path1, path3)
