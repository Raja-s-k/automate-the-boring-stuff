<pre>

import os,shutil

a=input("Please enter the path of the folder:")
b=os.listdir(a)
c=[]

for i in b:
    if i[0:4]=="spam":
        c.append(i)

c.sort()

for i in c:
    if i == c[0]:
        d=i
        shutil.move(a+"\\"+i,a+"\\"+i[0:4]+" " +i[4:])
        pass
    else:
        if int(i[6])!=int(d[6])+1:
            shutil.move(a+"\\"+i,a+"\\"+i[0:4]+" "+i[4:6]+str(int(d[6])+1)+".txt")
        else:
            shutil.move(a+"\\"+i,a+"\\"+i[0:4]+" "+i[4:])
        d=i

</pre>