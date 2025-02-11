from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c1=Counter(arr)
        lic1=list(c1.values())
        s=set(lic1)
        return len(lic1)==len(s)        



# arr = [1,2,2,1,1,1,1,3,3]
# c1=Counter(arr)

# print(c1.values())
# lic1=list(c1.values())
# print(lic1)
# s=set(lic1)
# print(s)
# print(len(lic1),len(s))
