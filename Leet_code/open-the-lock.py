from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def neighbor(wheels):
            ans = []
            for i in range (4):
                plus = wheels[:i] + str((int(wheels[i]) + 1)%10) + wheels[i+1:]
                ans.append(plus)
                minus = wheels[:i] + str((int(wheels[i]) - 1)%10) + wheels[i+1:]
                ans.append(minus)

            return ans
        
        queue = deque(["0000"])
        visited = set(deadends)
        level = 0

        while queue:
            for _ in range(len(queue)):
                wheels = queue.popleft()
                if wheels == target:
                    return level

                for wheel in neighbor(wheels):
                    if wheel not in visited:
                        visited.add(wheel)
                        queue.append(wheel)
            level+=1
                    
                    

        return -1
