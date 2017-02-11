import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__),"..",".."))
from constructors import UserInput

# List of returns
interface = UserInput("set interfaces {0} unit {1} family inet address {2}", "Interface name: ", "Unit ID: ", "IPv4 Address: ")
vlanid = UserInput("set vlans {0} vlan-id {1}", "VLAN Name: ", "VLAN ID: ")
vlantoint = UserInput("set interfaces {0} unit {1} family ethernet-switching vlan memebers {2}", "Interface name: ", "Unit ID: ", "VLAN Name")
