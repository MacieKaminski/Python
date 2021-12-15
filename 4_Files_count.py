import os

number_of_files = 0
for path in os.listdir():
    if os.path.isfile(path):
        number_of_files += 1

print("Number of files: ", number_of_files)