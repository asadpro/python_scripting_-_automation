from audioop import reverse
from ctypes import addressof
from fileinput import filename
import turtle
from wsgiref.simple_server import sys_version


x = "name"
y = "asad"
passion = "Computer programming"

# print("My {} is {}. My passion is {}".format(x,y,passion))

# print(passion.center(50,"*"))

# save = ''

# while type(save) != int:
#     try:
#         save = int(input('Enter a number: '))
#         print(type(save))
#         print(save)

#     except ValueError:
#         print('You have put the wrong format value')

# The following line of code will show the possible operations we can do with y variable
# print(dir(y))


def model():
    return " Hello world "


# print(dir(model()))


# save = model().center(29,"🛺")
# print(save)

# str = 'How are you? '
# print(str.split())

# The below line will remove How from the string if set to null then it will only remove whitespaces from the string.
# print(str.strip("How"))

# print(str.find('?',8 ))

# Print a string in the center of the cmd
# mode command is used to know the column no and line no of prompt.

sen = "Hello I love python because of it's simplicity it have."

# len_sen = len(sen)
# We have 195 column on cmd which means we can type 195 character on the horizontal axis of the cmd prompt.
# remaining_spaces = len_sen - 195
# result = abs(round(remaining_spaces/2))
# print(sen.center(result,"#"))
# print(result)

# print(sen.center(195))


# 🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰🏰

# la = [1,2,3,4,5]

# # Id method will find out the address of la variable and hex method will convert that address to hexadecimal format.
# # print(hex(id(la)))

# list1 = la
# list2 = la.copy()
# # print("Memory address of {} is {} \\\\nMemory address of {} is {} ".format(list1, id(list1),list2 ,id(list2)))

# # Are we can also check it equality using boolean
# print(id(list1) == id(list2)) #Will show False

# print("list1 == la :",id(list1) == id(la)) # will show True because "list1" and "la" both pointing to the space address space on memory.

# 🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩🚩

# printing a string in reverse order.
# def reverse(word):

#     print('Printing forward: ',word)
#     empty_list = []

#     for ch in word:
#         empty_list.append(ch)

#     empty_list.reverse()

#     reverse_list = "".join(empty_list)

#     print('Printing backward: ',reverse_list)

# reverse('asad')
# print('\\\\n')
# reverse('salih hayat')


# store  = help('modules')
# type(store)

# with open('commands.txt''w') as commands:
# commands.write(store)

# 🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍🎍
# getpass will prompt the user for password which will not be shown on screen while typing the password.
# import getpass

# user_name = getpass.getuser()
# user_password = getpass.getpass()

# print("Username : ",user_name)
# print("Password of the user: ",user_password)


# 🎏🎏🎏🎏🎏🎏🎏🎏🎏🎏🎏🎏🎏🎏🎏🎏🎏🎏
"""
We can pass command line arguments to python in command line like "python vim_intro.py Hello world My name is command line argument". ==> Now to capture those words 
we type after vim_intro.py we have to use the sys.argv method.
sys module provide function and variable that let us manipulate the runtime python because that function works strongly with interpreter.
"""

# print('sys is module which is used to manipulate the python execution.')
# import sys

# # Catching argument using sys.argv

# arguments = sys.argv

# string = arguments[1].lower()
# operation = arguments[2]

# if len(arguments) < 3 or len(arguments) > 3:
#     print('You have enter too many arguments to sys module.')
#     sys.exit()

# if operation == 'lower':
#     print(string.lower())

# elif operation == 'upper':
#     print(string.upper())

# elif operation == 'title':
#     print(string.title())

# else:
#     print("You have enter the invalid action. Sorry!!!")


# 🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳🍳
# Decorator in python


# def say(func):
#     def employer():
#         print("Say something about you.")

#     def say_name():
#         print("My name is Guido van Rossum.")

#     def say_nationality():
#         print("I am from Netherlands.")

#     def wrapper():
#         employer()
#         say_name()
#         say_nationality()
#         func()

#     return wrapper


# @say
# def start_interview():
#     print("Real interview Started...")
# start_interview()

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# Python File Input Output: Exercises, Practice
# Write a Python program to read an entire text file
sentence = """
1. Write a Python program to read an entire text file. Go to the editor
Click me to see the sample solution

2. Write a Python program to read first n lines of a file. Go to the editor
Click me to see the sample solution

3. Write a Python program to append text to a file and display the text. Go to the editor
Click me to see the sample solution

4. Write a Python program to read last n lines of a file. Go to the editor
Click me to see the sample solution

"""
# filename = "simple.txt"
# with open(filename, "w+") as file_object:
#     file_object.write(sentence)
# with open(filename, "r") as file_read:
#     reader = file_read.read()
#     print(reader)

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# Write a Python program to read first n lines of a file.

# filename = "simple.txt"

# with open(filename, "r") as file_read:
#     reader = file_read.readlines()
#     for line in reader[0:3]:
#         print(line, end="")

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# Write a Python program to append text to a file and display the text
# with open('simple.txt', "a") as appending:
#     appending.write("This line has been append to the file.")

# with open('simple.txt', "r") as reader:
#     reading = reader.read()
#     print(reading)

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# Write a Python program to read last n lines of a file.

# with open("simple.txt", "r") as reader:
#     reading = reader.readlines()
#     for line in reading[len(reading) : -4 : -1]:
#         print(line)


# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
#  Write a Python program to read a file line by line store it into a variable
# file_to_string = ""
# with open("simple.txt", "r") as reader:
#     reading = reader.readlines()
#     file_to_string = "".join(reading)

# print(file_to_string, type(file_to_string))

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# Write a python program to find the longest words.
# with open("simple.txt", "r") as reader:
#     reading = reader.read().split()
#     longest_words = ""
#     for word in reading:
#         if len(word) > len(longest_words):
#             longest_words = word
#         else:
#             pass
#     print(longest_words)

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# Write a Python program to count the number of lines in a text file.

# with open("simple.txt", "r") as reader:
#     reading = reader.readlines()
#     lines = len(reading)
#     print("We have {} no of lines in this file.".format(lines))

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# Write a Python program to count the frequency of words in a file.

# with open("simple.txt", "r") as file:
#     listLines = file.readlines()
#     listword = []
#     for line in listLines:
#         store = f"{line}".format(line).split()
#         for word in store:
#             listword.append(word)
#     print("This character comes in list: ", listword.count("a"), "times.")

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# Write a Python program to get the file size of a plain file.
# import os

# filesize = sys.getsizeof(
#     "C:\\Users\\User\\Desktop\\Python_Scripting_&_automation\\simple.txt"
# )
# print("Filesize in bytes: ", filesize)
# print("Filesize in Kilo bytes: ", filesize / 1000)
# size = os.stat("C:\\Users\\User\\Desktop\\Python_Scripting_&_automation\\simple.txt")
# print(size.st_size / 1000)

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# Write a Python program to write a list to a file.
# listString = ["Asad", "is", "my", "Nickname."]
# with open("simple.txt", "a+") as list_append:
#     for word in listString:
#         list_append.write("%s " % word)

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# class Car:
#     def __init__(self):

#         self.name = "bugati"
#         self.__password = "pass"

#     @property
#     def getpassword(self):
#         return self.__password

#     def settingPassword(self, newPassword):
#         self.__password = newPassword


# tesla = Car()
# print("Old password is: ", tesla.getpassword)
# tesla.settingPassword(newPassword="passwordChange")
# print("New password is: ", tesla.getpassword)


# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# To see what are the possible operation we can perform on a particular variable etc. We can use dir() function e.g.

# x = ["asadpro", "is", "my", "name"]
# print(dir(x))
# list_to_string = " 😍 ".join(x)
# print(list_to_string)

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# Using strip() function to remove whitespaces and split function to convert string to list.
# sent = " What is getter and setter in Python "
# print(sent)
# new_string = sent.strip(
#     " "
# )  # The below line has removed the leading and trailing spaces of above string.
# print(new_string)

# # The below statement will convert the above string into list format.
# listing = sent.split()
# print(listing)

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
# import fileinput
# import os

# os.chdir("C:\\Users\\User\\Downloads")
# for line in fileinput.fileno(
#     files=("file1.txt", "file2.txt", "file3.txt"), encoding="utf-8"
# ):
#     print(line)

# 🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘🍘
import os

path = os.getcwd()

for r, d, f in os.walk(path):
    print(r, f)
    print("=========================")
    for eachfile in f:
        print(os.path.join(r, eachfile))
