<pre>
def list_to_string(list1):
    a=list1
    b=""

    for i in a:
        if i==a[-2]:
            i=str(i)
            b+=i+", and "
        elif i==a[-1]:
            i=str(i)
            b+=i
        else:
            i=str(i)
            b+=i+", "
    return b

c=list(map(str,input().split()))
d=list_to_string(c)
print(d)
</pre>
