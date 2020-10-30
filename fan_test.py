#!/usr/bin/env python3

import argparse
import os
import sys


from senseme import discover
from senseme import SenseMe
# discover devices, returns list of SenseMe devices
# devices = discover()
# fan = devices[0]
# repr(fan)

fan = SenseMe(ip='192.168.1.123', name="Master Bedroom Fan", mac="20:F8:5E:DB:F9:A3")
repr(fan)
fan.listen(60)
print(fan.json)
print(fan.xml)


