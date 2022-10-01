import os
import shutle

path=input("enter path of folder")
files=os.listdir(path)
for i in files:
    filename.extension = os.path.splitext(i)
    extension_1=extension[1:]
    folder.path=path+"\\"+extension_1
    if os.path.exists(folder_path):
        shutle.move(path+"\\"+i,path+"\\"+extension_1+"\\"+i)
    else:
        os.makedirs(folder_path)
        shutle.move(path+"\\"+i,path+"\\"+extension_1+"\\"+i)

