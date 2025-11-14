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

**Example: Maximum Average Subarray**
```python
def findMaxAverage(nums, k):
    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window: remove leftmost, add rightmost
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)

    return max_sum / k

# Example: nums = [1,12,-5,-6,50,3], k = 4
# Window [1,12,-5,-6] = 2
# Window [12,-5,-6,50] = 51 (max)
# Window [-5,-6,50,3] = 42
# Answer: 51/4 = 12.75
```

**LeetCode Problems:**
- 643. Maximum Average Subarray I - [Solution](leet_code/array/643_max_avg_subarray.py)
- 1456. Maximum Number of Vowels in a Substring of Given Length - [Solution](leet_code/array/1456_max_number_vowels_substring_giving_length.py)
- 1876. Substrings of Size Three with Distinct Characters - [Solution](leet_code/array/1876_substrings_of_size3_distinct_characters.py)
- 2269. Find the K-Beauty of a Number - [Solution](leet_code/array/2269_find_k_beauty.py)

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

**Example: Longest Substring Without Repeating Characters**
```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Add current character to window
        while s[right] in char_set:  # Invalid: has duplicate
            char_set.remove(s[left])  # Shrink from left
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

# Example: s = "abcabcbb"
# Window "abc" (valid, length 3)
# Window "abca" (invalid, shrink) -> "bca" (valid)
# Window "bcab" (invalid, shrink) -> "cab" (valid)
# Answer: 3
```

**LeetCode Problems:**
- 3. Longest Substring Without Repeating Characters - [Solution](leet_code/array/3_longest_substring_withouth_repeating.py)
- 424. Longest Repeating Character Replacement - [Solution](leet_code/array/424_longest_repeating_char_replacement.py)
- 1004. Max Consecutive Ones III - [Solution](leet_code/array/1004_max_consecutive_ones_iii.py)
- 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit - [Solution](leet_code/array/1438_longest_continous_subarray_with_abs_diff.py)
- 239. Sliding Window Maximum [Solution](leet_code/queues_stacks/239_sliding_window_maximum.py)
- 992. Subarrays with K Different Integers - [Solution](leet_code/array/992_subarrays_with_k_different_int.py)


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

**Example: Minimum Size Subarray Sum**
```python
def minSubArrayLen(target, nums):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]  # Expand window

        while current_sum >= target:  # Valid window
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]  # Shrink window
            left += 1

    return min_length if min_length != float('inf') else 0

# Example: target = 7, nums = [2,3,1,2,4,3]
# Window [2,3,1,2] sum=8 (valid, length 4)
# Window [3,1,2,4] sum=10 (valid, length 4)
# Window [4,3] sum=7 (valid, length 2) <- minimum
# Answer: 2
```

**LeetCode Problems:**
- 209. Minimum Size Subarray Sum - [Solution](leet_code/array/209_min_siz_subarray_sum.py)
- 76. Minimum Window Substring - [Solution](leet_code/hash_tables/76_minimum_window_substr.py)
- 862. Shortest Subarray with Sum at Least K - [Solution](leet_code/array/862_shortest_subarray_sum_at_least_k.py)
- 1658. Minimum Operations to Reduce X to Zero  - [Solution](leet_code/array/1658_min_op_to_reduce_x_zero.py)
### Fast & Slow Pointers (Floyd's Cycle Detection)
**When to use:** Linked list cycle detection, finding middle of list, finding start of cycle

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

**Example: Linked List Cycle**
```python
def hasCycle(head):
    slow = fast = head

    # Move slow by 1, fast by 2
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If they meet, there's a cycle
        if slow == fast:
            return True

    return False

# Example: 3 -> 2 -> 0 -> -4 (with -4 pointing back to 2)
# slow: 3 -> 2 -> 0 -> -4 -> 2 -> 0
# fast: 3 -> 0 -> 2 -> -4 -> 0 -> 2
# They meet at position 2 (cycle detected)
# Answer: True
```

**LeetCode Problems:**
- 141. Linked List Cycle - [Solution](leet_code/linked_lists/141_is_cycle_linked_list.py)
- 142. Linked List Cycle II - [Solution](leet_code/linked_lists/142_linked_list_cycle_2.py)
- 876. Middle of the Linked List - [Solution](leet_code/linked_lists/876_middle_linked_list.py)
- 234. Palindrome Linked List - [Solution](leet_code/linked_lists/234_palindrome_linkded_list.py)
- 202. Happy Number - [Solution](leet_code/linked_lists/202_happy_number.py)

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

**Example: Two Sum II (Sorted Array)**
```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum

    return []

# Example: numbers = [2,7,11,15], target = 9
# left=0, right=3: 2+15=17 (too large, right--)
# left=0, right=2: 2+11=13 (too large, right--)
# left=0, right=1: 2+7=9 (found!)
# Answer: [1, 2]
```

**LeetCode Problems:**
- 167. Two Sum II - Input Array Is Sorted - [Solution](leet_code/array/167_two_sum_2_sorted.py)
- 15. 3Sum - [Solution](leet_code/array/15_3sum.py)
- 11. Container With Most Water - [Solution](leet_code/array/11_container_wiht_most_water.py)
- 283. Move Zeroes - [Solution](leet_code/array/283_move_zeros.py)
- 344. Reverse String - [Solution](leet_code/array/344_reverse_string.py)

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

**Example: Find First and Last Position of Element**
```python
def searchRange(nums, target):
    def findBound(isFirst):
        left, right = 0, len(nums) - 1
        bound = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                bound = mid
                if isFirst:
                    right = mid - 1  # Search left for first
                else:
                    left = mid + 1   # Search right for last
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return bound

    return [findBound(True), findBound(False)]

# Example: nums = [5,7,7,8,8,10], target = 8
# First occurrence: binary search finds 8, search left -> index 3
# Last occurrence: binary search finds 8, search right -> index 4
# Answer: [3, 4]
```

**LeetCode Problems:**
- 34. Find First and Last Position of Element in Sorted Array - [Solution](leet_code/binary_search/34_first_last_position_elem.py)
- 704. Binary Search
- 33. Search in Rotated Sorted Array - [Solution](leet_code/binary_search/33_find_rotated_array.py)
- 875. Koko Eating Bananas - [Solution](leet_code/binary_search/875_koko_eating_bananas.py)
- 1011. Capacity To Ship Packages Within D Days
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

**Example: Subarray Sum Equals K**
```python
def subarraySum(nums, k):
    # Key insight: if prefix[j] - prefix[i] = k, then prefix[i] = prefix[j] - k
    count = 0
    current_sum = 0
    sum_freq = {0: 1}  # prefix sum -> frequency

    for num in nums:
        current_sum += num

        # Check if there's a prefix sum that makes current subarray = k
        if current_sum - k in sum_freq:
            count += sum_freq[current_sum - k]

        sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1

    return count

# Example: nums = [1,2,3], k = 3
# prefix sums: 0, 1, 3, 6
# At sum=3: sum-k=0 exists (count=1) -> subarray [1,2]
# At sum=6: sum-k=3 exists (count=2) -> subarray [3]
# Answer: 2
```

**LeetCode Problems:**
- 560. Subarray Sum Equals K - [Solution](leet_code/array/560_subarray_sum_equals_k.py)
- 303. Range Sum Query - Immutable
- 525. Contiguous Array
- 974. Subarray Sums Divisible by K
- 1480. Running Sum of 1d Array

### Merge Intervals
**When to use:** Overlapping intervals, meeting rooms, scheduling problems

```python
def merge_intervals(intervals):
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        # If merged is empty or no overlap, add interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge by updating end time
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
```

**Example: Merge Intervals**
```python
def merge(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        # If merged is empty or current interval doesn't overlap
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge overlapping intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example: intervals = [[1,3],[2,6],[8,10],[15,18]]
# After sort: [[1,3],[2,6],[8,10],[15,18]]
# Process [1,3]: merged = [[1,3]]
# Process [2,6]: 3 >= 2 (overlap), merge -> [[1,6]]
# Process [8,10]: 6 < 8 (no overlap), add -> [[1,6],[8,10]]
# Process [15,18]: 10 < 15 (no overlap), add -> [[1,6],[8,10],[15,18]]
# Answer: [[1,6],[8,10],[15,18]]
```

**LeetCode Problems:**
- 56. Merge Intervals - [Solution](leet_code/array/56_merged_intervals.py)
- 57. Insert Interval
- 252. Meeting Rooms
- 253. Meeting Rooms II
- 435. Non-overlapping Intervals

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

**Example: Rotting Oranges**
```python
def orangesRotting(grid):
    from collections import deque
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Find all initially rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, minutes)
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        r, c, minutes = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2  # Make it rotten
                fresh -= 1
                queue.append((nr, nc, minutes + 1))

    return minutes if fresh == 0 else -1

# Example: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Minute 0: (0,0) is rotten
# Minute 1: (0,1), (1,0) rot
# Minute 2: (0,2), (1,1), (2,1) rot
# Minute 3: (1,2) rots
# Minute 4: (2,2) rots
# Answer: 4 minutes
```

**LeetCode Problems:**
- 994. Rotting Oranges
- 200. Number of Islands - [Solution](leet_code/graph/200_number_island.py)
- 733. Flood Fill - [Solution](leet_code/graph/733_flood_fill.py)
- 542. 01 Matrix
- 1091. Shortest Path in Binary Matrix

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

**Example: Number of Connected Components**
```python
def countComponents(n, edges):
    uf = UnionFind()

    # Union all connected nodes
    for a, b in edges:
        uf.union(a, b)

    # Count unique root parents
    return len(set(uf.find(i) for i in range(n)))

class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

# Example: n = 5, edges = [[0,1],[1,2],[3,4]]
# Components: {0,1,2} and {3,4}
# After union(0,1): 0->1
# After union(1,2): 0->1->2
# After union(3,4): 3->4
# Unique roots: 2 and 4
# Answer: 2 components
```

**LeetCode Problems:**
- 323. Number of Connected Components in an Undirected Graph
- 547. Number of Provinces
- 684. Redundant Connection
- 200. Number of Islands (can also use Union Find)
- 1319. Number of Operations to Make Network Connected

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

**Example: Next Greater Element**
```python
def nextGreaterElement(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # Stack stores indices

    for i in range(n):
        # Pop elements smaller than current (they found their next greater)
        while stack and nums[stack[-1]] < nums[i]:
            prev_idx = stack.pop()
            result[prev_idx] = nums[i]

        stack.append(i)

    return result

# Example: nums = [2,1,2,4,3]
# i=0: stack=[0]
# i=1: nums[1]=1 < nums[0]=2, stack=[0,1]
# i=2: nums[2]=2 > nums[1]=1, pop 1, result[1]=2
#      nums[2]=2 == nums[0]=2, stack=[0,2]
# i=3: nums[3]=4 > all, pop 2,0, result[2]=4, result[0]=4, stack=[3]
# i=4: nums[4]=3 < nums[3]=4, stack=[3,4]
# Answer: [4,2,4,-1,-1]
```

**LeetCode Problems:**
- 496. Next Greater Element I
- 503. Next Greater Element II
- 739. Daily Temperatures
- 84. Largest Rectangle in Histogram
- 42. Trapping Rain Water

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

**Example: Valid Parentheses**
```python
def isValid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        else:  # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0

# Example: s = "({[]})"
# char='(': stack=['(']
# char='{': stack=['(','{']
# char='[': stack=['(','{','[']
# char=']': pop '[', matches, stack=['(','{']
# char='}': pop '{', matches, stack=['(']
# char=')': pop '(', matches, stack=[]
# Answer: True (valid)
```

**LeetCode Problems:**
- 20. Valid Parentheses - [Solution](leet_code/queues_stacks/20_valid_parenthesis.py)
- 22. Generate Parentheses
- 32. Longest Valid Parentheses
- 1541. Minimum Insertions to Balance a Parentheses String
- 921. Minimum Add to Make Parentheses Valid - [Solution](leet_code/strings/921_minimum_add_make_parenthisis_valid.py)

## Linked List Patterns

### In-Place Reversal
**When to use:** Reversing linked list, reversing in groups, swapping nodes

```python
def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # Save next
        current.next = prev        # Reverse link
        prev = current             # Move prev forward
        current = next_node        # Move current forward

    return prev  # New head
```

**Example: Reverse Linked List**
```python
def reverseList(head):
    prev = None

    while head:
        next_node = head.next  # Save next node
        head.next = prev       # Reverse the link
        prev = head            # Move prev to current
        head = next_node       # Move to next node

    return prev  # New head of reversed list

# Example: 1 -> 2 -> 3 -> 4 -> 5
# Step 1: prev=None, head=1
#   next=2, 1->None, prev=1, head=2
# Step 2: prev=1, head=2
#   next=3, 2->1, prev=2, head=3
# Step 3: prev=2, head=3
#   next=4, 3->2, prev=3, head=4
# Step 4: prev=3, head=4
#   next=5, 4->3, prev=4, head=5
# Step 5: prev=4, head=5
#   next=None, 5->4, prev=5, head=None
# Answer: 5 -> 4 -> 3 -> 2 -> 1
```

**LeetCode Problems:**
- 206. Reverse Linked List - [Solution](leet_code/linked_lists/206_reverse_linked_list.py)
- 92. Reverse Linked List II
- 25. Reverse Nodes in k-Group
- 24. Swap Nodes in Pairs
- 61. Rotate List

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

**Example: Validate Binary Search Tree**
```python
def isValidBST(root):
    def validate(node, min_val, max_val):
        if not node:
            return True

        # Current node must be within bounds
        if not (min_val < node.val < max_val):
            return False

        # Left subtree: all values < node.val
        # Right subtree: all values > node.val
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))

    return validate(root, float('-inf'), float('inf'))

# Example tree:     5
#                  / \
#                 3   7
#                / \
#               2   4
# validate(5, -inf, inf): True
#   validate(3, -inf, 5): True
#     validate(2, -inf, 3): True
#     validate(4, 3, 5): True
#   validate(7, 5, inf): True
# Answer: True (valid BST)
```

**LeetCode Problems:**
- 98. Validate Binary Search Tree - [Solution](leet_code/trees/98_validate_BST.py)
- 104. Maximum Depth of Binary Tree - [Solution](leet_code/trees/104_max_depth.py)
- 112. Path Sum - [Solution](leet_code/trees/112_path_sum.py)
- 543. Diameter of Binary Tree - [Solution](leet_code/trees/543_diameter_binary_tree.py)
- 236. Lowest Common Ancestor of a Binary Tree - [Solution](leet_code/trees/236_lowest_common_ancester.py)

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

**Example: Binary Tree Level Order Traversal**
```python
def levelOrder(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

# Example tree:     3
#                  / \
#                 9  20
#                   /  \
#                  15   7
# Level 0: queue=[3], output=[3]
# Level 1: queue=[9,20], output=[9,20]
# Level 2: queue=[15,7], output=[15,7]
# Answer: [[3],[9,20],[15,7]]
```

**LeetCode Problems:**
- 102. Binary Tree Level Order Traversal - [Solution](leet_code/trees/102_binary_tree_level_order.py)
- 107. Binary Tree Level Order Traversal II
- 199. Binary Tree Right Side View - [Solution](leet_code/trees/199_binary_tree_right.py)
- 637. Average of Levels in Binary Tree
- 103. Binary Tree Zigzag Level Order Traversal - [Solution](leet_code/queues_stacks/103_binary_tree_zigzag.py)

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

**Example: Implement Trie (Prefix Tree)**
```python
trie = Trie()

# Insert "apple"
# root -> 'a' -> 'p' -> 'p' -> 'l' -> 'e' (is_end=True)
trie.insert("apple")

# Search "apple": traverse a->p->p->l->e, is_end=True -> Found
trie.search("apple")  # Returns True

# Search "app": traverse a->p->p, is_end=False -> Not found
trie.search("app")    # Returns False

# Insert "app"
trie.insert("app")

# Search "app": traverse a->p->p, is_end=True -> Found
trie.search("app")    # Returns True

# StartsWith "app": traverse a->p->p -> Prefix exists
trie.startsWith("app")  # Returns True
```

**LeetCode Problems:**
- 208. Implement Trie (Prefix Tree)
- 211. Design Add and Search Words Data Structure
- 212. Word Search II
- 648. Replace Words
- 677. Map Sum Pairs

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

**Example: Clone Graph**
```python
def cloneGraph(node):
    if not node:
        return None

    from collections import deque

    # Map original node to cloned node
    clones = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        current = queue.popleft()

        for neighbor in current.neighbors:
            if neighbor not in clones:
                # Create clone of neighbor
                clones[neighbor] = Node(neighbor.val)
                queue.append(neighbor)

            # Add cloned neighbor to current's clone
            clones[current].neighbors.append(clones[neighbor])

    return clones[node]

# Example: 1--2
#          |  |
#          4--3
# BFS from 1: visit 1, clone 1
# Visit neighbors 2,4: clone 2,4, add to 1's neighbors
# Visit 2's neighbors: 1 (visited), 3 (clone and add)
# Visit 4's neighbors: 1 (visited), 3 (visited, just link)
# Answer: Cloned graph with same structure
```

**LeetCode Problems:**
- 133. Clone Graph - [Solution](leet_code/graph/133_clone_graph.py)
- 127. Word Ladder
- 286. Walls and Gates
- 1091. Shortest Path in Binary Matrix
- 934. Shortest Bridge

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

**Example: Course Schedule (Cycle Detection)**
```python
def canFinish(numCourses, prerequisites):
    # Build adjacency list
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * numCourses

    def hasCycle(course):
        if state[course] == 1:  # Currently visiting -> cycle!
            return True
        if state[course] == 2:  # Already visited
            return False

        state[course] = 1  # Mark as visiting
        for prereq in graph[course]:
            if hasCycle(prereq):
                return True
        state[course] = 2  # Mark as visited
        return False

    # Check each course
    for course in range(numCourses):
        if hasCycle(course):
            return False

    return True

# Example: numCourses = 2, prerequisites = [[1,0]]
# Course 1 requires course 0
# DFS from 1: visits 0 (no cycle)
# DFS from 0: no prerequisites
# Answer: True (can finish all courses)
```

**LeetCode Problems:**
- 207. Course Schedule - [Solution](leet_code/graph/207_course_schedule.py)
- 210. Course Schedule II
- 261. Graph Valid Tree
- 797. All Paths From Source to Target
- 802. Find Eventual Safe States

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

**Example: Course Schedule II**
```python
def findOrder(numCourses, prerequisites):
    from collections import deque

    # Build graph and calculate indegrees
    graph = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses

    for course, prereq in prerequisites:
        graph[prereq].append(course)  # prereq -> course
        indegree[course] += 1

    # Start with courses that have no prerequisites
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        # Remove this course and update indegrees
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    # If we processed all courses, return order; else cycle exists
    return order if len(order) == numCourses else []

# Example: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Indegrees: [0, 1, 1, 2]
# Start queue: [0]
# Process 0: add 1,2 (indegree becomes 0)
# Process 1: add 3 (indegree 1)
# Process 2: add 3 (indegree 0)
# Process 3
# Answer: [0,1,2,3] or [0,2,1,3]
```

**LeetCode Problems:**
- 210. Course Schedule II
- 207. Course Schedule
- 269. Alien Dictionary
- 310. Minimum Height Trees
- 1136. Parallel Courses

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

**Example: Subsets**
```python
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Add current subset

        for i in range(start, len(nums)):
            path.append(nums[i])       # Choose
            backtrack(i + 1, path)     # Explore
            path.pop()                  # Unchoose (backtrack)

    backtrack(0, [])
    return result

# Example: nums = [1,2,3]
# Start: [] -> add []
#   Add 1: [1] -> add [1]
#     Add 2: [1,2] -> add [1,2]
#       Add 3: [1,2,3] -> add [1,2,3]
#     Remove 2, Add 3: [1,3] -> add [1,3]
#   Remove 1, Add 2: [2] -> add [2]
#     Add 3: [2,3] -> add [2,3]
#   Remove 2, Add 3: [3] -> add [3]
# Answer: [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
```

**LeetCode Problems:**
- 78. Subsets - [Solution](leet_code/back_tracking/78_subset.py)
- 90. Subsets II
- 77. Combinations
- 39. Combination Sum - [Solution](leet_code/back_tracking/39_combination_sum.py)
- 40. Combination Sum II

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

**Example: Permutations**
```python
def permute(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            path.append(nums[i])
            used[i] = True
            backtrack(path, used)
            used[i] = False
            path.pop()

    backtrack([], [False] * len(nums))
    return result

# Example: nums = [1,2,3]
# Path=[], used=[F,F,F]
#   Choose 1: path=[1], used=[T,F,F]
#     Choose 2: path=[1,2], used=[T,T,F]
#       Choose 3: path=[1,2,3] -> add [1,2,3]
#     Choose 3: path=[1,3], used=[T,F,T]
#       Choose 2: path=[1,3,2] -> add [1,3,2]
#   Choose 2: path=[2], used=[F,T,F]
#     ... generates [2,1,3], [2,3,1]
#   Choose 3: path=[3], used=[F,F,T]
#     ... generates [3,1,2], [3,2,1]
# Answer: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**LeetCode Problems:**
- 46. Permutations - [Solution](leet_code/back_tracking/46_permutations.py)
- 47. Permutations II - [Solution](leet_code/back_tracking/47_permutations_2.py)
- 784. Letter Case Permutation
- 996. Number of Squareful Arrays
- 1096. Brace Expansion II

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

**Example: Word Search**
```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, index):
        if index == len(word):
            return True

        if (r < 0 or r >= rows or c < 0 or c >= cols or
            board[r][c] != word[index]):
            return False

        temp = board[r][c]
        board[r][c] = '#'  # Mark visited

        found = (backtrack(r+1, c, index+1) or
                 backtrack(r-1, c, index+1) or
                 backtrack(r, c+1, index+1) or
                 backtrack(r, c-1, index+1))

        board[r][c] = temp  # Restore
        return found

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False

# Example: board = [['A','B','C'],
#                   ['S','F','C'],
#                   ['A','D','E']]
#          word = "ABCCED"
# Start at (0,0)='A': mark visited
#   Move to (0,1)='B': mark visited
#     Move to (0,2)='C': mark visited
#       Move to (1,2)='C': mark visited
#         Move to (2,2)='E': mark visited
#           Move to (2,1)='D': Found!
# Answer: True
```

**LeetCode Problems:**
- 79. Word Search - [Solution](leet_code/back_tracking/79_word_search.py)
- 212. Word Search II
- 51. N-Queens - [Solution](leet_code/back_tracking/51_n_queens.py)
- 37. Sudoku Solver
- 980. Unique Paths III

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

**Example: House Robber**
```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # dp[i] = max money robbing up to house i
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        # Either rob current house + dp[i-2] OR skip it and take dp[i-1]
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])

    return dp[-1]

# Example: nums = [2,7,9,3,1]
# dp[0] = 2 (rob house 0)
# dp[1] = max(2, 7) = 7 (rob house 1)
# dp[2] = max(9+2, 7) = 11 (rob houses 0,2)
# dp[3] = max(3+7, 11) = 11 (rob houses 1)
# dp[4] = max(1+11, 11) = 12 (rob houses 0,2,4)
# Answer: 12
```

**LeetCode Problems:**
- 198. House Robber - [Solution](leet_code/dynamic_programming/198_house_robber.py)
- 70. Climbing Stairs - [Solution](leet_code/dynamic_programming/70_climbing_stairs.py)
- 746. Min Cost Climbing Stairs - [Solution](leet_code/dynamic_programming/746_min_cost_climbing_stairs.py)
- 91. Decode Ways - [Solution](leet_code/dynamic_programming/91_decoded_ways.py)
- 1137. N-th Tribonacci Number

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

**Example: Longest Common Subsequence**
```python
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    # dp[i][j] = LCS length of text1[0:i] and text2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                # Characters match: add 1 to previous LCS
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # Take max of skipping either character
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Example: text1 = "abcde", text2 = "ace"
#     ""  a  c  e
# ""   0  0  0  0
# a    0  1  1  1
# b    0  1  1  1
# c    0  1  2  2
# d    0  1  2  2
# e    0  1  2  3
# Answer: 3 (subsequence "ace")
```

**LeetCode Problems:**
- 1143. Longest Common Subsequence - [Solution](leet_code/dynamic_programming/1143_longest_common_subsequence.py)
- 72. Edit Distance
- 62. Unique Paths - [Solution](leet_code/dynamic_programming/62_unique_paths.py)
- 64. Minimum Path Sum
- 221. Maximal Square

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

**Example: Partition Equal Subset Sum**
```python
def canPartition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    # dp[i] = can we make sum i using subset of nums
    dp = [False] * (target + 1)
    dp[0] = True  # We can always make sum 0

    for num in nums:
        # Traverse backwards to avoid using same element twice
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]

# Example: nums = [1,5,11,5]
# target = 11
# dp = [T,F,F,F,F,F,F,F,F,F,F,F]
# Add 1: [T,T,F,F,F,F,F,F,F,F,F,F]
# Add 5: [T,T,F,F,F,T,T,F,F,F,F,F]
# Add 11:[T,T,F,F,F,T,T,F,F,F,F,T]
# Add 5: [T,T,F,F,F,T,T,F,F,F,T,T]
# dp[11] = True
# Answer: True (subsets [1,5,5] and [11])
```

**LeetCode Problems:**
- 416. Partition Equal Subset Sum
- 494. Target Sum - [Solution](leet_code/dynamic_programming/494_target_sum.py)
- 1049. Last Stone Weight II
- 474. Ones and Zeroes
- 518. Coin Change II

### Kadane's Algorithm (Maximum Subarray)
**When to use:** Maximum/minimum subarray sum, maximum product subarray

```python
def max_subarray(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        current_sum = max(0, current_sum) + num  # Reset if negative
        max_sum = max(max_sum, current_sum)

    return max_sum
```

**Example: Maximum Subarray Sum**
```python
def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        # Reset to 0 if negative (start new subarray)
        current_sum = max(0, current_sum) + num
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example: nums = [-2,1,-3,4,-1,2,1,-5,4]
# num=-2: current=max(0,0)+(-2)=-2, max=-2
# num=1:  current=max(0,-2)+1=1, max=1
# num=-3: current=max(0,1)+(-3)=-2, max=1
# num=4:  current=max(0,-2)+4=4, max=4
# num=-1: current=max(0,4)+(-1)=3, max=4
# num=2:  current=max(0,3)+2=5, max=5
# num=1:  current=max(0,5)+1=6, max=6 (subarray: [4,-1,2,1])
# num=-5: current=max(0,6)+(-5)=1, max=6
# num=4:  current=max(0,1)+4=5, max=6
# Answer: 6
```

**LeetCode Problems:**
- 53. Maximum Subarray - [Solution](leet_code/array/53_max_sub_subarray.py)
- 918. Maximum Sum Circular Subarray
- 152. Maximum Product Subarray
- 978. Longest Turbulent Subarray
- 1191. K-Concatenation Maximum Sum

## Bit Manipulation Patterns

### Common Bit Operations
**When to use:** Finding single numbers, subset generation, optimization tricks

```python
# XOR properties: a ^ a = 0, a ^ 0 = a
# Useful for finding unique elements

# Check if bit is set
def is_bit_set(num, i):
    return (num & (1 << i)) != 0

# Set a bit
def set_bit(num, i):
    return num | (1 << i)

# Clear a bit
def clear_bit(num, i):
    return num & ~(1 << i)

# Toggle a bit
def toggle_bit(num, i):
    return num ^ (1 << i)

# Count set bits
def count_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count
```

**Example: Single Number (XOR)**
```python
def singleNumber(nums):
    result = 0

    # XOR all numbers: duplicates cancel out (a ^ a = 0)
    for num in nums:
        result ^= num

    return result

# Example: nums = [4,1,2,1,2]
# result = 0
# result ^= 4 -> result = 4 (binary: 100)
# result ^= 1 -> result = 5 (binary: 101)
# result ^= 2 -> result = 7 (binary: 111)
# result ^= 1 -> result = 6 (binary: 110)
# result ^= 2 -> result = 4 (binary: 100)
# Answer: 4 (only number appearing once)

# XOR properties:
# 1 ^ 1 = 0 (same numbers cancel)
# 2 ^ 2 = 0 (same numbers cancel)
# 4 ^ 0 = 4 (unique number remains)
```

**LeetCode Problems:**
- 136. Single Number - [Solution](leet_code/bit_manipulation/136_single_number.py)
- 268. Missing Number - [Solution](leet_code/bit_manipulation/268_missing_number.py)
- 191. Number of 1 Bits
- 338. Counting Bits
- 371. Sum of Two Integers

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

**Example: Kth Largest Element**
```python
def findKthLargest(nums, k):
    import heapq

    # Maintain min heap of size k
    # The root will be the kth largest
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        # Keep heap size at k by removing smallest
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]  # Smallest in heap = kth largest overall

# Example: nums = [3,2,1,5,6,4], k = 2
# Process 3: heap=[3]
# Process 2: heap=[2,3]
# Process 1: heap=[1,2,3], pop 1 -> heap=[2,3]
# Process 5: heap=[2,3,5], pop 2 -> heap=[3,5]
# Process 6: heap=[3,5,6], pop 3 -> heap=[5,6]
# Process 4: heap=[4,5,6], pop 4 -> heap=[5,6]
# Answer: 5 (2nd largest)
```

**LeetCode Problems:**
- 215. Kth Largest Element in an Array - [Solution](leet_code/heap/215_k_largest_element_heap.py)
- 347. Top K Frequent Elements - [Solution](leet_code/heap/347_top_k_frequent_elements.py)
- 692. Top K Frequent Words
- 973. K Closest Points to Origin
- 703. Kth Largest Element in a Stream - [Solution](leet_code/heap/703_kt_largest_element_stream.py)

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

**Example: Merge K Sorted Lists**
```python
def mergeKLists(lists):
    import heapq

    # Min heap: (value, list_index, node)
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))

    dummy = ListNode(0)
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next

        # Add next node from same list
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

# Example: lists = [[1,4,5],[1,3,4],[2,6]]
# Initial heap: [(1,0,node1), (1,1,node1'), (2,2,node2)]
# Pop (1,0,node1), add (4,0,node4): heap=[(1,1,node1'), (2,2,node2), (4,0,node4)]
# Pop (1,1,node1'), add (3,1,node3): heap=[(2,2,node2), (3,1,node3), (4,0,node4)]
# Continue merging...
# Answer: 1->1->2->3->4->4->5->6
```

**LeetCode Problems:**
- 23. Merge k Sorted Lists - [Solution](leet_code/linked_lists/23_merge_k_sorted_lists.py)
- 378. Kth Smallest Element in a Sorted Matrix
- 632. Smallest Range Covering Elements from K Lists
- 373. Find K Pairs with Smallest Sums
- 264. Ugly Number II

## Greedy Patterns

### Greedy Choice
**When to use:** Jump game, gas station, activity selection, interval scheduling

```python
# General greedy template
def greedy_solution(items):
    # Sort items based on greedy criterion
    items.sort(key=some_criterion)

    result = initial_value
    for item in items:
        if can_take(item):
            result = update(result, item)

    return result
```

**Example: Jump Game**
```python
def canJump(nums):
    max_reach = 0  # Furthest index we can reach

    for i in range(len(nums)):
        # If current position is unreachable
        if i > max_reach:
            return False

        # Update furthest reachable position
        max_reach = max(max_reach, i + nums[i])

        # Early exit if we can reach the end
        if max_reach >= len(nums) - 1:
            return True

    return True

# Example: nums = [2,3,1,1,4]
# i=0: max_reach = max(0, 0+2) = 2 (can reach index 2)
# i=1: max_reach = max(2, 1+3) = 4 (can reach index 4)
# i=2: max_reach >= 4 (reached end!)
# Answer: True

# Example: nums = [3,2,1,0,4]
# i=0: max_reach = max(0, 0+3) = 3
# i=1: max_reach = max(3, 1+2) = 3
# i=2: max_reach = max(3, 2+1) = 3
# i=3: max_reach = max(3, 3+0) = 3
# i=4: 4 > 3 (cannot reach index 4!)
# Answer: False
```

**Example: Gas Station**
```python
def canCompleteCircuit(gas, cost):
    # Check if solution exists
    if sum(gas) < sum(cost):
        return -1

    total = 0
    start = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]

        # If we can't reach next station, start from next
        if total < 0:
            total = 0
            start = i + 1

    return start

# Example: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# i=0: total = 1-3 = -2 (can't start here, start=1)
# i=1: total = 0 + 2-4 = -2 (can't start here, start=2)
# i=2: total = 0 + 3-5 = -2 (can't start here, start=3)
# i=3: total = 0 + 4-1 = 3 (good start!)
# i=4: total = 3 + 5-2 = 6 (still good)
# Answer: 3 (start at index 3)
```

**LeetCode Problems:**
- 55. Jump Game - [Solution](leet_code/dynamic_programming/55_jump_game.py)
- 45. Jump Game II
- 134. Gas Station
- 135. Candy
- 406. Queue Reconstruction by Height
- 621. Task Scheduler
- 763. Partition Labels

---

## Quick Pattern Recognition Guide

**See contiguous subarray/substring?** → Sliding Window or Prefix Sum
**See maximum/minimum subarray sum?** → Kadane's Algorithm
**See sorted array + find pair?** → Two Pointers
**See linked list cycle or middle?** → Fast & Slow Pointers
**See overlapping intervals?** → Merge Intervals
**See reverse linked list?** → In-Place Reversal
**See "find all combinations"?** → Backtracking
**See "optimize/min/max with subproblems"?** → Dynamic Programming
**See greedy choice (jump, gas, schedule)?** → Greedy
**See tree traversal?** → DFS or BFS
**See "shortest path" unweighted?** → BFS
**See "top K" or "Kth largest"?** → Heap
**See sorted + search?** → Binary Search
**See graph + dependencies?** → Topological Sort
**See connected components?** → Union Find or DFS
**See single/unique element?** → Bit Manipulation (XOR)
**See subset generation?** → Backtracking or Bit Manipulation
