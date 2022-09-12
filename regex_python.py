import re

# sentence = """
# In physics, magnitude is defined simply as “distance or quantity.”
# It depicts the absolute or relative direction or size in which an object moves in the sense of motion.
# It is used to express the size or scope of something. In physics, magnitude generally refers to distance or quantity.
# """

# resultant_list = re.findall(string=sentence, pattern="is|It|in")
# isCount = 0
# ItCount = 0
# inCount = 0
# for i in resultant_list:
#     if i == "is":
#         isCount += 1
#     elif i == "It":
#         ItCount += 1
#     if i == "in":
#         inCount += 1
# print(isCount)
# print(ItCount)
# print(inCount)
# print(len(resultant_list) == isCount + ItCount + inCount)

# 🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽
# Look for is in the given sentence
# text = "This is pythonlearn and this it is easy to learnads. learn ASAD 9124 + lastlearnaaa"
# digits = "2342342232432234549234"
# my_pat = "is" #this pattern will pick all the is pattern in the text from words also like "this"
# my_pat = "i[st]"
# my_pat = "[a-c e-i k-l]"  # this expression will look for a-to-c character and e-to-i character and so on.
# my_pat = "[abc]"  # Look for any of the specified character in the set.
# my_pat = "[A-Z0-9]"  # Return any UPPERCASE and 0-9 digits from the string.
# my_pat = "\w"  # Matches any single letter digit and underscore. You will see that this does not return the white spaces so for that we need capital \W
# my_pat = "\W"  # \W is opposite of the \w small one. Returns a match where the string DOES NOT contain any word characters
# my_pat = (
#     "9124\Z"  # Return a match if a specified characters are at the end of the string.
# )
# my_pat = "[^Tip]"  # Exclude charcter from the words that starts with 'Tip' any of the specified characters.
# my_pat = "[+]" # Look for the + sign in the given text.
# my_pat = "[0-5][0-9]"  # this will check all the combinations of these two sets.
# my_pat = "\s" # Look for all the whitespaces
# my_pat = "\S"  # This is the opposite of the lowercase of '\s' and return all the non-white spaces string and words.
# my_pat = "\d"  # Return all the digit from the given text
# my_pat = "\D"  # Opposite of the above and will return all the non digit character including whitespaces and special symbols.
# my_pat = "\AThis"  # Return a string if a specified characters are the beginning of the string.
# my_pat = (
#     "last\Z"  # Return a string if a specified characters are the end of the string.
# )

# print(re.findall(my_pat, text))

# my_pat = "\\blearn\\b"  # Return all the words learn that have space at the beginning and at the end.
# my_pat = "\\blearn\\B"
# my_pat = "this"  # this will return only the 'this' words from the given text so to make it insensitive we need ignore flag e.g. look below
# print(re.findall(my_pat, text, re.IGNORECASE))

# 🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽
# text = """
# this is a string End
# this is second line end
# This is third line end
# this is fourth line enD
# """
# my_pat = "this"  # Now this will look for all the 'this' word whether it capital or small because of the flag.
# print(re.findall(my_pat, text2, re.IGNORECASE))

# my_pat = "end$"
# print(re.findall(my_pat, text2, re.IGNORECASE | re.MULTILINE))

# 🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽
# text = "This is python and there are two major version of python2 and python3 and future version would be python4"
# Search and match operation of re module.
# my_pat = "python\d" # this will look for all the python string which have digit at last.
# my_pat = "python[\d]?"
# print(re.findall(my_pat, text, re.IGNORECASE))

# 🥙🥙🥙🥙 But if you want to search for a single occurence of the python words in the given text then we use search function.
# my_pat = "python"
# match_object = re.search(my_pat, text)
# This will return <re.Match object; span=(8, 14), match='python'> where 8,14 are the position of first and last line
# Otherwise the above line will return None. If nothing returns.
# print("Matched word is: ", match_object.group())
# print("Starting index: ", match_object.start())
# print("Ending index: ", match_object.end() - 1)

# 🥙🥙🥙🥙 Search for pattern in the given string.
# Both search and match are the same but match will look only in the beginning of the string if found return else return None.
# my_pat = "this"
# print(re.match(my_pat, text, re.IGNORECASE | re.MULTILINE))

# 🥙🥙🥙🥙 To look for index group and more info of the matching we use finditer where findall will only return the matching pattern but not it's index etc.
# my_pat = "\\bpython[\d]?"

# finditer_object = re.finditer(my_pat, text)
# for item in finditer_object:
#     print(
#         "The match is: ",
#         item.group(),
#         "\t",
#         "Starting index is: ",
#         item.start(),
#         "\t",
#         "Ending index is: ",
#         item.end(),
#     )


# 🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽
# Working with split, sub and subn operations of re module.
# text = "This is python and there are two major version of python2 and python3 and future version would be python4"
# # # my_pat = " " # split the above text based on the match of whitespace.
# # my_pat = "python[\d]?"
# # # To split the given text into list by occurrence of the match. we use split operation.
# # print(re.split(my_pat, text))
# # 🧇🧇🧇🧇 sub operation
# my_pat = "python"
# # print(re.sub(my_pat, "Dart language ", text))

# # 🧇🧇🧇🧇 The subn operation is the same as substitute but it will return the count parameter as default and will return the result in tuple.
# print(re.subn(my_pat, "Java Programming ", text))

# 🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽🌽
# Compile operation of re module.
text = "This is python and there are two major version of python2 and python3 and future version would be python4"

my_pat = "python"
# print(re.compile(my_pat))
compiled_pattern = re.compile(my_pat)
print("Findall operation ==> ", compiled_pattern.findall(text))
print("Finditer operation ==> ", compiled_pattern.finditer(text))
print("Match operation ==> ", compiled_pattern.match(text))
print("Search operation ==> ", compiled_pattern.search(text))
print("Split operation ==> ", compiled_pattern.split(text))
print("Sub operation ==> ", compiled_pattern.sub("Java", text))
print("Subn operation ==> ", compiled_pattern.subn("Java", text))
