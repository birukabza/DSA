class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        start = 0
        maxPoints = 0
        minPoints = float("inf")
        currentSum = sum(cardPoints[:len(cardPoints)-k])
        minPoints = min(minPoints, currentSum)

        for end in range(len(cardPoints)-k, len(cardPoints)):
            currentSum+=cardPoints[end]
            currentSum-=cardPoints[start]
            minPoints = min(minPoints, currentSum)
            start+=1
        
        maxPoints = sum(cardPoints) - minPoints

        return maxPoints