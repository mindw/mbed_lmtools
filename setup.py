"""
This module defines the attributes of the
PyPI package for the mbed SDK test suite
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

DESCRIPTION = "Command line tools used to detect connected mbed enabled devices. See http://mbed.org for details"
OWNER_NAMES = 'Przemyslaw Wirkus, Johan Seferidis'
OWNER_EMAILS = 'Przemyslaw.Wirkus@arm.com, Johan.Seferidis@arm.com'

setup(
    name='mbed-lmtools',
    version='0.1.2',
    description=DESCRIPTION,
    long_description=long_description,
    author=OWNER_NAMES,
    author_email=OWNER_EMAILS,
    maintainer=OWNER_NAMES,
    maintainer_email=OWNER_EMAILS,
    url='https://github.com/mbedmicro/mbed',
    packages=find_packages(),
    include_package_data=True,
    license="Apache-2.0",
    entry_points={
        "console_scripts": [
            "lm=lmtools:main",
        ],
    },
    install_requires=["PrettyTable>=0.7.2"]
)
