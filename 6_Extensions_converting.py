import os

for path in os.listdir():
    if os.path.isfile(path):
        base = os.path.splitext(path)[0]
        extension = os.path.splitext(path)[1]
        if extension == ".jpg":
            os.rename(path, base + ".png")
