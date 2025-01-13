#Given to nodes check if there exists a route between them
from collections import deque

#depth approch with recuresion
def is_route(graph, start, end, visited=None):
    # create a set of visisted nodes in case is the first iteration
    if visited is None:
        visited=set()
    # for each child in the node
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            #recurse to go to the next child
            if node == end or is_route(graph,node, end, visited):
                return True
    return False

#breadht approch iteration
def is_route_bdf(graph,start, end ):
    #if root is start and end
    if start==end:
        return True
    visited =set()
    #using queue for breadth-first
    queue = deque()
    queue.append(start)
    while queue:
        node= queue.popleft()
        #for each adjacen node child
        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.add(adjacent)
                if adjacent == end:
                    return True
                else:
                    #add childs to the queue
                    queue.append(adjacent)
    return False

def is_route_bidirectional(graph, start, end):
    to_visit = deque()
    to_visit.append(start)
    to_visit.append(end)
    visited_start = set()
    visited_start.add(start)
    visited_end = set()
    visited_end.add(end)
    while to_visit:
        node = to_visit.popleft()

        if node in visited_start and node in visited_end:
            return True

        for y in graph[node]:
            if node in visited_start and y not in visited_start:
                visited_start.add(y)
                to_visit.append(y)
            if node in visited_end and y not in visited_end:
                visited_end.add(y)
                to_visit.append(y)
    return False

#graph is created with dictionaries, pointing to the child nodes.
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["B", "C"],
    "E": ["C", "F"],
    "F": ["E", "O", "I", "G"],
    "G": ["F", "H"],
    "H": ["G"],
    "I": ["F", "J"],
    "O": ["F"],
    "J": ["K", "L", "I"],
    "K": ["J"],
    "L": ["J"],
    "P": ["Q", "R"],
    "Q": ["P", "R"],
    "R": ["P", "Q"]
}

#test different routes between nodes
tests = [
    ("A", "L", True),
    ("A", "B", True),
    ("H", "K", True),
    ("L", "D", True),
    ("P", "Q", True),
    ("Q", "P", True),
    ("Q", "G", False),
    ("R", "A", False),
    ("P", "B", False),
]

for [start, end, expected] in tests:
    print(is_route(graph, start, end))

for [start, end, expected] in tests:
    print(is_route_bdf(graph, start, end))