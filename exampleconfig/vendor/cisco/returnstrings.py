import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),"..",".."))
from constructors import UserInput

# List of returns
interface = UserInput("interface {0}\nip address {1} {2}\nno shutdown", "Interface name: ", "IPv4 Address: ", "Subnet: ")
vlanid = UserInput("vlan {0}\nname {1}\nno shutdown", "VLAN ID: ", "VLAN Name: ")
vlantoint = UserInput("interface {0}\nswitchport access vlan {1}", "Interface name: ", "VLAN ID: ")
