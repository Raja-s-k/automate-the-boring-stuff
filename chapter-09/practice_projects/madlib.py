a=open("sample.txt","r")
b=a.read()
b=b.split()
c,d,f,g=[],[],[],[]

for i in b:
    if i in ["ADJECTIVE","NOUN","ADVERB","VERB","ADJECTIVE.","NOUN.","ADVERB.","VERB."] :
        print("Enter an ",i)
        h=input()
        if i in ["ADJECTIVE","ADJECTIVE."]:
            c.append(h)
        elif i in ["NOUN","NOUN."]:
            d.append(h)
        elif i in ["ADVERB","ADVERB."]:
            f.append(h)
        elif i in ["VERB","VERB."]:
            g.append(h)
        else:
            pass
a.flush()
a.close()

a=open("sample.txt","w")
j=""

for i in b:
    if i not in ["ADJECTIVE","NOUN","ADVERB","VERB","VERB."] :
        j+=i+" "
    else:
        if i== "ADJECTIVE":
            j+=c[0]+" "
            c.pop(0)
        elif i== "ADJECTIVE.":
            j+=c[0]+"."
            c.pop(0)
        elif i == "NOUN":
            j+=d[0]+" "
            d.pop(0)
        elif i == "NOUN.":
            j+=d[0]+"."
            d.pop(0)
        elif i == "ADVERB":
            j+=f[0]+" "
            f.pop(0)
        elif i == "ADVERB.":
            j+=f[0]+"."
            f.pop(0)
        elif i == "VERB":
            j+=g[0]+" "
            g.pop(0)
        elif i == "VERB.":
            j+=g[0]+"."
            g.pop(0)
        else:
            pass

a.write(j)
a.close()    
        
