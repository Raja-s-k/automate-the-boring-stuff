<pre>

import os,shutil

a=input("Please enter the path of the folder:")
b=os.listdir(a)

for i in b:
    c=os.path.getsize(i)/1000000
    if c>100:
        print(a+"\\"+i)

</pre>