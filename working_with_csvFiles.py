# from prettytable import PrettyTable, from_csv

# # Importing and reading csv file through prettyTable module we can also read json file and put it into a prettytable object.

# table = PrettyTable()

# with open("survey.csv", "r") as csv_object:
#     table = from_csv(csv_object)

# print(table)

# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋

# import csv

# Now read the csv file using csv build-in python module
# with open("survey.csv", "r") as csv_object:
#     content = csv.reader(csv_object, delimiter=",")
#     for item in content:
#         print(item)

# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
# Now writing to the above csv file.
# Below newline parameter will skip adding the empty line to the files remove for a while and run the example and then go check the csv file.
# with open("survey.csv", "a", newline="") as writer_object:
#     csv_writer = csv.writer(writer_object, delimiter=",")
#     universities = [
#         "city university",
#         "abasyn university",
#         "peshawar university",
#         "alama iqbal university",
#         "sarhad university",
#         "iqra university",
#         "comsat university",
#     ]
#     for i in range(len(universities)):
#         csv_writer.writerow(
#             [
#                 "1999",
#                 "9124",
#                 "Average",
#                 universities[i],
#             ]
#         )

# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
# import csv

# content_list = [
#     ["s_no", "name", "age"],
#     [1, "saeed", 23],
#     [2, "khadim", 33],
#     [3, "sadiq", 19],
# ]

# # Creating a csv file name personal_info.csv and insert some data into it then read it.
# with open("personal_info.csv", "w", newline="") as csv_file_create:
#     write_file = csv.writer(csv_file_create, delimiter=",")
#     write_file.writerows(content_list)

# # Reading the above csv file
# with open("personal_info.csv", "r") as csv_file_read:
#     reading = csv.reader(csv_file_read, delimiter=",")
#     # The below next function will direct the cursor from header to the next line.
#     next(reading)
#     for line in list(reading):
#         print(line)

# 🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋🍋
# Working with json files using json module
# import os
# import json
# import ast


# current_path = os.getcwd()
# path = current_path + "\\jsonfile.json"

# with open(path, "r") as json_reader:
#     content = json.load(json_reader)
#     dictionary = ast.literal_eval(content)

#     for i in range(len(dictionary["results"])):
#         for key, value in dictionary["results"][i].items():
#             print(key, " : ", value)
#         print("=================================")


# writing to the above json file using json dump method.
# dic = {"name": "asad", "fathername": "habib", "age": 23, "address": "dalazak road"}
# with open(
#     "demo.json",
#     "w",
# ) as json_writer:
#     json.dump(dic, json_writer, indent=4)
