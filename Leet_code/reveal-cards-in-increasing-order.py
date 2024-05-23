from collections import deque
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        queue = deque(range(n))
        res = [0] * n
        deck.sort()

        for d in deck:
            i = queue.popleft()
            res[i] = d
            if queue:
                x = queue.popleft()
                queue.append(x)

        return res

        


        