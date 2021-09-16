import os

file_path = "../Lv1"
file_name = os.listdir(file_path)

for name in file_name:
    scr = os.path.join(file_path, name)
    name = name.replace("_", " ")
    dst = os.path.join(file_path, name)
    os.rename(scr, dst)

print(file_name)