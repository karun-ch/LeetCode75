from collections import deque

class Solution:
    def predict_party_victory(self, senate: str) -> str:
        queue_radiant = deque()
        queue_dire = deque()
      
        for index, senator in enumerate(senate):
            if senator == "R":
                queue_radiant.append(index)
            else:
                queue_dire.append(index)
      
        n = len(senate)
      
        while queue_radiant and queue_dire:
            if queue_radiant[0] < queue_dire[0]:
                queue_radiant.append(queue_radiant[0] + n)
            else:
                queue_dire.append(queue_dire[0] + n)
          
            queue_radiant.popleft()
            queue_dire.popleft()
      
        return "Radiant" if queue_radiant else "Dire"