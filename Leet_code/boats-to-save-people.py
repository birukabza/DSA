class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        countBoats = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left+=1
                right-=1
            else:
                right-=1
            
            countBoats+=1
        
        return countBoats
