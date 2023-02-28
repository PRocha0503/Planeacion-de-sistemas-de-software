import os
import re

folder = r"Project Documentation"


def rename(folder):
    for file in os.listdir(folder):
        # Checking if the file is present in the list
        fileName = os.path.join(folder, file)

        print(fileName)


rename(folder)
