from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=set(nums1)
        n2=set(nums2)
        return ([list(n1-n2),list(n2-n1)])
    
    
    
    
# from collections import Counter
# from typing import List

# nums1 = [1,2,3]
# nums2 = [2,4,6]
# # n1,n2 = nums1,nums2
# # n1l=[]
# # n2l=[]
# # for ind,ele in enumerate(n1):
# #     n1
# # arr = [1, 2,5,5, 3, 3,3,3,3,3,3,4,4, 4, 5,5,5,4, 4, 4]

# # c1=Counter(n1)
# # c2=Counter(n2)
# # d1 = dict(c1)
# # d2 = dict(c2)

# # n1u=list(d1.keys())
# # n2u=list(d2.keys())

# n1= set(nums1)
# n2= set(nums2)

# print([list(n1-n2),list(n2-n1)])












# # print(c)
# # print(result)

# # d=Counter(arr)

# # print(d[3])

# # arr = [1, 2,23, 3,5, 4, 55]
# # result = "'" + ''.join(map(str, arr)) + "'"
# # print(result)

# # s=[1,8,9,22,5,4,55]
# # d=[]
# # for i in s:
# #     if str(i) in result:
# #         d.append(i)
# # print(d)