def printt(a):
    for i in a:
        for j in i:
            if(j!=0):print(j,end=" ")
            else:print(" ",end=" ")
        print()
    print()

def h(a):
    s=0
    b=[[1,1],[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0]]
    for i in range(3):
        for j in range(3):
            s+=abs(b[a[i][j]][0]-i)+abs(b[a[i][j]][1]-j)
    return s;

a=[[0,0,0],[0,0,0],[0,0,0]]
print("enter your matrix")
for i in range(3):
    a[i]=list(map(int,input().split()))
print()
for i in range(3):
    for j in range(3):
        if(a[i][j]==0): i1,j1=i,j
i2,j2=i1,j1
while(1):
        s=[-1,-1,-1,-1]
        min=10000;
        if(i1+1!=i2 and i1<2):
            a[i1+1][j1],a[i1][j1]=a[i1][j1],a[i1+1][j1]
            s[0]=h(a)
            a[i1][j1],a[i1+1][j1]=a[i1+1][j1],a[i1][j1]
        if(i1-1!=i2 and i1>0):
            a[i1-1][j1],a[i1][j1]=a[i1][j1],a[i1-1][j1]
            s[1]=h(a)
            a[i1][j1],a[i1-1][j1]=a[i1-1][j1],a[i1][j1]
        if(j1+1!=j2 and j1<2):
            a[i1][j1+1],a[i1][j1]=a[i1][j1],a[i1][j1+1]
            s[2]=h(a)
            a[i1][j1],a[i1][j1+1]=a[i1][j1+1],a[i1][j1]
        if(j1-1!=j2 and j1>0):
            a[i1][j1-1],a[i1][j1]=a[i1][j1],a[i1][j1-1]
            s[3]=h(a)
            a[i1][j1],a[i1][j1-1]=a[i1][j1-1],a[i1][j1]
        for i in range(4):
            if(s[i]<min and s[i]!=-1):
                min=s[i]
                j=i
        b=[[1,0],[-1,0],[0,1],[0,-1]]
        x=h(a)
        a[i1+b[j][0]][j1+b[j][1]],a[i1][j1]=a[i1][j1],a[i1+b[j][0]][j1+b[j][1]]
        if(h(a)>=x):break
        else:printt(a)
        i2,j2=i1,j1
        i1,j1=i1+b[j][0],j1+b[j][1]
