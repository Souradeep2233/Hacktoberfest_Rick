l=[]
sum=0
print("PRESS 'X' to stop!")
print("ENTER THE VALUES:")
for i in range(10000):
    q=input()
    l.append(q)
    if(l[i]=='x'):
        break
l.pop(len(l)-1)
for j in range(len(l)):    
    l=list(map(float,l))
    sum+=l[j]    
    avg=sum/(len(l))
print("THE AVERAGE IS:",avg)    
   