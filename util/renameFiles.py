import os
import re

folder = r"../wiki"

REGEX = r' \S*(\S*([a-zA-Z]\S*[0-9])|([0-9]\S*[a-zA-Z]))\S*'


def rename(folder):
    for file in os.listdir(folder):
        # Checking if the file is present in the list
        oldName = os.path.join(folder, file)

        if "." not in file:
            newName = re.sub(REGEX, "", file)
            newName = os.path.join(folder, newName)
            os.rename(oldName, newName)
            rename(newName)
        else:
            if re.search(REGEX, file):
                fileExtension = file.split(".")
                newName = re.sub(REGEX, ".", fileExtension[0])+fileExtension[1]
                newName = os.path.join(folder, newName)
                os.rename(oldName, newName)


rename(folder)
