import sys
import os
from constructors import MenuItem

menu = []
quit = MenuItem("Quit")

# Import from vendors
# import vendor.VENDORNAME.returnstrings as VENDORIMPORT
import vendor.cisco.returnstrings as CSCreturn
import vendor.juniper.returnstrings as JNPreturn

# Menu item and functions
# VARIABLE = MenuItem('MENU TEXT', {'VENDOR NAME': VENDORIMPORT.FUNCTION.run, 'VENDOR NAME 2': VENDORIMPORT2.FUNCTION.run})
# menu.append(VARIABLE)
