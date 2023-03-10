import os
import re

folder = r"wiki"

REGEX = r' \S*(\S*([a-zA-Z]\S*[0-9])|([0-9]\S*[a-zA-Z]))\S*'

pathsDict = {}
absPathsArr = []


def rename(folder, folderNew):
    for file in os.listdir(folder):
        # Checking if the file is present in the list
        oldName = os.path.join(folder, file)
        if "." not in file:
            newName = re.sub(REGEX, "", file)
            newName = os.path.join(folder, newName)
            rename(oldName, newName)
            os.rename(oldName, newName)
        else:
            if re.search(REGEX, file):
                fileExtension = file.split(".")
                newName1 = re.sub(
                    REGEX, ".", fileExtension[0])+fileExtension[1]
                newName = os.path.join(folder, newName1)
                os.rename(oldName, newName)
                newName = os.path.join(folderNew, newName1)
                oldName = addSpaceCharacter(oldName)
                absPathsArr.append("/"+addSpaceCharacter(newName))
                pathArray = pathPossibilities(oldName)
                for path in pathArray:
                    pathsDict[path] = "/"+addSpaceCharacter(newName)


def addSpaceCharacter(path, spacing="%20"):
    newPath = ""
    for i in path:
        if i == " ":
            newPath += "%20"
        else:
            newPath += i
    return newPath


def pathPossibilities(path):
    pathArray = [path]
    for i in range(len(path)):
        if path[i] == "/":
            pathArray.append(path[i+1:])
    return pathArray


def renamePaths():
    for file in absPathsArr:
        print(file)


def main():
    rename(folder, folder)
    renamePaths()


if __name__ == "__main__":
    main()
