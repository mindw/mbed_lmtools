## Description
lmttools are module used to list mbed enabled devices connected to host computer.
Currently lmtools support these OSs:
* Windows 7,
* Ubuntu

### Rationale
When connecting more than one mbed enabled device to host computer it takes time to check platform's binds:
* mounted disk,
* virtual serial port
* target id and platform name.

# Instalation

* Clone this repository to your local machine:
```
git clone <link to this repo>
```
* Go to mbed_lmtools directory
```
cd mbed_lmtools
```
* Create a Python's pip package by calling a command:
```
python setup.py sdist
```
```
running sdist
running egg_info
writing requirements to mbed_lmtools.egg-info\requires.txt
writing mbed_lmtools.egg-info\PKG-INFO
writing top-level names to mbed_lmtools.egg-info\top_level.txt
writing dependency_links to mbed_lmtools.egg-info\dependency_links.txt
writing entry points to mbed_lmtools.egg-info\entry_points.txt
reading manifest file 'mbed_lmtools.egg-info\SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'mbed_lmtools.egg-info\SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt

running check
creating mbed-lmtools-0.1.2
creating mbed-lmtools-0.1.2\lmtools
creating mbed-lmtools-0.1.2\mbed_lmtools.egg-info
copying files to mbed-lmtools-0.1.2...
copying LICENSE -> mbed-lmtools-0.1.2
copying MANIFEST.in -> mbed-lmtools-0.1.2
copying README.md -> mbed-lmtools-0.1.2
copying setup.py -> mbed-lmtools-0.1.2
copying lmtools\__init__.py -> mbed-lmtools-0.1.2\lmtools
copying lmtools\lmtools_base.py -> mbed-lmtools-0.1.2\lmtools
copying lmtools\lmtools_ubuntu.py -> mbed-lmtools-0.1.2\lmtools
copying lmtools\lmtools_win7.py -> mbed-lmtools-0.1.2\lmtools
copying lmtools\main.py -> mbed-lmtools-0.1.2\lmtools
copying mbed_lmtools.egg-info\PKG-INFO -> mbed-lmtools-0.1.2\mbed_lmtools.egg-info
copying mbed_lmtools.egg-info\SOURCES.txt -> mbed-lmtools-0.1.2\mbed_lmtools.egg-info
copying mbed_lmtools.egg-info\dependency_links.txt -> mbed-lmtools-0.1.2\mbed_lmtools.egg-info
copying mbed_lmtools.egg-info\entry_points.txt -> mbed-lmtools-0.1.2\mbed_lmtools.egg-info
copying mbed_lmtools.egg-info\requires.txt -> mbed-lmtools-0.1.2\mbed_lmtools.egg-info
copying mbed_lmtools.egg-info\top_level.txt -> mbed-lmtools-0.1.2\mbed_lmtools.egg-info
Writing mbed-lmtools-0.1.2\setup.cfg
creating 'dist\mbed-lmtools-0.1.2.zip' and adding 'mbed-lmtools-0.1.2' to it
adding 'mbed-lmtools-0.1.2\LICENSE'
adding 'mbed-lmtools-0.1.2\MANIFEST.in'
adding 'mbed-lmtools-0.1.2\PKG-INFO'
adding 'mbed-lmtools-0.1.2\README.md'
adding 'mbed-lmtools-0.1.2\setup.cfg'
adding 'mbed-lmtools-0.1.2\setup.py'
adding 'mbed-lmtools-0.1.2\lmtools\lmtools_base.py'
adding 'mbed-lmtools-0.1.2\lmtools\lmtools_ubuntu.py'
adding 'mbed-lmtools-0.1.2\lmtools\lmtools_win7.py'
adding 'mbed-lmtools-0.1.2\lmtools\main.py'
adding 'mbed-lmtools-0.1.2\lmtools\__init__.py'
adding 'mbed-lmtools-0.1.2\mbed_lmtools.egg-info\dependency_links.txt'
adding 'mbed-lmtools-0.1.2\mbed_lmtools.egg-info\entry_points.txt'
adding 'mbed-lmtools-0.1.2\mbed_lmtools.egg-info\PKG-INFO'
adding 'mbed-lmtools-0.1.2\mbed_lmtools.egg-info\requires.txt'
adding 'mbed-lmtools-0.1.2\mbed_lmtools.egg-info\SOURCES.txt'
adding 'mbed-lmtools-0.1.2\mbed_lmtools.egg-info\top_level.txt'
removing 'mbed-lmtools-0.1.2' (and everything under it)
```
* Install package using pip installer:
```
pip install dist/mbed-lmtools-0.1.2.zip
```
If you have trouble installing or you want to force reinstall please use below command:
```
pip install -U --force-reinstall --no-deps dist\mbed-lmtools-0.1.2.zip
```
You should see similar output:
```
Unpacking c:\work\mbed_lmtools\dist\mbed-lmtools-0.1.2.zip
  Running setup.py (path:c:\users\przwir01\appdata\local\temp\pip-b0lcrc-build\setup.py) egg_info for package from file:///c:/Work/mbed_lmtools/dist/mbed-lmtools-0.1.2.zip

Installing collected packages: mbed-lmtools
  Found existing installation: mbed-lmtools 0.1.2
    Uninstalling mbed-lmtools:
      Successfully uninstalled mbed-lmtools
  Running setup.py install for mbed-lmtools

    Installing lm-script.py script to c:\Python27\Scripts
    Installing lm.exe script to c:\Python27\Scripts
    Installing lm.exe.manifest script to c:\Python27\Scripts
Successfully installed mbed-lmtools
Cleaning up...
```
Now in your command line you should have a command **lm** which should allow you to list all connected mbeds.

You can verify your install by typing:
```
where lm.exe
```
```
C:\Python27\Scripts\lm.exe
```
## Usage examples
### Listing
```
lm
```
Example output:
```
+---------------------+-------------------+-------------------+--------------------------------+
|platform_name        |mount_point        |serial_port        |target_id                       |
+---------------------+-------------------+-------------------+--------------------------------+
|unknown              |F:                 |COM58              |107002161FE6E019E20F0F91        |
|unknown              |G:                 |COM93              |0231020337317E7FCACD83B6        |
+---------------------+-------------------+-------------------+--------------------------------+
```
### Simplified list
```
lm -s
```
```
unknown        F:        COM58        107002161FE6E019E20F0F91
unknown        G:        COM93        0231020337317E7FCACD83B6
```
# lmtools as Python module
Please note that when you install lmtools you get not only command line tools but also siple Python libary used to detect connected mbed enabled devices:
## lmtools API examples
Run Python interpreter from command line:
```
python
```
```
Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import lmtools
>>> from lmtools import lmtools_factory
```
### Printing functionality
```
>>> lm = lmtools_factory()
>>> print lm # use of __str__()
platform_name        mount_point        serial_port        target_id
unknown              F:                 COM58              107002161FE6E019E20F0F91
unknown              G:                 COM93              0231020337317E7FCACD83B6
```
```
>>> s = lm.get_string()
>>> print s
platform_name        mount_point        serial_port        target_id
unknown              F:                 COM58              107002161FE6E019E20F0F91
unknown              G:                 COM93              0231020337317E7FCACD83B6
```
### Access detected devices' descriptors
```
>>> d = lm.list_mbeds()
>>> print d
[{'platform_name': None, 'mount_point': 'F:', 'target_id': '107002161FE6E019E20F0F91', 'serial_port': u'COM58'}, {'platform_name': None, 'mount_point': 'G:', 'target_id': '0231020337317E7FCACD83B6', 'serial_port': u'COM93'}]
```
```
>>> import json
>>> json.dumps(d, indent=4)
'[\n    {\n        "platform_name": null, \n        "mount_point": "F:", \n        "target_id": "107002161FE6E019E20F0F91", \n        "serial_port": "COM58"\n    }, \n    {\n        "platform_name": null, \n        "mount_point": "G:", \n        "target_id": "0231020337317E7FCACD83B6", \n        "serial_port": "COM93"\n    }\n]'
>>> print json.dumps(d, indent=4)
[
    {
        "platform_name": null,
        "mount_point": "F:",
        "target_id": "107002161FE6E019E20F0F91",
        "serial_port": "COM58"
    },
    {
        "platform_name": null,
        "mount_point": "G:",
        "target_id": "0231020337317E7FCACD83B6",
        "serial_port": "COM93"
    }
]
```
