l=[]
print("ENTER THE NUMBER OF ELEMENTS:")
k=int(input())
if(k==1):
        l.append(0)
        print(l)
if(k==2):
    l.extend([0,1])
    print(l)            
for i in range (k):
    l[0]=0
    l[1]=1
               
    