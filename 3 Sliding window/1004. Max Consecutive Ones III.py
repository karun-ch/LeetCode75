from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0    # left 
        ml=0    # maximum length of consecutive 1's
        zc=0    # zeros count

        for r in range(len(nums)):
            if nums[r]==0:
                zc+=1

            while zc>k:
                if nums[l]==0:
                    zc-=1
                l +=1

            ml = max(ml, r-l+1)
        
        return ml