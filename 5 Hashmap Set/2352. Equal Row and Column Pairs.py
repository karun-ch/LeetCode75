from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transposed_grid = [list(column) for column in zip(*grid)]      
        equal_pairs_count = 0
        for row in grid:
            for transposed_row in transposed_grid:
                if row == transposed_row:
                    equal_pairs_count += 1
        return equal_pairs_count







# import numpy as np

# grid = [[3,2,1],[1,7,6],[2,7,7]]
# matrix=grid
# # Convert to NumPy array
# matrix_np = np.array(matrix)
# m=matrix_np
# # Transpose
# transpose_np = matrix_np.T
# t=transpose_np

# # print("Original Matrix:")
# # print(matrix_np)
# # print("Transposed Matrix:")
# # print(transpose_np)

# ss=0

# for i in m:
#     for j in t:
#         if i==j:
#             ss+=1
            
# print(ss)