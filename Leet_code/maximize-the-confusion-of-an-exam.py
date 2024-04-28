class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def confusion(letter):
            start = 0
            res = 0
            count = k
            for end in range(len(answerKey)):
                if answerKey[end]!=letter:
                    count-=1
                while count < 0:
                    if answerKey[start]!=letter:
                        count+=1
                    start+=1
                res = max(res, end-start+1)
            return res
        return max(confusion('T'), confusion('F'))