# Copy the content of a source file to a destination file.
source_file = "C:\\Users\\User\\Desktop\\Python Crash Course A Hands-On, Project-Based Introduction to Programming, 2nd Edition\\responses.txt"

with open(source_file, "r") as file_read:
    dest_file = file_read.readlines()
    # Here we have append the content of the above file to the next new created file.
    with open("destination.txt", "w") as file_write:
        # Below line will remove all \n from the end of the line.
        while "\n" in dest_file:
            dest_file.remove("\n")
        for item in dest_file:
            file_write.write(item)

# To read the content of the file that we just created.
with open("destination.txt", "r") as file:
    content = file.read()
    print(content, end="")
