st = "3[a]2[bc]"
class Solution:
  def decodeString(self, s: str) -> str:
    stack = []  # (prevStr, repeatCount)
    currStr = ''
    currNum = 0

    for c in s:
      if c.isdigit():
        currNum = currNum * 10 + int(c)
      else:
        if c == '[':
          stack.append((currStr, currNum))
          currStr = ''
          currNum = 0
        elif c == ']':
          prevStr, num = stack.pop()
          currStr = prevStr + num * currStr
        else:
          currStr += c

    return currStr









# s=[]
# s.append(st[0])

# print(s)

# fs=""

# for c in  st:
#     if c!='[':
#         s.append(c)
#     if c=='[':
        