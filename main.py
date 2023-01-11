import flask,os,urllib.request
import math
import base64
import socket
import urllib.request
import hashlib
from PIL import Image
app=flask.Flask("Vmess Plus Plus Node Core")
app.config["JSON_AS_ASCII"]=False
IP = str(urllib.request.urlopen('https://checkip.amazonaws.com').read())
dz = base64.b64encode(IP.encode("utf-8"))
dz = str(dz)
obj = hashlib.md5()
obj.update(dz.encode("utf-8"))
result=obj.hexdigest()
print(result)
dz = "vmesspp://" + dz + "-" +"5069" + result
print(dz)
"""
@app.errorhandler(500)
def error500(err):
    return {"code":500,"text":"未知错误"}
@app.errorhandler(404)
def error404(err):
    return {"code":404,"text":"找不到页面"}
"""
def encode(text):
    str_len = len(text)
    width = math.ceil(str_len**0.5)
    im = Image.new("RGB", (width, width), 0x0)

    x, y = 0, 0
    for i in text:
        index = ord(i)
        rgb = ( 0,  (index & 0xFF00) >> 8,  index & 0xFF)
        im.putpixel( (x, y),  rgb )
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1
    return im
@app.route("/api/account/<ID>/send",methods=["GET"])
def sendUserMsg(ID): #相信我,发送的是用户信息:
    if(os.path.exists(ID + '.msg')):
        return {"code":5000,"text":"你注册了吗?(意味深"}
    else:
        with open(ID + '.msg',"r") as f:
            msg=f.read()
            decode = msg[-10:]
            data = urllib.request.urlopen(decode)
            with open("decode.py","w") as f:
                f.write(data.read()) #你相信我 我下载的是发送用户信息的页面
            import decode
            with open("overfile.txt","w") as f:
                with open('overfile.txt', encoding="utf-8") as f:
                    all_text = f.read()
                    im = encode(all_text)
                    im.save("{}_layout.bmp".format('.'.join('overfile.txt'.split('.')[:-1])))
            return {"code":2000,"text":"用户头像地址在img","image":"overfile.txt_layout.bmp"}
@app.route("/api/account/<ID>/info",methods=["GET"])
def getAccountInfo(ID): #相信我,返回的是用户信息
    print()
app.run(host="0.0.0.0",port=5069)