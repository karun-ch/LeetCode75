s="hello"
vs=[]
sa=[]

for i in s:
    sa.append(i)
    
for i in range(len(sa)):
    if sa[i] in 'AEIOUaeiou':
        vs.append(sa[i])
if len(vs)>1:
    for i in range(len(sa)):
        if sa[i] in 'AEIOUaeiou':
            sa[i]=vs.pop()

print(''.join(sa))
