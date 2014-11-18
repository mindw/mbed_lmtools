"""
mbed SDK
Copyright (c) 2011-2013 ARM Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from lmtools_base import LmToolsBase

import sys, os, re
if sys.version_info[0]<3:
	from _winreg import *
else:
	from winreg import *


class LmToolsWin7(LmToolsBase):
    """ LmToolsWin7 supports mbed enabled platforms detection across Windows7 OS family
    """
    def __init__(self):
        LmToolsBase.__init__()
        self.os_supported.append('Windows7')


    # Returns [(<mbed_mount_point>, <mbed_id>, <com port>, <board model>), ..]
    # (notice that this function is permissive: adds new elements in-places when and if found)
    def discover_connected_mbeds(defs):
        mbeds=[(m[0], m[1], '', '') for m in get_connected_mbeds()]
        for i in range(len(mbeds)):
            mbed=mbeds[i]
            mnt, id = mbed[0], mbed[1]
            id_prefix=id[0:4]
            if id_prefix in defs:
                board=defs[id_prefix]
                mbeds[i]=(mnt, id, mbeds[i][2], board)
            port=get_mbed_com_port(id)
            if port:
                mbeds[i]=(mnt, id, port, mbeds[i][3])
        return mbeds
    
    
    # (This goes through a whole new loop, but this assures that even if
    #  com is not detected, we still get the rest of info like mount point etc.)
    def get_mbed_com_port(id):
        enum=OpenKey(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Enum')
        usb_devs=OpenKey(enum, 'USB')
    
        # first try to find all devs keys (by id)
        dev_keys=[]
        for VID in iter_keys(usb_devs):
            try:
                dev_keys+=[OpenKey(VID, id)]
            except:
                pass
    
        # then try to get port directly from "Device Parameters"
        for key in dev_keys:
            try:
                param=OpenKey(key, "Device Parameters")
                port=QueryValueEx(param, 'PortName')[0]
                return port
            except:
                pass
    
        # else follow symbolic dev links in registry
        for key in dev_keys:
            try:
                ports=[]
                parent_id=QueryValueEx(key, 'ParentIdPrefix')[0]
                for VID in iter_keys(usb_devs):
                    for dev in iter_keys_as_str(VID):
                        if parent_id in dev:
                            ports+=[get_mbed_com_port(dev)]
                for port in ports:
                    if port:
                        return port
            except:
                pass
    
    
    # Returns [(<mbed_mount_point>, <mbed_id>), ..]
    def get_connected_mbeds():
        return [m for m in get_mbeds() if os.path.exists(m[0])]
    
    
    # Returns [(<mbed_mount_point>, <mbed_id>), ..]
    def get_mbeds():
        mbeds=[]
        for mbed in get_mbed_devices():
            mountpoint=re.match('.*\\\\(.:)$', mbed[0]).group(1)
            # id is a hex string with 10-36 chars
            id=re.search('[0-9A-Fa-f]{10,36}', mbed[1]).group(0)
            mbeds+=[(mountpoint, id)]
        return mbeds
    
    
    
    
    # =============================== Registry ====================================
    
    
    # Iterate over subkeys of a key returning subkey as string
    def iter_keys_as_str(key):
        for i in range(QueryInfoKey(key)[0]):
            yield EnumKey(key, i)


    # Iterate over subkeys of a key
    def iter_keys(key):
        for i in range(QueryInfoKey(key)[0]):
            yield OpenKey(key, EnumKey(key, i))

 
    # Iterate over values of a key
    def iter_vals(key):
        for i in range(QueryInfoKey(key)[1]):
            yield EnumValue(key, i)


    # Get MBED devices (connected or not)
    def get_mbed_devices():
        return [d for d in get_dos_devices() if 'VEN_MBED' in d[1].upper()]


    # Get DOS devices (connected or not)
    def get_dos_devices():
        ddevs=[dev for dev in get_mounted_devices() if 'DosDevices' in dev[0]]
        return [(d[0], regbin2str(d[1])) for d in ddevs]


    # Get all mounted devices (connected or not)
    def get_mounted_devices():
        devs=[]
        mounts=OpenKey(HKEY_LOCAL_MACHINE, 'SYSTEM\MountedDevices')
        for i in range(QueryInfoKey(mounts)[1]):
            devs+=[EnumValue(mounts, i)]
        return devs


    # Decode registry binary to readable string
    def regbin2str(bin):
        string=''
        for i in range(0, len(bin), 2):
            # bin[i] is str in Python2 and int in Python3
            if isinstance(bin[i], int):
                if bin[i]<128:
                    string+=chr(bin[i])
            elif isinstance(bin[i], str):
                string+=bin[i]
            else:
                print('ERROR: Can\'t decode REG_BIN from registry')
                exit(1)
        return string
