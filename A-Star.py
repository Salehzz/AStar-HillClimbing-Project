import copy
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
    return s

def Astar(a,i1,j1,i2,j2,k):
    c=[];p=0;d=[]
    while(h(a)!=0):
        e=[];
        min=1000000;
        if(i1+1!=i2 and i1<2):
            a[i1+1][j1],a[i1][j1]=a[i1][j1],a[i1+1][j1]
            if(a not in d):e.append([copy.deepcopy(a),h(a)+k+1,k+1,i1+1,j1,i1,j1])
            a[i1][j1],a[i1+1][j1]=a[i1+1][j1],a[i1][j1]
        if(i1-1!=i2 and i1>0):
            a[i1-1][j1],a[i1][j1]=a[i1][j1],a[i1-1][j1]
            if(a not in d):e.append([copy.deepcopy(a),h(a)+k+1,k+1,i1-1,j1,i1,j1])
            a[i1][j1],a[i1-1][j1]=a[i1-1][j1],a[i1][j1]
        if(j1+1!=j2 and j1<2):
            a[i1][j1+1],a[i1][j1]=a[i1][j1],a[i1][j1+1]
            if(a not in d):e.append([copy.deepcopy(a),h(a)+k+1,k+1,i1,j1+1,i1,j1])
            a[i1][j1],a[i1][j1+1]=a[i1][j1+1],a[i1][j1]
        if(j1-1!=j2 and j1>0):
            a[i1][j1-1],a[i1][j1]=a[i1][j1],a[i1][j1-1]
            if(a not in d):e.append([copy.deepcopy(a),h(a)+k+1,k+1,i1,j1-1,i1,j1])
            a[i1][j1],a[i1][j1-1]=a[i1][j1-1],a[i1][j1]
        for i in e:
            present=False
            for j in c:
                if(i[0]==j[0]):
                    present=True
                    if(i[2]<j[2]):
                        j[2]=i[2]
                        j[1]=i[1];
            if(not present):
                c.append(i)
                p+=1
        for i in range(p):
            if(c[i][1]<min):
                min=c[i][1]
                j=i
        #print(j)
        #print(p)
        a=copy.deepcopy(c[j][0]);i1=c[j][3];j1=c[j][4];i2=c[j][5];j2=c[j][6];k=c[j][2]
        printt(a)
        d.append(copy.deepcopy(c[j][0]))
        del(c[j]);p-=1
    else:
        printt(a)
        print("cost is ",k)
a=[[0,0,0],[0,0,0],[0,0,0]]
print("enter your matrix")
for i in range(3):
    a[i]=list(map(int,input().split()))
print()
for i in range(3):
    for j in range(3):
        if(a[i][j]==0):
            i1,j1=i,j
            break
Astar(a,i1,j1,i1,j1,0)