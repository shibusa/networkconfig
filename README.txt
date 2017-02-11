DESCRIPTION:
Vendor neutral terminal interface for network device configuration.

REQUIREMENTS:
- Python 2.7.* on local system

SETUP:
1. Run configprep.py to build vendor
2. Create folder of vendor(s) for configuration
3. Re-run configprep to create returnstrings.py file
4. Set up ./vendor/<VENDORNAME>/returnstrings.py with commands in the format of:
VARIABLE = UserInput('STRING FORMATTING {0} {1} {2}', 'INPUT REQUEST 0', 'INPUT REQUEST 1', 'INPUT REQUEST 2')"
5. Set up ./core.py with menu in the format of:
VARIABLE = MenuItem('MENU TEXT', {'VENDOR NAME': VENDORIMPORT.FUNCTION.run, 'VENDOR NAME 2': VENDORIMPORT2.FUNCTION.run})
6. Populate 'menu' variable in ./core.py by using menu.append(menuitem)

STANDARD USE:
1. Run script:
./networkconfig.py
2. Check for outputs in config.cfg
3. SCP config.cfg onto JunOS device or "load set terminal" and copy paste contents of config.cfg
