class Solution(object):
    def gcdOfStrings(self, str1, str2):
        s1=str1
        s2=str2
        a=""
        def gcd(a,b):
            if b==0:
                return a
            else:
                return gcd(b,a%b)

        if s1+s2!=s2+s1:
            return ""
        else:
            l1=len(s1)
            l2=len(s2)
            b=gcd(l1,l2)
            if l1>l2:
                for i in range(b):
                    a=a+s2[i]
            else:
                for i in range(b):
                    a=a+s1[i]
            return a




        
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        
#  old
s1="aba"
s2="abaaba"

# if a+b==b+a:
#     print("base")
# else: print("Nah")

# s1=str1
# s2=str2
a=""
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

if s1+s2!=s2+s1:
    print("")
else:
    l1=len(s1)
    l2=len(s2)
    b=gcd(l1,l2)

    if l1>l2:
        for i in range(b):
            # a.append(s2[i])
            a=a+s2[i]
    else:
        for i in range(b):
            # a.append(s1[i])
            a=a+s1[i]

print(a)