#!/usr/bin/env python
import subprocess
import os
mypass= input("enter root password : ")
command = "python snort/snortypy.py"
os.popen("sudo -S %s"%(command), 'w').write(mypass)

