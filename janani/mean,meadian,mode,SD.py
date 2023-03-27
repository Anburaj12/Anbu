#Mean
l=[1,2,3,4,5,6]
a=len(l)
sum=sum(l)
c=sum/a
print("mean:",c)


#Meadian
a=[1,3,5,7,8,9,2]
b=len(a)
c=(b+1)/2
print("meadian:",c)

#Mode
a=[2,5,3,8,5]
b=[]
c=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
print("mode:",c)

#standard Deviation
num=[1,2,3,4]
sum=0
for i in num:
    sum = sum + i
    p = len(num)
    mean = sum / p
    var = 0
for i in num:
   c=((i-mean)**2)
   var=var+c
   dev=(var/(p-1))**0.5
print("standard deviation:",dev)

#changes made

