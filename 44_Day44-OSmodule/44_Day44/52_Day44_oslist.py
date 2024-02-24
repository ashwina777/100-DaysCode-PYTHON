import os
path = r"C:\Users\Amit rana\Documents\Data Science\python 100 days of code\44_Day44-OSmodule\data" 
folders=os.listdir(path)
print(folders)
for folder in folders:
    print(f"Folder : {folder}")
    print(f"file in {folder} : {(os.listdir(os.path.join(path,folder)))}")
print(os.getcwd())