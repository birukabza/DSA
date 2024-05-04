class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        counter = 0
        n = len(tickets)
        
        for i in range(n):
            if i <=k:
                counter += min(tickets[i], tickets[k])
            else:
                counter+= min(tickets[i], tickets[k]-1)            
        
        return counter

        