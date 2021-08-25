import copy


def printt(a):
    for i in a:
        for j in i:
            if (j != 0):
                print(j, end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
k=[0,0];
def mojaverha(q,i1,j1,i2,j2,a,d,z):
    e=[];global k
    if (i1 + 1 != i2 and i1 < 2):
        a[i1 + 1][j1], a[i1][j1] = a[i1][j1], a[i1 + 1][j1]
        if (a not in d): e.append([copy.deepcopy(a), h(a,z) + k[q] + 1, k[q] + 1, i1 + 1, j1, i1, j1])
        a[i1][j1], a[i1 + 1][j1] = a[i1 + 1][j1], a[i1][j1]
    if (i1 - 1 != i2 and i1 > 0):
        a[i1 - 1][j1], a[i1][j1] = a[i1][j1], a[i1 - 1][j1]
        if (a not in d): e.append([copy.deepcopy(a), h(a,z) + k[q] + 1, k[q] + 1, i1 - 1, j1, i1, j1])
        a[i1][j1], a[i1 - 1][j1] = a[i1 - 1][j1], a[i1][j1]
    if (j1 + 1 != j2 and j1 < 2):
        a[i1][j1 + 1], a[i1][j1] = a[i1][j1], a[i1][j1 + 1]
        if (a not in d): e.append([copy.deepcopy(a), h(a,z) + k[q] + 1, k [q]+ 1, i1, j1 + 1, i1, j1])
        a[i1][j1], a[i1][j1 + 1] = a[i1][j1 + 1], a[i1][j1]
    if (j1 - 1 != j2 and j1 > 0):
        a[i1][j1 - 1], a[i1][j1] = a[i1][j1], a[i1][j1 - 1]
        if (a not in d): e.append([copy.deepcopy(a), h(a,z) + k[q] + 1, k[q] + 1, i1, j1 - 1, i1, j1])
        a[i1][j1], a[i1][j1 - 1] = a[i1][j1 - 1], a[i1][j1]
    return e
p=[0,0]
def bound(c,e,k):
    min = 1000000;
    for i in e:
        present = False
        for j in c:
            if (i[0] == j[0]):
                present = True
                if (i[2] < j[2]):
                    j[2] = i[2]
                    j[1] = i[1];
        if (not present):
            c.append(i)
            p[k]+= 1;
    j1=0
    for i in range(p[k]):
        if (c[i][1] < min):
            min = c[i][1]
            j1 = i
    return j1
def h(a,b):
    s = 0
    for i in range(3):
        for j in range(3):
            s += abs(b[a[i][j]][0] - i) + abs(b[a[i][j]][1] - j)
    return s

a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
b = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
print("enter your matrix")
for i in range(3):
    a[i] = list(map(int, input().split()))
print()
for i in range(3):
    for j in range(3):
        if (a[i][j] == 0):
            i3, j3 = i, j
            break
i1=[i3,1];j1=[j3,1];i2=[i3,1];j2=[j3,1]
c = [[],[]];
d = [[],[]]
f=[[],[]]
a1=[[1,1],[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0]]
b1=[[1,1],[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0]]
for i in range(3):
    for j in range(3):
        b1[a[i][j]][0]=i
        b1[a[i][j]][1]=j
j=[0,0]
while (1):
    e=[]
    e.append(mojaverha(0,i1[0],j1[0],i2[0],j2[0],a,d,a1))
    e.append(mojaverha(1,i1[1],j1[1],i2[1],j2[1],b,d,b1))
    j[0]=bound(c[0],e[0],0)
    j[1]=bound(c[1],e[1],1)
    a = copy.deepcopy(c[0][j[0]][0]);
    b = copy.deepcopy(c[1][j[1]][0]);
    for i in range(2):
        i1[i] = c[i][j[i]][3];j1[i] = c[i][j[i]][4];i2[i] = c[i][j[i]][5];j2[i] = c[i][j[i]][6];k[i] = c[i][j[i]][2]
    d[0].append(copy.deepcopy(c[0][j[0]][0]))
    f[0].append(k[0])
    d[1].append(copy.deepcopy(c[1][j[1]][0]))
    f[1].append(k[1])
    del(c[0][j[0]])
    del(c[1][j[1]])
    p[0]-=1
    p[1]-=1
    t=False
    for i in range(p[0]):
        if(c[0][i][0] in d[1] or c[0][i][0] in c[1]):
            a=c[0][i][0]
            for o in range(p[1]):
                if(a==c[1][o][0]):k[1]=c[1][o][2]
            for o,item in enumerate(d[1]):
                if(item==a):k[1]=f[1][o]
            t=True
            k[0]=c[0][i][2]
            break
    if(not t):
        for i,item in enumerate(d[0]):
            if(d[0][i] in d[1] or d[0][i] in c[1]):
                k[0]=f[0][i]
                a=d[0][i]
                t=True
                for o in range(p[1]):
                    if(a==c[1][o][0]):k[1]=c[1][o][2]
                for o,item in enumerate(d[1]):
                    if(item==a):k[1]=f[1][o]
                break
    if(t):break
printt(a)
print("cost is ",k[0]," + ",k[1])

