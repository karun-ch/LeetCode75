from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls =0
        rs=sum(nums)
        for ind, ele in enumerate(nums):
            rs-=ele
            if ls==rs:
                return ind
            ls+=ele
        return -1