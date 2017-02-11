import sys
import os
import vendor.cisco.returnstrings as CSCreturn
import vendor.juniper.returnstrings as JNPreturn
from constructors import MenuItem
from vendor import __all__ as vendors

menu = []
quit = MenuItem("Quit")

# Menu item and functions
# VARIABLE = MenuItem('MENU TEXT', {'VENDOR NAME': VENDORIMPORT.FUNCTION.run, 'VENDOR NAME 2': VENDORIMPORT2.FUNCTION.run})
# menu.append(VARIABLE)
interface = MenuItem("Assign IPv4 address to interface", {'juniper':JNPreturn.interface.run, 'cisco':CSCreturn.interface.run})
menu.append(interface)
vlanid = MenuItem("Create VLAN", {'juniper':JNPreturn.vlanid.run, 'cisco':CSCreturn.interface.run})
menu.append(vlanid)
vlantoint = MenuItem("Assign VLAN to interface", {'juniper':JNPreturn.vlantoint.run, 'cisco':CSCreturn.interface.run})
menu.append(vlantoint)