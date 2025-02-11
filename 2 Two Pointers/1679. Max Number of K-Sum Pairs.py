import collections
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        op=0
        l=0
        r=len(nums)-1

        while l<r:
            if nums[l]+nums[r] == k:
                op+=1
                l+=1
                r-=1
            elif nums[l]+nums[r] < k:
                l+=1
            else: r-=1

        return op


# /////////////////////////////

# class Solution:
#   def maxOperations(self, nums: list[int], k: int) -> int:
#     count = collections.Counter(nums)
#     return sum(min(count[num], count[k - num])
#                for num in count) // 2