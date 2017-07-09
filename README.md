Vendor neutral network device configuration generator.

## REQUIREMENTS
- Python 2.7.* on local system

## SETUP
1. Make configprep.py executable
```
chmod +x configprep.py
```
2. Run configprep.py to build vendor
```
./configprep.py
```
3. Create folder of vendor(s) for configuration
4. Re-run configprep to create returnstrings.py file
```
./configprep.py
```
4. Set up ./vendor/<VENDORNAME>/returnstrings.py with commands in the format of
```
VARIABLE = UserInput('STRING FORMATTING {0} {1} {2}', 'INPUT REQUEST 0', 'INPUT REQUEST 1', 'INPUT REQUEST 2')"
```
5. Import returnstrings.py into ./core.py
```
import vendor.VENDORNAME.returnstrings as VENDORIMPORT
```
6. Set up ./core.py with menu items in the format of
```
VARIABLE = MenuItem('MENU TEXT', {'VENDOR NAME': VENDORIMPORT.FUNCTION.run, 'VENDOR NAME 2': VENDORIMPORT2.FUNCTION.run})
```
7. Populate 'menu' variable in ./core.py
```
menu.append(menuitem)
```

## USAGE
1. Make networkconfig.py executable
```
chmod +x networkconfig.py
```
2. Run script
```
./networkconfig.py
```
3. Create config
4. Check for outputs in config.cfg
5. SCP config.cfg onto device or copy paste contents of config.cfg
