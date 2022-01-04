<pre>

import os,shutil

a=input("Please enter the path of the folder:")
b=os.listdir(a)
d=["Audio","Pictures","Videos","Python programs","C++ programs","Java programs","Softwares","Text files","PDF files","ZIP files","Documents","Derbian packeges","ISO images","Others"]

for i in d:
    try:
        os.mkdir(a+"\\"+i)
    except:
        continue

for i in b:
    c=i.split('.')
    try:
        if c[1] in ["cda","mid","midi","mp3","mpa","ogg","wav","wma","wpl"]:
            shutil.move(a+"\\"+i,a+"\\"+"Audio")

        elif c[1] in ["3gp","avi","flv","h264","m4v","mkv","mov","mp4","mpg","mpeg","rm","swf","vob","wmv"]:
            shutil.move(a+"\\"+i,a+"\\"+"Videos")

        elif c[1] in ["txt"]:
            shutil.move(a+"\\"+i,a+"\\"+"Text files")

        elif c[1] in ["tif","tiff","bmp","jpeg","jpg","gif","png","eps","raw","cr2","nef","orf","sr2"]:
            shutil.move(a+"\\"+i,a+"\\"+"Pictures")

        elif c[1] in ["pdf"]:
            shutil.move(a+"\\"+i,a+"\\"+"PDF files")

        elif c[1] in ["apk","bat","bin","cgi","pl","com","exe","gadget","msi","wsf","lnk"]:
            shutil.move(a+"\\"+i,a+"\\"+"Softwares")

        elif c[1] in ["py"]:
            shutil.move(a+"\\"+i,a+"\\"+"Python programs")

        elif c[1] in ["cpp","c","h"]:
            shutil.move(a+"\\"+i,a+"\\"+"C++ programs")

        elif c[1] in ["deb","udeb"]:
            shutil.move(a+"\\"+i,a+"\\"+"Derbian packeges")

        elif c[1] in ["jar","class"]:
            shutil.move(a+"\\"+i,a+"\\"+"Java programs")

        elif c[1] in ["zip","zipx"]:
            shutil.move(a+"\\"+i,a+"\\"+"ZIP files")        

        elif c[1] in ["iso"]:
            shutil.move(a+"\\"+i,a+"\\"+"ISO images")

        elif c[1] in ["doc","docx","odt","rtf","tex","wpd"]:
            shutil.move(a+"\\"+i,a+"\\"+"Documents")    

    except:
        shutil.move(a+"\\"+i,a+"\\"+"Others")
        continue


for h in d:
    f=os.listdir(a+"\\"+h) 
    if f==[]:
        os.removedirs(a+"\\"+h)
    else:
        continue
</pre>