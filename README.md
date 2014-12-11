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
* Install package using pip installer:
```
pip install dist/mbed-lmtools-0.1.2.zip
```

Now in your command line you should have a command **lm** which should allow you to list all connected mbeds.
