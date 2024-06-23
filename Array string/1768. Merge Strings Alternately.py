

w1="abcd"
w2="pqrstu"

# a1=[]
# a2=[]

s=""
l1=len(w1)
l2=len(w2)

print(l1,l2)


while l1>0 and l2>0:
    i=0
    s=s+w1[i]
    w1=w1[1:]
    s+=w2[i]
    w2=w2[1:]
    l1-=1
    l2-=1

if l1==0:
    for i in w2:
        s+=i
elif l2==0:
    for i in w1:
        s+=i 
    
print(s)
# print(''.join(s))
















# # way 1
# w1="abcdef"
# w2="pqrj"

# a1=[]
# a2=[]

# s=[]

# for i in w1:
#     a1.append(i)
# for i in w2:
#     a2.append(i)
    
# print(a1,a2)

# l1=len(a1)
# l2=len(a2)

# print(l1,l2)


# while l1>0 and l2>0:
#     i=0
#     s.append(a1[i])
#     a1.pop(i)
#     s.append(a2[i])
#     a2.pop(i)
#     l1-=1
#     l2-=1

# if l1==0:
#     for i in a2:
#         s.append(i)
# elif l2==0:
#     for i in a1:
#         s.append(i) 
    
# print(s)
# print(''.join(s))