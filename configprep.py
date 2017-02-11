#!/usr/bin/env python
import os

# directory list
def dirlist(filetype, path):
    if filetype == "file":
        return [os.path.splitext(item)[0]for item in os.listdir(path) if item.endswith(".py") and item != "__init__.py" and os.path.isfile(os.path.join(path, item))]

    elif filetype == "dir":
        return [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]

# __init__.py creator/updater
def initpy(filetype, path):
    # Remove __init__.py if exists
    removeinit = os.path.join(path,"__init__.py")
    if os.path.isfile(removeinit):
        os.remove(removeinit)

    # Create updated __init__.py
    with open(removeinit, "w+") as createinit:
        if os.listdir(path):
            createinit.write("__all__ = {0}".format(dirlist(filetype, path)))
        createinit.close()

# returnstrings.py creator
def returnstrings(path):
    returnstringcheck = os.path.join(path,"returnstrings.py")
    fileheader = "import sys\nimport os\nsys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','..'))\nfrom constructors import UserInput\n\n# List of returns\n # VARIABLE = UserInput('STRING FORMATTING {0} {1} {2}', 'INPUT REQUEST 0', 'INPUT REQUEST 1', 'INPUT REQUEST 2')"

    if not os.path.isfile(returnstringcheck):
        with open(returnstringcheck, "w+") as createinit:
            if os.listdir(path):
                createinit.write(fileheader)
            createinit.close()

# Check if vendor folder exists, if not create directory and exit, otherwise update __init__.py file
vendordir = os.path.join(os.getcwd() ,"vendor")
if not os.path.exists(vendordir):
    os.mkdir(vendordir)
    print "Create necessary configs in vendor folder then rerun 'configprep.py'." + "\n" + "Example: ~/vendor/juniper or ~/vendor/cisco"
    exit
else:
    initpy("dir", vendordir)

# Save files in 'vendor' directory into an array
directories = dirlist("dir", vendordir)

# create __init__.py files in subfolders within vendor
for directory in directories:
    filepath = os.path.join(vendordir,directory)
    initpy("file", filepath)
    returnstrings(filepath)
