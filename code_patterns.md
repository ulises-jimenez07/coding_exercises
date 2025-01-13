# Templates

## Array

### Sliding Window (Fixed Size)

```python
def sliding_window_fixed(input, window_size):
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size
        remove input[left] from window
        append input[right] to window
        ans = optimal(ans, window)
    return ans
```

### Sliding Window (Fixed Flexible)

```python
def sliding_window_flexible_longest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while invalid(window):        # update left until window is valid again
            remove input[left] from window
            left += 1
        ans = max(ans, window)        # window is guaranteed to be valid here
    return ans
``` 


### Sliding Window (Fixed Flexible shortest)

```python
def sliding_window_flexible_shortest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while valid(window):
            ans = min(ans, window)      # window is guaranteed to be valid here
            remove input[left] from window
            left += 1
    return ans
```
### Binary Search

```python
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1
    while left <= right:
        mid = (left + right) // 2
        if feasible(mid):
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_true_index
```
### BFS on Matrix

```python
num_rows, num_cols = len(grid), len(grid[0])
def get_neighbors(coord):
    row, col = coord
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
            res.append((neighbor_row, neighbor_col))
    return res

from collections import deque

def bfs(starting_node):
    queue = deque([starting_node])
    visited = set([starting_node])
    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            # Do stuff with the node if required
            # ...
            queue.append(neighbor)
            visited.add(neighbor)
```

### Union Find
```python
class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)
```

## Queues Stack

### Mono Stack

```python
def mono_stack(insert_entries):
    stack = []
    for entry in insert_entries:
        while stack and stack[-1] <= entry:
            stack.pop()
            # Do something with the popped item here
        stack.append(entry)
```

## Trees

### DFS (Depth First Search)

```python
def dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    left = dfs(root.left, target)
    if left is not None:
        return left
    return dfs(root.right, target)
```

### BFS (Breadth First Search)

```python
def bfs(root):
    queue = deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        for child in node.children:
            if is_goal(child):
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND
```

### Trie

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def insert(self, s, idx):
        # idx: index of the current character in s
        if idx != len(s):
            self.children.setdefault(s[idx], Node(s[idx]))
            self.children.get(s[idx]).insert(s, idx + 1)
```

## Graphs

### Backtracking 1

```python
ans = []
def dfs(start_index, path, [...additional states]):
    if is_leaf(start_index):
        ans.append(path[:]) # add a copy of the path to the result
        return
    for edge in get_edges(start_index, [...additional states]):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        if additional states:
            update(...additional states)
        dfs(start_index + len(edge), path, [...additional states])
        # revert(...additional states) if necessary e.g. permutations
        path.pop()
```

### Backtracking 2

```python
def dfs(start_index, [...additional states]):
    if is_leaf(start_index):
        return 1
    ans = initial_value
    for edge in get_edges(start_index, [...additional states]):
        if additional states: 
            update([...additional states])
        ans = aggregate(ans, dfs(start_index + len(edge), [...additional states]))
        if additional states: 
            revert([...additional states])
    return ans
```

### BFS on graphs

```python
def bfs(root):
    queue = deque([root])
    visited = set([root])
    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
```

### DFS on graphs

```python
def dfs(root, visited):
    for neighbor in get_neighbors(root):
        if neighbor in visited:
            continue
        visited.add(neighbor)
        dfs(neighbor, visited)
```

### Topological sort

```python 
def find_indegree(graph):
    indegree = { node: 0 for node in graph }  # dict
    for node in graph:
        for neighbor in graph[node]:
            indgree[neighbor] += 1
    return indegree


def topo_sort(graph):
    res = []
    q = deque()
    indegree = find_indegree(graph)
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
    while len(q) > 0:
        node = q.popleft()
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return res if len(graph) == len(res) else None
```

# 8 Patterns

## Sliding window
Use for a subset of elements that satisfy
Array, Linked

Ex. Find the longest substring with k unique characters in a given string

## Subset
Possible combinations, repetitions or not repetitions.
Iterate 

## Modify Binary Search
Search in Rotated Array, bisect left and right

## Top K elements
Select K elements, top ranking elements
Heap <- 

## Binary Tree DFS
Recursion Maximum left of a 

## Topological Sort
Arrange elements in a specific order when there is dependencies DAG
Course schedule

## Binary Tree BFS
Queue data structure
Binary Level Order Traversal

## Two Pointer pattern
Two sum problem <- sorted


# Patters 2
## Linear
### Two pointers
Reduce time complexity when traversing line structures (array, linked list)

1. Same direction : single past, slow fast pointer
2. Opposite directions: Involve finding pairs or compare elements 

### Sliding window

Maintains a window of data. Tracking contigous sequeneces. Often with hash maps

### Binary search
repating looking at halfs

## Non-Linear

Trees and graphs. A tree is agraph with no cycles

### BFS
Nodes are visited in the correct order. Level order

### DFS
```python
def get_neighbors(grid, row, col):
neighbors = []
directions = [(0, 1), (1, 0), (0, -1), (−1, 0)]
for d in directions:
new_row, new_col = row + d[0], col + d[1]
if 0 <= new_row < len(grid)
and 0 <= new_col < len(grid[0])
and grid[new_row][new_col] == '1':
neighbors.append((new_row, new_col))
return neighbors
def dfs(grid, row, col, visited):
visited.add((row, col))
for neighbor in get_neighbors(grid, row, col):
if neighbor in visited:
continue
dfs(grid, neighbor[0], neighbor [1], visited)
```

### Backtracking
Combinations

### Top K
Priority queue. Heaps (Min/Max)

### Dynamic Programming
Optimizing the solution by storing overlapping solutions