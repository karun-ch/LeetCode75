from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        ml=0
        zc=0
        k=1

        for r in range(len(nums)):
            if nums[r]==0:
                zc+=1

            while zc>k:
                if nums[l]==0:
                    zc-=1
                l +=1

            ml = max(ml, r-l+1)
        
        return ml-1
        