from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=len(height)
        a=0
        l,r = 0, l-1

        while l < r :
            ca = min(height[l],height[r]) * (r-l)
            a=max(a,ca)

            if height[l]<height[r]:
                l+=1
            else: r-=1

        return a


# #  Time Limit Exceeded

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         a=0
#         for i in range(len(height)-1):
#             for j in range(i+1,len(height)):
#                 ca = int(min(int(height[i]),int(height[j]))) * int(abs(i-j))
#                 if ca > a:
#                     a = ca
#         return a