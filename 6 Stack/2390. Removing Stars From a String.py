
class Solution:
    def removeStars(self, s: str) -> str:
        f=[]
        for c in s:
            if c=='*':
                f.pop()
            else:
                f.append(c)
        return ''.join(f)



















# # Convert string to a list using a delimiter
# string = "apple,banana,cherry"
# string ="leet**cod*e"
# # list_with_comma = string.split("*")
# crs=list(string)
# print(crs)

# i=0

# while i<len(crs):
#     if crs[i] =='*':
#         crs.pop(i-1)
#         i-=1
#         crs.pop(i)
#     else: i+=1
    
# print(''.join(crs))










# # Stack implementation using a list
# stack = []

# # Push elements onto the stack
# stack.append(10)
# stack.append(20)
# stack.append(30)

# print("Stack after pushing:", stack)

# # Pop elements from the stack
# print("Popped element:", stack.pop())
# print("Stack after popping:", stack)

# # Peek at the top element
# if stack:
#     print("Top element:", stack[-1])
# else:
#     print("Stack is empty")
