y=input("enter a  string\n")
x=y.lower()
if x[0]==' ':
    print('do not start with a space')
c=x[0]
k=1
j=2
length=len(x)
while j<=length:
    if x[j-1]==' ':
        j=j+1
        continue
    f=0
    while f<=k:
        if c[f]==x[j-1]:
            break
        f=f+1
        if f==k:
            c=c+x[j-1]
            k=k+1
    j=j+1

for l in c:
    count=0
    for m in x:
        if m==l:
            count =count+1
    print(l,':',count)
