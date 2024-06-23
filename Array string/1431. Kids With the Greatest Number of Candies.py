c=[2,3,5,1,3]
# c=[12,1,12]
# c=[4,2,1,1,2]
e=3
n=len(c)
r=[]
def g(i,c):
    d=0
    for j in c:
        if c[i]<j:
            d+=1
    if d==0:
        return True
    else: return False
    
    # return 0

for i in range(n):
    c[i]+=e
    print("1:",c)
    res=g(i,c)
    c[i]-=e
    print(c)
    r.append(res)
    print(r)

print()
print(r)