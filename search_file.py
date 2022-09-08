from genericpath import isdir, isfile
import os
import string


# To search for a file in all the filesystem.

# req_file = input("Enter a file name to search for: ")
# pd_names = string.ascii_uppercase

# drive = []
# for char in pd_names:
#     if os.path.exists(f"{char}:\\"):
#         drive.append(f"{char}:\\")

# for each_drive in drive:
#     for r, d, f in os.walk(each_drive):
#         if d == req_file:
#             print(os.path.join(r, d))

#     print("Not found!!!!")


# 👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺👺

# To search for a file into the download folder.
# search_file = input("Enter the name of the file to search for: ")
# path = "C:\\Users\\User\\Downloads"

# for r, d, f in os.walk(path):
#     for file in f:
#         if file == search_file:
#             print(os.path.join(r, file))

# 😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎😎
# Read a path and check if a path is file or a directory.
# path = input("Enter the path: ")
# if os.path.exists(path):
#     if os.path.isfile(path):
#         print("The given path is a file.")
#     elif os.path.isdir(path):
#         print("The given path is a directory.")
# else:
#     print("The given path doesn't exists.")

# 🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓🍓
# Read a directory path and count the number of file & directories quantity.
# path = "C:\\Users\\User\\Desktop\\Python_Scripting_&_automation"
# no_of_files = 0
# no_of_directories = 0

# for r, d, f in os.walk(path):
#     if f:
#         for i in f:
#             no_of_files += 1
#     if d:
#         for j in d:
#             no_of_directories += 1

# print("No of files this path have ", no_of_files)
# print("No of folders this path have ", no_of_directories)

# 🍟🍟🍟🍟🍟🍟 We can do the above using the following scripts as well.
# print("======================================")

# files = os.listdir(path)
# f = 0
# d = 0

# for item in files:
#     full_path = os.path.join(path, item)
#     if os.path.isfile(full_path):
#         f += 1
#     elif os.path.isdir(full_path):
#         d += 1
# print("No of files this path have ", f)
# print("No of folders this path have ", d)


# 🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡
# Unpacking values from tuple
# my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)] # We can unpack nested list as well.
# for v1, v2, v3 in my_list:
#     print(v1, " : ", v2, " : ", v3)

# new_list = [
#     [a for a in range(1, 5)],
#     [b for b in range(11, 15)],
#     [c for c in range(111, 115)],
# ]
# for a, b, c, d in new_list:
#     print(a, b, c, d)
#     print("==============")
#     print("==============")
#     print("==============")


# # 🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡
# import datetime
# import pytz

# req_timezone = pytz.timezone("Asia/Karachi")
# print(datetime.datetime.now(req_timezone))
# # print(dir(datetime.datetime))
# # print(datetime.datetime.utcnow())
# print(datetime.datetime.now().strftime("%Y-%m-%d"))
# print(pytz.common_timezones)


# 🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡
# Find the files which are older than x days from a given path.
from datetime import datetime

path = "C:\\Users\\User\\Desktop\\Python_Scripting_&_automation"

# Function which return the creation time a file and folder.
# def timeCreation(file):
#     """Return the File/Folder creation time."""
#     file_creation_time = os.path.getctime(file)

#     old = datetime.fromtimestamp(file_creation_time).day
#     if old == 6:
#         listing = file.split("\\")
#         print(f"This {listing[-1]} has been removed.")
#         os.remove(file)

#     elif old <= 10:
#         listing = file.split("\\")
#         print(f"This {listing[-1]} is {old} days old.")


# for file in os.listdir(path):
#     item = os.path.join(path, file)
#     if os.path.isfile(item):
#         result = timeCreation(file=item)

# 🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡
# practicing with subprocess module.

# import subprocess

# sp = subprocess.Popen(
#     "dir",
#     shell=True,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     universal_newlines=True,
# )
# status_code = sp.wait()
# print(status_code)

# out, err = sp.communicate()
# print("Output is:", out.splitlines())
# print("Error is:", err)
# subprocess.run("dxdiag")

# 🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡🥡
# Find the python version and print only the version omit everything else.
# import subprocess

# sub_pro = subprocess.Popen(
#     "python --version",
#     shell=True,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     universal_newlines=True,
# )

# return_code = sub_pro.wait()

# # Getting the output of the command
# out, err = sub_pro.communicate()
# if return_code == 0:
#     splited_result = out.split()
#     print(f"Your python version is: {splited_result[1]}")
# else:
#     print("Error is: ", err)

# 🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚🍚
# Getting process ID's of all the process that are running now
# Below the tasklist file has been fetched through the tasklist cmd command.


# processes = {}
# counter = 1

# with open(
#     "C:\\Users\\User\\tasklist.txt",
#     "r",
# ) as file:
#     readingFile = file.read()
#     listing = readingFile.splitlines()
#     for item in listing:
#         nested_list = item.split()
#         if "chrome.exe" in nested_list:
#             processes[f"{counter} {nested_list[0]}"] = nested_list[1]
#             counter += 1

# for process, pid in processes.items():
#     print(process, " : ", pid)

# print("The number of process we have are: ", len(processes))
