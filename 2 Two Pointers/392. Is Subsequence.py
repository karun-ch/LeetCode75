class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        i=0
        j=0
        
        while i<len(s) and j < len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)


        # i=0
        # for c in t:
        #     if s[i]==c:
        #         i+=1
        #         if i==len(s):
        #             return True
        # return False
