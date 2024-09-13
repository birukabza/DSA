from collections import defaultdict


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[(parentName)].append((childName))

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []

        self.dfs(self.king, order)
        return order

    def dfs(self, node, order):
        if node not in self.dead:
            order.append(node)

        for nei in self.graph[node]:
            self.dfs(nei, order)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
