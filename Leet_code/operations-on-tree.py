from collections import defaultdict


class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = defaultdict(list)
        self.state = [[0, None] for _ in range(len(parent))]
        for i, par in enumerate(parent):
            self.graph[i].append(par)
            self.graph[par].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.state[num][0] == 1:
            return False
        self.state[num][0] = 1
        self.state[num][1] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.state[num][1] != user:
            return False
        self.state[num][0] = 0
        self.state[num][1] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.state[num][0]:
            return False

        par = self.parent[num]
        while par != -1:
            if self.state[par][0]:
                return False
            par = self.parent[par]
        flag = False

        def dfs(node, par):
            nonlocal flag
            for child in self.graph[node]:
                if child != par:
                    if self.state[child][0]:
                        self.state[child][0] = 0
                        self.state[child][1] = None
                        flag = True
                    dfs(child, node)

        dfs(num, self.parent[num])
        if not flag:
            return False
        self.state[num][0] = 1
        self.state[num][1] = user
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
