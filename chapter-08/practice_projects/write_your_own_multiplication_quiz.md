<pre>

mport random,time

for i in range(10):
    a=random.randint(0,9)
    b=random.randint(0,9)
    print(a,"*",b,":")
    c=int(input())
    d=a*b
    if c==d:
        print("Correct!")
        time.sleep(1)
        if i==9:
            pass
        else:
            print("NEXT QUESTION")
    else:
        print("U have answered it incorrectly. U will be getting exactly three tries to correct ur answer")
        for i in range(3):
            print(a,"*",b,":")
            c=int(input())
            d=a*b
            if c==d:
                print("Correct!")
                time.sleep(1)
                break
            else:
                print("Incorrect!")
                pass
        if i==9:
            pass
        else:
            print("NEXT QUESTION")

</pre>