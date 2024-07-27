class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        maxScore = weights[0] + weights[n-1]
        minScore = weights[0] + weights[n-1]
        pairSum = [0]*(n-1)
        for i in range(n-1):
            pairSum[i] = weights[i] + weights[i+1]
        
        pairSum.sort()

        for i in range(k-1):
            maxScore += pairSum[n-2-i]
            minScore += pairSum[i]
        
        return maxScore - minScore
        