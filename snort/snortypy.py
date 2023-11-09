import subprocess
import os


key_cmd = 'mv /etc/apt/sources.list /etc/apt/sources.list.bak'

try:
    subprocess.run(key_cmd, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("New file created ", e)



rm_up = 'find /var/lib/apt/lists -type f -exec rm {} \; '

try:
    subprocess.run(rm_up, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("Recent update removed ", e)


dwnld_key = 'wget https://gist.githubusercontent.com/ishad0w/788555191c7037e249a439542c53e170/raw/3822ba49241e6fd851ca1c1cbcc4d7e87382f484/sources.list -O /etc/apt/sources.list'

try:
    subprocess.run(dwnld_key, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(" Keys Downloaded Succefully ")


key_setup = """sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 871920D1991BC93C"""

try:
    subprocess.run(key_setup, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("Key installing failed ")

up = "sudo apt update"
try:
    subprocess.run(up, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("Error executing update ",e)

snort = "sudo apt-get install snort -y"

try:
    subprocess.run(snort, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print("Error installing snort:", e)

