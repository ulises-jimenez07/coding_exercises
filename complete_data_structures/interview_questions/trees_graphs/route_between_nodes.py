from collections import deque


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, startNode, endNode):
        visited = set()
        visited.add(startNode)
        queue = deque()
        queue.append(startNode)

        while queue:
            current = queue.popleft()

            for adjacent in self.gdict[current]:
                if adjacent not in visited:
                    if adjacent == endNode:
                        return True
                    else:
                        queue.append(adjacent)
        return False
