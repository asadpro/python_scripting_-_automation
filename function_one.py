# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
# To check the platform of operating system
# import platform

# print("Name of the operating system: %s" % platform.system())

# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
# Calling a function from another function and scope of the variable.

# Here we have defined x as global variable that's why it's scope is now beyond functions. and can be accessible anywhere in the program.
# def func1():
#     global x
#     x = 97879
#     print("This is function 1")
#     func2()


# def func2():
#     print("This is function 2 and the value of X: ", x)


# func1()

# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
# functions with default values arguments
# def addNumbers(a=3, b=4):
#     return a + b


# res1 = addNumbers()  # This function will pass the default values to the functions.
# res2 = addNumbers(a=53, b=324)  # These are also called keyword/named arguments.
# res3 = addNumbers(239824, 398238)  # These are called positional arguments.

# print("Result of default values: ", res1)
# print("Result of keyword arguments: ", res2)
# print("Result of positional arguments: ", res3)

# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
# functions with variable length arguments.


# def variable_lengthArgs(*data):
#     for item in data:
#         print(item)


# # Pass a list to it.
# variable_lengthArgs(83, 43, 54, 76, 34)
# variable_lengthArgs("asad", "salim", "sadiq", "sahil")

# Using **kwargs means keyword arguments which takes dictionary


# def display_dictionary(Roll_no, **display):
#     for key, value in display[
#         "display"
#     ].items():  # We have take the display Because the display arguments bring nested dictionaries
#         print(key, " : ", value)
#     print("Roll_no variable ====> ", Roll_no)


# profile = {
#     "Name": "Asad",
#     "Father_name": "Habibullah",
#     "Address": "Dalazak road fattu abdurrahima Peshawar",
#     "Email": "saeed.mlops.techy@gmail.com",
# }


# display_dictionary(display=profile, Roll_no=9124)


# 🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟🍟
# pass multiple dictionaries to a function as an argument
# SP = dict({"key1": "value1", "key2": "value2"})
# CP = dict({"key1": "value1", "key2": "value2"})


# def test(SP, **CP):
#     # print(SP.keys(), CP.keys())
#     print("Keys of Dictionary 1: ", SP.keys())
#     print("Keys of Dictionary 2: ", CP.keys())


# test(SP, **CP)


# 🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉🍉
"""
If __name__ == "__main__":
    main()
The above statement is  used when you want to execute a specific code in the main file which refers to the file from where we run our script. Let's take
a look with example by doing it practically.
"""


# def addition(x, y):
#     print("Addition of two numbers is : ", x + y)


# if __name__ == "__main__":
#     addition(3, 4)
