# Coding Patterns Cheat Sheet

## Array Patterns

### Sliding Window (Fixed Size)
**When to use:** Finding subarrays of exact size k (max sum of k elements, avg of k elements)

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

### Sliding Window (Flexible - Longest)
**When to use:** Longest substring/subarray with constraint (longest substring with k unique chars)

```python
def sliding_window_flexible_longest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while invalid(window):        # shrink until valid
            remove input[left] from window
            left += 1
        ans = max(ans, window)        # window is valid here
    return ans
```

### Sliding Window (Flexible - Shortest)
**When to use:** Shortest substring/subarray meeting condition (min window substring)

```python
def sliding_window_flexible_shortest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while valid(window):
            ans = min(ans, window)    # window is valid here
            remove input[left] from window
            left += 1
    return ans
```
### Two Pointers
**When to use:** Sorted arrays, finding pairs, reversing (Two Sum, 3Sum, Container With Most Water)

```python
# Opposite direction
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        # process
        left += 1
        right -= 1
    elif need_larger:
        left += 1
    else:
        right -= 1

# Same direction (fast/slow)
slow = fast = 0
while fast < len(arr):
    if condition:
        slow += 1
    fast += 1
```

### Binary Search
**When to use:** Sorted data, finding boundaries, minimizing/maximizing with constraint

```python
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1
    while left <= right:
        mid = (left + right) // 2
        if feasible(mid):
            first_true_index = mid
            right = mid - 1        # search left for first occurrence
        else:
            left = mid + 1
    return first_true_index
```
### Prefix Sum
**When to use:** Range sum queries, subarray sum problems

```python
# Build prefix sum
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)

# Get sum of arr[i:j]
range_sum = prefix[j] - prefix[i]
```

### BFS on Matrix
**When to use:** Shortest path, level-order traversal on grids (flood fill, rotting oranges)

```python
from collections import deque

num_rows, num_cols = len(grid), len(grid[0])

def get_neighbors(coord):
    row, col = coord
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
    res = []
    for dr, dc in directions:
        neighbor_row, neighbor_col = row + dr, col + dc
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
            res.append((neighbor_row, neighbor_col))
    return res

def bfs(starting_node):
    queue = deque([starting_node])
    visited = set([starting_node])
    while queue:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
```

### Union Find (Disjoint Set)
**When to use:** Connected components, cycle detection, dynamic connectivity
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

## Stack & Queue Patterns

### Monotonic Stack
**When to use:** Next greater/smaller element, histogram problems

```python
def mono_stack(insert_entries):
    stack = []  # maintains decreasing order
    for entry in insert_entries:
        while stack and stack[-1] <= entry:
            popped = stack.pop()
            # Do something with popped (found next greater for popped)
        stack.append(entry)
```

### Stack for Parentheses/Brackets
**When to use:** Valid parentheses, calculator problems

```python
stack = []
pairs = {'(': ')', '[': ']', '{': '}'}
for char in s:
    if char in pairs:
        stack.append(char)
    elif not stack or pairs[stack.pop()] != char:
        return False
return len(stack) == 0
```

## Tree Patterns

### DFS (Inorder/Preorder/Postorder)
**When to use:** Path problems, tree construction, validation

```python
# Recursive DFS
def dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    # Preorder: process before children
    left = dfs(root.left, target)
    if left is not None:
        return left
    # Inorder: process between children (for BST)
    return dfs(root.right, target)
    # Postorder: process after children

# Iterative DFS
def dfs_iterative(root):
    stack = [root]
    while stack:
        node = stack.pop()
        # process node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### BFS (Level Order)
**When to use:** Level-by-level traversal, shortest path in tree

```python
from collections import deque

def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for _ in range(level_size):  # process level by level
            node = queue.popleft()
            # process node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
```

### Trie (Prefix Tree)
**When to use:** Word search, autocomplete, prefix matching

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
```

## Graph Patterns

### BFS on Graphs
**When to use:** Shortest path (unweighted), level exploration

```python
from collections import deque

def bfs(root):
    queue = deque([root])
    visited = set([root])
    while queue:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
```

### DFS on Graphs
**When to use:** Cycle detection, connected components, path finding

```python
def dfs(node, visited):
    visited.add(node)
    for neighbor in get_neighbors(node):
        if neighbor in visited:
            continue
        dfs(neighbor, visited)

# Iterative version
def dfs_iterative(root):
    stack = [root]
    visited = set([root])
    while stack:
        node = stack.pop()
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
```

### Topological Sort
**When to use:** Task scheduling, course prerequisites (DAGs only)

```python
from collections import deque

def find_indegree(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    return indegree

def topo_sort(graph):
    res = []
    q = deque()
    indegree = find_indegree(graph)

    # Start with nodes that have no dependencies
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)

    while q:
        node = q.popleft()
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # Check if cycle exists
    return res if len(graph) == len(res) else None
```

## Backtracking Patterns

### Backtracking (Combinations/Subsets)
**When to use:** Generate all combinations, subsets, permutations

```python
def backtrack(start_index, path, result):
    result.append(path[:])  # add current state to result

    for i in range(start_index, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path, result)  # i+1 for combinations, start for repetition
        path.pop()  # backtrack
```

### Backtracking (Permutations)
**When to use:** All orderings matter

```python
def backtrack(path, used, result):
    if len(path) == len(nums):
        result.append(path[:])
        return

    for i in range(len(nums)):
        if used[i]:
            continue
        path.append(nums[i])
        used[i] = True
        backtrack(path, used, result)
        used[i] = False
        path.pop()
```

### Backtracking (Word Search/Board)
**When to use:** Finding paths in grids with constraints

```python
def backtrack(row, col, index):
    if index == len(word):
        return True

    if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0])
        or board[row][col] != word[index]):
        return False

    temp = board[row][col]
    board[row][col] = '#'  # mark as visited

    found = (backtrack(row+1, col, index+1) or
             backtrack(row-1, col, index+1) or
             backtrack(row, col+1, index+1) or
             backtrack(row, col-1, index+1))

    board[row][col] = temp  # restore
    return found
```

## Dynamic Programming Patterns

### 1D DP
**When to use:** Fibonacci-like, house robber, climbing stairs

```python
# Bottom-up
dp = [0] * (n + 1)
dp[0], dp[1] = base_case_0, base_case_1
for i in range(2, n + 1):
    dp[i] = some_function(dp[i-1], dp[i-2])
return dp[n]
```

### 2D DP
**When to use:** Longest common subsequence, edit distance, grid paths

```python
# Grid paths example
dp = [[0] * n for _ in range(m)]
dp[0][0] = 1

for i in range(m):
    for j in range(n):
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]
```

### Knapsack (0/1)
**When to use:** Subset sum, partition equal subset

```python
# dp[i][w] = max value using first i items with weight limit w
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(W + 1):
        # Don't take item i-1
        dp[i][w] = dp[i-1][w]
        # Take item i-1 if it fits
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
```

## Heap Patterns

### Top K Elements
**When to use:** Kth largest/smallest, top K frequent

```python
import heapq

# Min heap for K largest
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)

# Max heap (negate values)
heap = []
for num in nums:
    heapq.heappush(heap, -num)
```

### K-Way Merge
**When to use:** Merge K sorted lists

```python
import heapq

heap = []
for i, lst in enumerate(lists):
    if lst:
        heapq.heappush(heap, (lst[0], i, 0))  # (value, list_idx, elem_idx)

result = []
while heap:
    val, list_idx, elem_idx = heapq.heappop(heap)
    result.append(val)
    if elem_idx + 1 < len(lists[list_idx]):
        next_val = lists[list_idx][elem_idx + 1]
        heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
```

---

## Quick Pattern Recognition Guide

**See contiguous subarray/substring?** → Sliding Window or Prefix Sum
**See sorted array + find pair?** → Two Pointers
**See "find all combinations"?** → Backtracking
**See "optimize/min/max with subproblems"?** → Dynamic Programming
**See tree traversal?** → DFS or BFS
**See "shortest path" unweighted?** → BFS
**See "top K" or "Kth largest"?** → Heap
**See sorted + search?** → Binary Search
**See graph + dependencies?** → Topological Sort
**See connected components?** → Union Find or DFS
