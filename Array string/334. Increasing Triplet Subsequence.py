nums = [2,1,5,0,4,6]
nums=[20,100,10,12,5,13]
n=nums
l=len(n)
a=False
for i in range(1,l-1):
    print(i)
    n1=min(n[:i])
    n2=max(n[i+1:])
    print(n1,n[:i],n2,n[i+1:])
    if n1<n[i]and n[i]<n2:
         a=True
print(a)


def increasingTriplet(self, nums):

    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False