from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=nums
        
        
        # Calculate the sum of the first k elements
        
        cs = sum(n[:k])
        avg = cs/k

        # Sliding window to compute sum of next windows
        
        for i in range(k, len(n)):
            cs += n[i] - n[i-k]  # Slide the window
            avg = max(avg, cs/k) # Update the max average
        return avg





# from cmath import inf
# from typing import List

# # ////////// TLE
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         avg = -inf
#         for i in range(len(nums)-k+1):
#             avg = max(sum(nums[i:i+k])/k , avg)
#         return avg