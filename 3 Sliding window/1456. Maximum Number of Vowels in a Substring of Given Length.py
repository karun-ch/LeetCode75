# Optimized Solution: Sliding Window

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = set('aeiou')
        maxv=0
        cv=0
        
        # Count vowels in the first window
        
        for i in range(k):
            if s[i] in v:
                cv+=1
        maxv = cv

        # Slide the window
        for i in range (k, len(s)):
            
            # Remove the leftmost character of the previous window
            if s[i-k] in v:
                cv-=1
            # Add the new character to the current window
            if s[i] in v:
                cv+=1
            # Update max_vowels
            maxv = max(maxv,cv)
        return maxv
            














# Time Limit Exceeded

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=len(s)
        vc=0
        for i in range(l-k+1):
            ss=s[i:i+k]
            vcss=0
            # print(ss)
            for i in ss :
                if i in 'aeiou':
                    vcss+=1
            vc = max(vc,vcss)
        return vc

