class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        start = 0
        counter = {}
        maxFruits = 0

        for end in range(len(fruits)):
            counter[fruits[end]] = counter.get(fruits[end], 0)+1

            while len(counter) > 2:
                counter[fruits[start]]-=1

                if counter[fruits[start]] == 0:
                    del counter[fruits[start]]
                
                start+=1
            
            maxFruits = max(maxFruits, end-start+1)
        
        return maxFruits
                






        