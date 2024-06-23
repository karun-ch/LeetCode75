# n=5
# for i in range(n,-1,-1):
#     print(i)



nums = [1,2,3,4]
n=nums
l=len(n)
p=[1]*len(n)
s=[1]*len(n)

for i in range(1,l):
    p[i]=p[i-1]*n[i-1]
for i in range(l-2,-1,-1):
    s[i]=s[i+1]*n[i+1]
    
a=[s[i]*p[i] for i in range(l)]
print(a)



# #  old
# # nums = [1,2,3,4]
# # n=nums
# # a=[]

# # l=len(n)
# # for i in range(l):
# #     c=1
# #     for j in range(l):
# #         if i!=j:
# #             c=c*n[j]
# #     a.append(c)

        