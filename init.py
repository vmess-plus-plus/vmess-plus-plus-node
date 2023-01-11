import os
import zipfile
import urllib.request
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


