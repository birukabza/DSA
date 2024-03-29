class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort(reverse=True)
        j=1
        max_coin=0
        for _ in range((len(piles)//3)):
            max_coin+=piles[j]
            j+=2
        return max_coin
            
        
        
        