from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque([0])

        while queue:
            key = queue.popleft()

            for k in rooms[key]:
                if k not in visited:
                    visited.add(k)
                    queue.append(k)

        return len(visited) == len(rooms) 