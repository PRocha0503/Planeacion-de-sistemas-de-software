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
            oldName = addSpaceCharacter(oldName)
            pathArray = pathPossibilities(oldName)
            for path in pathArray:
                pathsDict[path] = "/"+addSpaceCharacter(newName)
        else:
            if re.search(REGEX, file):
                fileExtension = file.split(".")
                newName1 = re.sub(
                    REGEX, ".", fileExtension[0])+fileExtension[1]
                newName = os.path.join(folder, newName1)
                os.rename(oldName, newName)
                newName = os.path.join(folderNew, newName1)
                absPathsArr.append(fr"{newName}")
                oldName = addSpaceCharacter(oldName)
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
        # todo search for files in the page and update them
        for key in pathsDict:
            try:
                inplace_change(file, key, pathsDict[key])
            except:
                continue


def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print(
            'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


def main():
    rename(folder, folder)
    renamePaths()
    # wiki/Risk%20analysis.md
    # print(os.listdir())
    # print(os.getcwd())
    # inplace_change(r"wiki/Risk analysis.md", "a", "a")


if __name__ == "__main__":
    main()
