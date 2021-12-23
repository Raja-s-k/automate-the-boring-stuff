<pre>

def printTable(Data):
    length=[]
    
    for i in Data:
        a=0
        for j in i:
            if len(j)>a:
                a=len(j)
            else:
                pass
        length.append(a)

    for i in range(4):
        print(Data[0][i].rjust(length[0]),Data[1][i].rjust(length[1]),Data[2][i].rjust(length[2]))

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

</pre>