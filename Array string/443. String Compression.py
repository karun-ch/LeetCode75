class Solution(object):
    def compress(self, chars):
        ans = 0
        i = 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            chars[ans] = letter
            ans += 1
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1

        return ans





#  old working
# chars=["a","a","b","b","c","c","c","a"]
chars = ["a","a","b","b","c","c","c"]
# chars = ["a"]
# chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]

c=chars
l=len(c)
cs=["0"]
ns=["0"]
for i in range(l):
    
    p=cs.pop()
    cs.append(p)
    if c[i] not in p:
        cs.append(c[i])

k=0        
while k<l:
    count=1
    while k<l-1 and c[k]==c[k+1] :
        count+=1
        k+=1
    ns.append(count) 
    k+=1
    
cs.pop(0)
ns.pop(0)
print(cs)
print(ns)
ans=[]
a2=[]
for i in range(len(cs)):
    ans.append(cs[i])
    if ns[i]>10:
        for i in str(ns[i]):
            ans.append(i)
    elif ns[i]!=1:
        ans.append(str(ns[i]))
print(str(ans).replace("'",'"'))



# a2=ans.__repr__("'",",")
# print(a2)