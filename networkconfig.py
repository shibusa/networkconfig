#!/usr/bin/env python
import os
import core
from vendor import __all__ as vendors

# Put quit at the end of the menu, quit if no menu options are updated in core.py
core.menu.append(core.quit)
if len(core.menu) <= 1:
    print "Please update core.py with menu options"
    exit()

# Select Vendor OS
netos = raw_input("Device configuration type ({}): ".format(", ".join(vendors)))
while netos not in vendors:
    print "\nInvalid vendor name."
    netos = raw_input("Device configuration type ({}): ".format(", ".join(vendors)))

# Check if config.cfg exists
if os.path.isfile("config.cfg"):
    select = raw_input("Delete current 'config.cfg' file? ")
    if select.lower() == "yes" or select.lower() == "y":
        os.remove("config.cfg")

# Load core.menu, allow file remain open when regex checks are introduced
while True:
    # Open file
    outputfile = open("config.cfg","a+")
    print "\nAvailable Commands:"
    for itemnum in range(0,len(core.menu)):
        print str(itemnum + 1) + ".", core.menu[itemnum].display
    print ""

    try:
        # Alter human input to array form
        mselect = input("Select [1-{0}]: ".format(len(core.menu))) - 1

        # If last item in menu, exit
        if mselect < 0 or mselect >= len(core.menu):
            print "\nPlease enter corresponding menu number."
        elif core.menu[mselect] == core.menu[-1]:
            # Close file
            outputfile.close()
            exit()
        # Else write outputs to file
        else:
            outputfile.write(core.menu[mselect].func[netos]() + '\n')
    except NameError:
        print "\nPlease enter corresponding menu number."
