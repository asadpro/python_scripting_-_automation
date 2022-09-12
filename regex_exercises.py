import re

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
# text = "This is python which easy to absol abbylearn and understand python3 isabbb the updated version maybe in future we lower_case upper_case would see the python4 version. abbb"
# pat = "[abd]"
# print(re.findall(pat, text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 2. Write a Python program that matches a string that has an 'a' followed by zero or more b's.
# pat = "a[b]*"
# obj = re.compile(pattern=pat)
# print(obj.findall(text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 3. Write a Python program that matches a string that has an 'a' followed by one or more b's.
# pat = "a[b]+"
# obj = re.compile(pattern=pat)
# print(obj.findall(text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 4. Write a Python program that matches a string that has an 'a' followed by zero or one 'b'
# pat = "a[b]?"
# obj = re.compile(pattern=pat)
# print(obj.findall(text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 5. Write a Python program that matches a string that has an a followed by three 'b'.
# pat = "ab{3}"
# obj = re.compile(pattern=pat)
# print(obj.findall(text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 6. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
# pat = "ab{2,3}"
# obj = re.compile(pat)
# print(obj.findall(text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 7. Write a Python program to find sequences of lowercase letters joined with a underscore.
# pat = "^[a-z]+_[a-z]+$"
# pat = "\w*_\w*"
# obj = re.compile(pat)
# print(obj.findall(text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
# text2 = "Asad Sadiq Salim Salar"
# pat = "[A-Z]+[a-z]+"
# print(re.findall(pat, text2))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
# temp = "alibab adkljlkb sdfaskl asdfkjasa asbabab"
# pat = "a[a-zA-Z0-9]+[b]+"
# print(re.findall(pattern=pat, string=temp))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 10. Write a Python program that matches a word at the beginning of a string.
# sentence = "this is python this is new version of python"
# matching = re.match("this", sentence)
# print("Matching text is: ", matching.group())

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 11. Write a Python program that matches a word at the end of string, with optional punctuation.
# test = "punctuation are playing key role in communication e.g. however."
# pat = "\w+\S*$"
# print(re.search(pat, test).group())

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 12. Write a Python program that matches a word containing 'z'.
# contain_z = "word that contain z like zology zimbabwe uzair"
# pat = "\w*z\w*"
# print(re.findall(pat, contain_z))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
# pat = "\Bz\B"
# print(re.findall(pat, contain_z))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
# contain_z = "Python_Exercises_1"
# pat = "^[a-zA-Z0-9_]*$"
# print(re.findall(pat, contain_z))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 15. Write a Python program where a string will start with a specific number.
# number = "9124 is your roll no but in etea you have 3453423 roll no."
# pat = "^[3-9]\d*"
# print(re.findall(pat, number))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 16. Write a Python program to remove leading zeros from an IP address.
# address = "216.08.094.196"
# pat = "\.[0]*"
# print(re.sub(pat, ".", address))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 17. Write a Python program to check for a number at the end of a string.
# num = "Currently i am working in python3"
# pat = "\d$"
# print(re.findall(pattern=pat, string=num))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 18. Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.
# program = "Exercises number 1, 12, 13, and 345 are important"
# pat = "[0-9]{1,3}"
# for item in re.finditer(pat, program):
#     print(item.group())

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
"""
19. Write a Python program to search some literals strings in a string.
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox', 'dog', 'horse'
"""
# Sample_text = "The quick brown fox jumps over the lazy dog."
# pat = ["fox", "dog", "horse"]
# for pattern in pat:
#     print(re.findall(pattern, Sample_text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 20. Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.
"""
Sample text : 'The quick brown fox jumps over the lazy dog.'
Searched words : 'fox'
"""
# Sample_text = "The quick brown fox jumps over the lazy dog."
# search_object = re.search("fox", Sample_text, re.IGNORECASE)
# match = search_object.group()
# tup = search_object.span()

# print('Found "%s" in "%s" from %d to %d ' % (str(match), Sample_text, tup[0], tup[1]))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
"""
21. Write a Python program to find the substrings within a string.
    Sample text : 'Python exercises, PHP exercises, C# exercises'
    Pattern : 'exercises'     
"""
# Sample_text = "Python exercises, PHP exercises, C# exercises"
# pat = "[exercises]+"
# print(re.findall(pat, Sample_text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 22. Write a Python program to find the occurrence and position of the substrings within a string.
# text = "Python exercises, PHP exercises, C# exercises"
# pattern = "exercises"
# matches = re.finditer(pattern, text)
# for match in matches:
#     print(match.span())

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 23. Write a Python program to replace whitespaces with an underscore and vice versa.
# text = "This is ip_address"
# pat = "\s+"
# print(re.sub(pat, "_", text))
# text = text.replace("_", " ")
# print(text)
# text = text.replace(" ", "_")
# print(text)

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 24. Write a Python program to extract year, month and date from an url.
# url1 = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
# pat = "\d{4}/\d{2}/\d{2}"
# print(re.findall(pat, url1))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 25. Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
# url1 = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
# pat = "\d{4}/\d{2}/\d{2}"
# old_date = re.findall(pat, url1)
# splited_date = re.split("/", old_date[0])
# d, m, y = splited_date[2], splited_date[1], splited_date[0]
# print(url1)
# print(re.sub(pat, f"{d}/{m}/{y}", url1))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 26. Write a Python program to match if two words from a list of words starting with letter 'P'.
# words = "this is Python. we have two version of python Python2 Python3"
# pat = "p\w*"
# print(re.findall(pat, words, re.IGNORECASE))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 27. Write a Python program to separate and print the numbers of a given string.
# separate_string = "this 10 is python split it 45 count the no of string into it."
# # listing = re.split(" ", separate_string)
# listing = re.split("\D+", separate_string)
# print(listing)

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 28. Write a Python program to find all words starting with 'a' or 'e' in a given string.
# words = "My name is asad. we have endof string two version of python Python2 Python3"
# print(re.findall("[a,e]\w+", words))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 29. Write a Python program to separate and print the numbers and their position of a given string.
# text = "The following example creates an ArrayList with a capacity of 50 elements."
# obj = re.finditer("\d{1,}", text)
# for item in obj:
#     print(item.group())
#     print("Index position: {} ".format(item.end()))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 30. Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.
# text = "We are near to GT Road"
# print(re.sub("Road", "Rd", text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 31. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
# text = "Python Exercises, PHP exercises."
# print(re.sub("[\s,\.]", ":", text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 32. Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.
# text = "Python Exercises, PHP exercises."
# print(re.sub("[,.]", ":", text, count=2))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 33. Write a Python program to find all five characters long word in a string.
# text = "The follo example creat an ArrayList withs a capacity of 50 elements."
# pat = "\\b\\w{5}\\b"
# print(re.findall(pat, text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 34. Write a Python program to find all three, four, five characters long words in a string.
# text = "The  four follo example creat an ArrayList withs a capacity of 50 elements."
# pat = "\\b\\w{3,5}\\b"
# print(re.findall(pat, text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 35. Write a Python program to find all words which are at least 4 characters long in a string.
# text = "The quick brown fox jumps over the lazy dog."
# pat = "\\b\\w{4,}\\b"
# print(re.findall(pat, text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 36. Write a python program to convert camel case string to snake case string.
# text = "PythonExercises"
# pat = "(.)([A-Z][a-z]+)"
# print(re.sub(pat, "\\1_\\2", text).lower())

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 37. Write a python program to convert snake case string to camel case string.
# text = "python_exercises"
# list_string = re.split("_", text)
# new_string = ""
# for item in list_string:
#     new_string += item.capitalize()
# print(new_string)

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 38. Write a Python program to extract values between quotation marks of a string.
# text = ' "Python", "PHP", "Java" '
# pat = r'"(.*?)"'
# print(re.findall(pat, text))

# # fullmatch operation of re module. the key difference b/w match and
# # fullmatch match only looking at the beginning of the string while fullmatch looking the whole string
# email = "no-reply@pythontutorial.net"
# pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
# match = re.fullmatch(pattern, email)
# print(match.group())

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 39. Write a Python program to remove multiple spaces in a string.
# text = "Python      Exercises singleSpace"
# pat = "\\s{2,}" #Below is the alternative to this one.
# pat2 = " +"
# print(re.sub(pat2, " ", text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 40. Write a Python program to remove all whitespaces from a string.
# text = "Python      Exercises singleSpace"
# # Both of the below are the alternative to one another.
# print(re.sub("\\s+", "", text))
# print(re.sub(" ", "", text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 41. Write a Python program to remove everything except alphanumeric characters from a string.
# text = "Python_      Exercises singleSpace234 $@#asdfs#$# 🥞🥞🥞fdsfa"
# pat = "[\W_]+"
# print(re.sub(pat, "", text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 42. Write a Python program to find urls in a string.
# text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More https://w3resource.com/python-exercises/re/python-re-exercise-42.php Examples</a>'
# pat = r"http[s]?://[a-zA-Z0-9_$-_@.&+!*\(\),]*\.\w{2,3}"
# print(re.findall(pat, text))
# print(
#     re.findall(
#         "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
#         text,
#     )
# )

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 43. Write a Python program to split a string at uppercase letters.
# text = "Python_Exercises singleSpace234 ASAD This Is Python Version Ff295 deans center"
# pat = "[A-Z][A-Za-z0-9]*"
# print(re.findall(pat, text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 44. Write a Python program to do a case-insensitive string replacement.
# text = "Python_Exercises singleSpace234 ASAD PytHOn This Is Python Version Ff295 pythON deans center"
# compiled = re.compile("python", re.IGNORECASE)
# print(compiled.sub("PYTHON3", text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 45. Write a Python program to split a string with multiple delimiters.
# text = "The quick, brown\nfox jumps*over the lazy dog. Hello"
# pat = r"\;|\,|\*|\n|\."
# print(re.split(pat, text, re.IGNORECASE))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
"""
Write a Python program to remove the parenthesis area in a string.
Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
Expected Output:
example
w3resource
github
stackoverflow
"""
# Sample_data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# for item in Sample_data:
#     print(re.sub(" ?\([^)]+\)", "", item))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 51. Write a Python program to insert spaces between words starting with capital letters.
# text = "PythonExercisesPracticeSolution"
# pat = r"(\w)([A-Z])"
# print(re.sub(pat, r"\1 \2", text))

# 🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭🥭
# 53. Write a Python program to remove lowercase substrings from a given string.
# text = "KDeoALOklOOHserfLoAJSIskdsf"
# pat = "[a-z]"
# print(re.sub(pat, "", text))
