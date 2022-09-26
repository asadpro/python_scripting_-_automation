from ctypes import sizeof
import shutil
import os
import re


# 🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩
# cwd = os.getcwd()
# path = cwd + "\\temp_folder\\"
# # This will check whether the folder if not then create one.
# if not os.path.exists(path):
#     os.mkdir(path)
# try:
#     src_name = input("Enter the source filename: ")
#     import re

#     name_pat = "[a-zA-Z]*.py"
#     name_object = re.search(name_pat, src_name, re.IGNORECASE | re.MULTILINE)
#     src = path + name_object.group()
#     # create a file at specified path.
#     with open(src, "w") as file_object:
#         pass
#     print(os.listdir(path))
# except AttributeError:
#     print("Please insert only .py extension files.")
# print(path)

# 🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩🥩
# list out all the operation related to copying

# shutil_operations = dir(shutil)

# copy_operation = []

# pat = "^co"
# for op in shutil_operations:
#     if re.match(pat, op):
#         copy_operation.append(op)
# print(copy_operation)

# 🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞🥞
# 🧃🧃🧃🧃🧃🧃 copying operations 🧃🧃🧃🧃🧃🧃
# ['collections', 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree']

# copyfile
src = r"C:\Users\User\Desktop\Python_Scripting_&_automation\temp_folder\asad.py"
dst = r"C:\Users\User\Desktop\Python_Scripting_&_automation\temp_folder\asad_backup.py"

# Using copyfile function the permission of the file would be the default permission and no permission would be copied to newly created file.
# result = shutil.copyfile(src, dst)

# Copy function will take the permission of the old file as it is to the newly created file.
# result = shutil.copy(src, dst)

# Copy2 function will take all the meta data from the src file to the distination file.
# result = shutil.copy2(src, dst)

# Copymode will only copies the mode of the file without copying the content of that file into other file.
# result = shutil.copymode(src, dst)

# copyfileobj is used to copy one file object to another fileobject e.g.
# f1 = open('asad.txt','r')
# f2 = open('sadiq.txt','w')
# result = shutil.copyfileobj(f1,f2)

# copytree command will copy all the file into the source file to the distination file
source = r"C:\Users\User\Desktop\Python_Scripting_&_automation"
distination = r"C:\Users\User\Desktop\Python_Scripting_&_automation\temp_folder\delete"


# shutil.copytree(source, distination)
