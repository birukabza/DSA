from typing import List
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        cur_coins = coins
        for i in range(len(costs)): 
            if costs[i]<= cur_coins:
                count+=1
                cur_coins-=costs[i]
            else:
                return i
            
            if i == len(costs)-1:
                return len(costs)
        

        