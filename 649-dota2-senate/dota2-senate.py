from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)

        radiant = 0
        dire = 0

        while queue:
            senator = queue.popleft()

            if senator == 'R':
                if dire > 0:
                    dire -= 1
                else:
                    radiant += 1
                    queue.append('R')

            else: 
                if radiant > 0:
                    radiant -= 1
                else:
                    dire += 1
                    queue.append('D')

           
            if all(x == 'R' for x in queue):
                return "Radiant"
            if all(x == 'D' for x in queue):
                return "Dire"

        return "Radiant" if radiant > 0 else "Dire"