# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
# exceptions handling in python

# names = ["salim", "salman", "sadiq"]
# try:
#     print(names[4])
# except Exception as error:
#     print("The error is : ", error)

#     # We can also catch the above error like below:
# try:
#     print(names[4])

# except IndexError as indexEr:
#     print("The error is : ", indexEr)

# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
# Difference b/w try/except/finally vs try/except/else block.
# try:
#     a = 10
#     print(a)
# except NameError:
#     print("You have name error")
# else:
#     print("Else ==> block will execute only when try block execute successfully.")
# finally:
#     print("Finally ==> block will execute whether try block execute or not.")

# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
# Raise user defined exceptions.
# try:
#     age = int(input("Enter age: "))
#     assert age == 30
#     print("Age is valid")

# except AssertionError:
#     print("Assertion get failed because age is not equal to 30.")

# except ValueError:
#     print("You have put the wrong type of value.")
