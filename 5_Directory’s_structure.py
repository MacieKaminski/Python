import os

for root, dirs, files in os.walk(os.getcwd()):
    print(root, dirs, files)
