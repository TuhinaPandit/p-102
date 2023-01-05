import os
import shutil
source = r"C:\Users\Tuhina\Desktop\Coding\Python\p-102"
destination = r"C:\Users\Tuhina\Desktop\Coding\Python\p-102\Document_Files"

list_of_files = os.listdir(source)
#print(list_of_files)

for x in list_of_files:
   name, extention = os.path.splitext(x)
   if extention == "":
    continue
   if extention in [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = source + "/" + x
        path2 = destination
        path3 = path2 + "/" + x
        print(path1)
        print(path2)
        print(path3)
        if os.path.exists(path2):
            print("Moving" + x + ".....")
            shutil.move(path1,path3)
        else:
            print("Creating a folder")
            os.mkdir(path2)
            print("Moving" + x + ".....")
            shutil.move(path1,path3)
        