<pre>

mport pyinputplus as pyip

a=pyip.inputMenu(["wheat","white","sourdough"])
b=pyip.inputMenu(["chicken","turkey","ham","tofu"])
c=pyip.inputYesNo(prompt="Do u want cheese:")

if c == "yes":
    d=pyip.inputMenu(["cheddar","Swiss","mozzarella"])
else:
    d=0

f=pyip.inputYesNo(prompt="Do u want mayo, mustard, lettuce, or tomato:")
g=pyip.inputInt(prompt="How many sandwitch do they want:",min=1)

h={"wheat":10,"white":12,"sourdough":14,"chicken":20,"turkey":22,"ham":18,"tofu":24,
   "cheddar":24,"Swiss":26,"mozzarella":30}

j=0
for i in [a,b,d,f]:
    if i==0:
        j+=0
    elif i=="yes":
        j+=20
    else:
        j+=h[i]

print("Total cost:",j*g)

</pre>