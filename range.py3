def CreateList(l,rangeofl):
    for i in range(rangeofl):
        temp=int(input("enter the elements"))
        l.append(temp)
    return l
l1=[]
l2=[]
l3=[]
rangeofl1=int(input("enter first list"))
rangeofl2=int(input("enter second list"))
rangeofl3=int(input("enter third list"))
l1=CreateList(l1,rangeofl1)
print(l1)
l2=CreateList(l2,rangeofl2)
print(l2)
l3=CreateList(l3,rangeofl2)
print(l3)
