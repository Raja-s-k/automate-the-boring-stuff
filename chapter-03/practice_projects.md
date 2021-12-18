<pre>
def collatz(number):
    a=number
    if a%2==0:
        print(a//2)
        return a//2
    elif a%2==1:
        print(3*(number+1))
        return (3*(number+1))
    else:
        pass

b=0

while b!=1:
    try:
        c=int(input())
        b=collatz(int(c))
    except:
        print("Pls provide the integer value")
</pre>