<pre>

import random,time

for i in range(10):
    a=random.randint(0,9)
    b=random.randint(0,9)
    print(a,"*",b,":")
    f=g=0
    f=time.time()
    c=int(input())
    d=a*b
    g=time.time()
    if c==d and (g-f)<=8:
        f=g=0
        print("Correct!")
        time.sleep(1)
        if i==9:
            pass
        else:
            print("NEXT QUESTION")
    else:
        f=g=0
        print("U have answered it incorrectly. U will be getting exactly three tries to correct ur answer")
        for i in range(3):
            print(a,"*",b,":")
            f=g=0
            f=time.time()
            c=int(input())
            d=a*b
            g=time.time()
            if c==d and (g-f)<=8:
                f=g=0
                print("Correct!")
                time.sleep(1)
                break
            else:
                f=g=0
                print("Incorrect!")
                pass
        if i==9:
            pass
        else:
            print("NEXT QUESTION")




</pre>