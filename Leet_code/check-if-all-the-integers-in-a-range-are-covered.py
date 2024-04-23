class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        for i in range(left, right + 1):
            is_covered = False
            for start, end in ranges:
                if start <= i <= end:
                    is_covered= True
                    break
            if not is_covered:
                return False
        return True
                


