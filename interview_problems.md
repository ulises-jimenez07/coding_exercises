# Algorithm Patterns — Problem Tracker

---

## Two Pointers

**Core idea:** Use two pointers that start at opposite ends of a sorted (or arbitrary) array and move toward each other. Each step eliminates a subset of candidates in O(1), reducing overall complexity from O(n^2) to O(n).

**When to apply:**
- Finding pairs or triplets that sum to a target
- Eliminating impossible candidates based on sorted order
- Moving or partitioning elements in place

**Pattern — opposite direction:**
```python
left, right = 0, len(arr) - 1
while left < right:
    if condition_met:
        # found
    elif need_larger:
        left += 1
    else:
        right -= 1
```

**Key insight:** When the current sum exceeds the target, the right pointer cannot form any valid pair with elements to its left since they are all smaller, so move `right` left. Symmetrically, if the sum is too small, advance `left`.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 11 | Container With Most Water | Medium | done | [solution](leet_code/array/11_container_wiht_most_water.py) |
| 167 | Two Sum II — Sorted Array | Medium | done | [solution](leet_code/array/167_two_sum_2_sorted.py) |
| 15 | 3Sum | Medium | done | [solution](leet_code/array/15_3sum.py) |
| — | Triangle Numbers | Medium | done | [solution](leet_code/math/triangle_numbers.py) |
| 283 | Move Zeroes | Easy | done | [solution](leet_code/array/283_move_zeros.py) |
| 75 | Sort Colors | Medium | done | [solution](leet_code/sorting/75_sort_colors.py) |
| 42 | Trapping Rain Water | Hard | done | [solution](leet_code/queues_stacks/42_trapping_rain_water.py) |

**Container With Most Water — hint:**
Start with the widest container (pointers at both ends). Moving the taller wall inward can never increase the area because width shrinks and height stays capped by the shorter wall, so always move the shorter pointer.

**3Sum — hint:**
Sort first. Fix one element, then use two pointers on the remaining subarray. Skip duplicates after fixing and after finding a triplet to avoid duplicate results.

**Trapping Rain Water — hint:**
The water above index `i` is `min(max_left, max_right) - height[i]`. With two pointers, maintain running `max_left` and `max_right`; whichever side has the smaller max constrains the water level and can be processed immediately.

---

## Sliding Window

**Core idea:** Maintain a contiguous window over an array. Instead of recomputing from scratch, slide the window by adding one element on the right and removing one on the left. This gives O(n) over O(n^2) for subarray and substring problems.

**When to apply:**
- Fixed-size subarray problems such as max sum of k elements
- Longest subarray or substring satisfying a constraint (expand right, shrink left when invalid)
- Shortest subarray or substring satisfying a constraint (expand right until valid, then shrink left)

**Pattern — fixed size:**
```python
window_sum = sum(nums[:k])
for right in range(k, len(nums)):
    window_sum += nums[right] - nums[right - k]
    ans = max(ans, window_sum)
```

**Pattern — flexible (longest):**
```python
left = 0
for right in range(len(s)):
    # add s[right] to window
    while invalid(window):
        # remove s[left], left += 1
    ans = max(ans, right - left + 1)
```

**Pattern — flexible (shortest):**
```python
left = 0
for right in range(len(nums)):
    # add nums[right] to window
    while valid(window):
        ans = min(ans, right - left + 1)
        # remove nums[left], left += 1
```

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 643 | Maximum Sum Subarray of Size K | Easy | done | [solution](leet_code/array/643_max_avg_subarray.py) |
| 1423 | Max Points You Can Obtain From Cards | Medium | todo | — |
| 2461 | Max Sum of Distinct Subarrays Length k | Medium | done | [solution](leet_code/array/2461_max_sum_distinct_subarray_length_k.py) |
| 3 | Longest Substring Without Repeating Characters | Medium | done | [solution](leet_code/array/3_longest_substring_withouth_repeating.py) |
| 424 | Longest Repeating Character Replacement | Medium | done | [solution](leet_code/array/424_longest_repeating_char_replacement.py) |

**Max Points from Cards — hint:**
You take cards from either end, so the cards you do not take form a contiguous middle window. Minimize the sum of that window of size `n - k` to maximize the score.

**Longest Repeating Character Replacement — hint:**
Track the count of the most frequent character in the window (`max_count`). The window is valid when `window_size - max_count <= k`. You never need to shrink the window smaller than the historical best because that cannot improve the answer.

---

## Intervals

**Core idea:** Sort intervals strategically, then iterate once to detect overlaps, merge, or count conflicts.

**When to apply:**
- Scheduling and meeting-room problems
- Merging or inserting overlapping ranges
- Counting minimum resources needed

**Sort by start time** to detect and merge overlaps:
```python
intervals.sort(key=lambda x: x[0])
merged = []
for interval in intervals:
    if not merged or interval[0] > merged[-1][1]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])
```

**Sort by end time** to greedily maximize non-overlapping intervals. Always keep the interval that ends earliest, which frees room for more intervals later.

**Key insight — overlap detection:** Two intervals `[a, b]` and `[c, d]` overlap when `c <= b`, meaning the second starts before the first ends. The merged interval ends at `max(b, d)`.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 252 | Can Attend Meetings | Easy | done | [solution](leet_code/intervals/252_meeting_rooms.py) |
| 57 | Insert Interval | Medium | done | [solution](leet_code/intervals/57_insert_interval.py) |
| 435 | Non-Overlapping Intervals | Medium | done | [solution](leet_code/intervals/435_non_overlapping_intervals.py) |
| 56 | Merge Intervals | Medium | done | [solution](leet_code/intervals/56_merged_intervals.py) |
| — | Employee Free Time | Hard | todo | — |

**Insert Interval — hint:**
Walk through existing intervals in three phases: add all that end before the new interval starts, merge all that overlap with the new interval by expanding its bounds, then add everything remaining.

**Non-Overlapping Intervals — hint:**
Sort by end time. Greedily keep intervals that end earliest since this leaves the most room for subsequent intervals. Count the ones you must remove.

**Employee Free Time — hint:**
Flatten all employees' schedules into one list, sort by start time, then find the gaps between merged intervals. Those gaps are the free time.

---

## Stack

**Core idea:** Last-in, first-out. The most recently opened item closes first. Stacks are ideal for matching nested structures and tracking nearest relationships.

**When to apply:**
- Validating or computing over nested or paired structures like parentheses
- Nearest-greater-element style problems (monotonic stack)
- Undo and history semantics

**Monotonic stack pattern** for next greater element:
```python
stack = []  # stores indices
for i, val in enumerate(nums):
    while stack and nums[stack[-1]] < val:
        idx = stack.pop()
        result[idx] = val  # val is the next greater for idx
    stack.append(i)
```

**Key insight:** A monotonic stack maintains elements in sorted order by popping anything that violates the ordering before each push. This finds nearest-greater or nearest-smaller relationships in O(n).

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 20 | Valid Parentheses | Easy | done | [solution](leet_code/queues_stacks/20_valid_parenthesis.py) |
| 394 | Decode String | Medium | done | [solution](leet_code/queues_stacks/394_decode_string.py) |
| 32 | Longest Valid Parentheses | Hard | done | [solution](leet_code/queues_stacks/32_longest_valid_parenthesis.py) |
| 739 | Daily Temperatures | Medium | done | [solution](leet_code/queues_stacks/739_daily_temperatures.py) |
| 84 | Largest Rectangle in Histogram | Hard | done | [solution](leet_code/queues_stacks/84_largest_rectangle_in_histogram.py) |

**Decode String — hint:**
When you hit `[`, push the current string and the current repeat count onto the stack. When you hit `]`, pop the count and previous string, then append the current string repeated `count` times.

**Longest Valid Parentheses — hint:**
Keep a stack of indices. Push the index of `(`; when you see `)`, pop — if the stack is empty, push the current index as a new base. The longest valid length at each step is `current_index - stack[-1]`.

**Daily Temperatures — hint:**
Use a monotonic decreasing stack of indices. When a warmer day is found, pop all cooler days and record the wait. Elements remaining in the stack at the end have no warmer day ahead.

**Largest Rectangle in Histogram — hint:**
Use a monotonic increasing stack of indices. When a shorter bar is encountered, pop taller bars and compute the rectangle using the popped bar's height times the distance back to the new stack top. Append a sentinel value of 0 at the end to flush everything.

---

## Linked List

**Core idea:** Linked list problems usually reduce to pointer manipulation. Three fundamental techniques: fast/slow pointers for cycle detection and finding the middle, three-pointer reversal, and dummy nodes to simplify edge cases at the head.

**When to apply:**
- Detecting or locating cycles
- Finding the middle or k-th-from-end node
- Reversing or reordering a list

**Fast/slow pointer:**
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is at the middle
```

**In-place reversal:**
```python
prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev, curr = curr, nxt
return prev
```

**Dummy node pattern:**
```python
dummy = ListNode(0)
dummy.next = head
# manipulate using dummy; return dummy.next
```

**Key insight — dummy node:** Avoids special-casing when the operation might remove or insert at the head. Return `dummy.next` at the end.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 141 | Linked List Cycle | Easy | done | [solution](leet_code/linked_lists/141_is_cycle_linked_list.py) |
| 234 | Palindrome Linked List | Easy | done | [solution](leet_code/linked_lists/234_palindrome_linkded_list.py) |
| 19 | Remove Nth Node From End | Medium | done | [solution](leet_code/linked_lists/19_remove_nth_node_linked_list.py) |
| 143 | Reorder List | Medium | done | [solution](leet_code/linked_lists/143_reorder_list.py) |
| 24 | Swap Nodes in Pairs | Medium | done | [solution](leet_code/linked_lists/24_swap_nodes_pairs.py) |

**Palindrome Linked List — hint:**
Find the middle using fast/slow, reverse the second half in place, then compare both halves node by node. O(n) time, O(1) space.

**Remove Nth From End — hint:**
Use two pointers separated by `n` nodes. When the fast pointer hits the end, the slow pointer is right before the node to remove. Use a dummy node to handle removing the head.

**Reorder List — hint:**
Three steps: find the middle, reverse the second half, then merge the two halves by alternating nodes.

---

## Binary Search

**Core idea:** Reduce the search space by half each iteration. Works on any monotonic function, not just sorted arrays. If you can express "is mid a valid answer?" as a yes/no monotonic predicate, binary search applies.

**When to apply:**
- Searching in sorted arrays
- Minimize-the-maximum or maximize-the-minimum optimization problems
- Any problem where the feasibility of a candidate answer is monotonic

**Template:**
```python
left, right = lo, hi
while left <= right:
    mid = (left + right) // 2
    if feasible(mid):
        ans = mid
        right = mid - 1   # look for smaller valid answer
    else:
        left = mid + 1
```

**Key insight — binary search on the answer:** For problems like "minimum capacity to ship in D days," define `feasible(cap)` as "can we ship everything in D days with capacity cap?" This predicate is monotone, so binary search works over the capacity range.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 875 | Koko Eating Bananas | Medium | done | [solution](leet_code/binary_search/875_koko_eating_bananas.py) |
| 33 | Search in Rotated Sorted Array | Medium | done | [solution](leet_code/binary_search/33_find_rotated_array.py) |

**Koko Eating Bananas — hint:**
Binary search on the eating speed `k` in the range `[1, max(piles)]`. For each candidate speed, check if Koko can finish all piles in `h` hours: `sum(ceil(pile/k) for pile in piles) <= h`.

**Search in Rotated Sorted Array — hint:**
After computing `mid`, determine which half is sorted by comparing `nums[left]` to `nums[mid]`. The target must lie in the sorted half if it falls within that range; otherwise search the other half.

---

## Heap

**Core idea:** A heap gives O(1) access to the min or max element and O(log n) insertion and deletion. Use it when you need to repeatedly extract the extremum from a changing set.

**When to apply:**
- Top-K problems: k largest, k most frequent, k closest
- Merging k sorted streams
- Running median using two heaps

**Python note:** `heapq` is a min-heap. Negate values to simulate a max-heap.

**Top-K pattern using a min-heap of size k:**
```python
import heapq
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)  # evict the smallest
# heap contains the k largest; heap[0] is the k-th largest
```

**Key insight:** A min-heap of size k holding the k largest elements evicts the smallest among them when full. The root (`heap[0]`) is always the k-th largest overall.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 215 | Kth Largest Element in an Array | Medium | done | [solution](leet_code/heap/215_k_largest_element_heap.py) |
| 973 | K Closest Points to Origin | Medium | done | [solution](leet_code/heap/973_k_closest_point_to_origin.py) |
| 658 | Find K Closest Elements | Medium | done | [solution](leet_code/binary_search/658_find_k_closest.py) |
| 23 | Merge K Sorted Lists | Hard | done | [solution](leet_code/linked_lists/23_merge_k_sorted_lists.py) |

**K Closest Points to Origin — hint:**
Use a max-heap of size k keyed by squared distance (`x*x + y*y`; no need for sqrt). When the heap exceeds size k, pop the farthest. What remains is the k closest.

**Merge K Sorted Lists — hint:**
Push the head of each list into a min-heap as `(val, list_id, node)`. Each time you pop the minimum node, push its successor if one exists. Continue until the heap is empty.

---

## Depth-First Search

**Core idea:** Explore as deep as possible along one branch before backtracking. In trees this is the natural recursive traversal. In graphs, maintain a `visited` set to avoid cycles.

**When to apply:**
- Tree traversals: path sums, depths, diameters
- Graph connectivity, cycle detection, topological reasoning
- Grid flood-fill and island counting

**Tree DFS template:**
```python
def dfs(node):
    if not node:
        return base_value
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(left, right, node.val)
```

**Graph DFS template:**
```python
def dfs(node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)
```

**Key insight — return vs. update global:** Some tree problems like diameter and tilt need a global variable updated at each node while returning a different value up the call stack. Keep these two roles separate.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 104 | Maximum Depth of Binary Tree | Easy | done | [solution](leet_code/trees/104_max_depth.py) |
| 112 | Path Sum | Easy | done | [solution](leet_code/trees/112_path_sum.py) |
| 98 | Validate Binary Search Tree | Medium | done | [solution](leet_code/trees/98_validate_BST.py) |
| 563 | Binary Tree Tilt | Easy | done | [solution](leet_code/trees/563_binary_tree_tilt.py) |
| 543 | Diameter of a Binary Tree | Easy | done | [solution](leet_code/trees/543_diameter_binary_tree.py) |
| 113 | Path Sum II | Medium | done | [solution](leet_code/trees/113_path_sum_2.py) |
| 687 | Longest Univalue Path | Medium | done | [solution](leet_code/trees/687_longest_univalue_path.py) |
| 133 | Clone Graph | Easy | done | [solution](leet_code/graph/133_clone_graph.py) |
| 261 | Graph Valid Tree | Medium | done | [solution](leet_code/graph/261_valid_tree.py) |
| 733 | Flood Fill | Easy | done | [solution](leet_code/graph/733_flood_fill.py) |
| 200 | Number of Islands | Medium | done | [solution](leet_code/graph/200_number_island.py) |
| 130 | Surrounded Regions | Medium | done | [solution](leet_code/graph/130_surronding_regions.py) |
| 417 | Pacific Atlantic Water Flow | Medium | done | [solution](leet_code/graph/417_pacific_atlantic.py) |

**Diameter of Binary Tree — hint:**
At each node, the candidate diameter is `left_depth + right_depth`. Return `max(left_depth, right_depth) + 1` up the call stack as the depth contribution, but update a global `max_diameter` in place.

**Validate BST — hint:**
Pass `(min_val, max_val)` bounds down the recursion. The left subtree must stay below `node.val`; the right subtree must stay above. Initialize bounds to negative and positive infinity.

**Surrounded Regions — hint:**
Any 'O' reachable from a border cannot be flipped. DFS from all border 'O' cells and mark them safe, then flip all remaining 'O' to 'X' and restore the safe cells.

**Pacific Atlantic Water Flow — hint:**
Reverse the flow direction: BFS from all Pacific-border cells to find which cells can drain there, and do the same for the Atlantic. The answer is the intersection of both reachable sets.

---

## Breadth-First Search

**Core idea:** Explore level by level using a queue. Guarantees the shortest path in unweighted graphs. In trees it processes nodes by depth.

**When to apply:**
- Shortest path in unweighted graphs or grids
- Level-order tree traversals
- Problems where all nodes at distance d must be processed before distance d+1

**Template:**
```python
from collections import deque
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

**Level-by-level template:**
```python
queue = deque([root])
while queue:
    for _ in range(len(queue)):   # process one full level
        node = queue.popleft()
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
```

**Key insight:** BFS on a grid treats each cell as a graph node with up to 4 neighbors. Multi-source BFS starts from multiple cells simultaneously, which is useful for nearest-distance problems like 01-Matrix and Rotting Oranges.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 102 | Level Order Traversal | Easy | done | [solution](leet_code/queues_stacks/102_binary_tree_level_order_traversal.py) |
| 199 | Binary Tree Right Side View | Medium | done | [solution](leet_code/trees/199_binary_tree_right.py) |
| 103 | Zigzag Level Order | Medium | done | [solution](leet_code/queues_stacks/103_binary_tree_zigzag.py) |
| 662 | Maximum Width of Binary Tree | Medium | done | [solution](leet_code/trees/662_maximum_width_binary_tree.py) |
| — | Minimum Knight Moves | Medium | todo | — |
| 994 | Rotting Oranges | Medium | done | [solution](leet_code/graph/994_rotting_oranges.py) |
| 542 | 01-Matrix | Medium | done | [solution](leet_code/graph/542_01_matrix.py) |
| 815 | Bus Routes | Hard | done | [solution](leet_code/graph/815_bus_routes.py) |

**Maximum Width of Binary Tree — hint:**
Assign indices to nodes (root = 1; left child of i = 2i, right = 2i+1). The level width is `last_index - first_index + 1`. Normalize by subtracting the first index of each level to avoid integer overflow.

**Rotting Oranges — hint:**
Multi-source BFS: add all initially rotten oranges to the queue at time 0. Spread rot level by level where each level equals one minute. If any fresh orange remains unreachable after BFS, return -1.

**Bus Routes — hint:**
Model it as a graph where nodes are routes, not stops. Two routes are connected if they share a stop. BFS on routes rather than stops to find the minimum number of buses needed.

---

## Backtracking

**Core idea:** DFS through a solution space tree. At each node, make a choice, recurse, then undo the choice. Prune branches early when they cannot lead to valid solutions.

**When to apply:**
- Generating all subsets, permutations, or combinations
- Constraint-satisfaction problems like N-Queens or Sudoku
- Grid search with state such as Word Search

**Template:**
```python
def backtrack(start, current):
    if is_solution(current):
        results.append(list(current))
        return
    for choice in choices(start):
        if not is_valid(choice, current):
            continue          # prune
        current.append(choice)
        backtrack(next_start, current)
        current.pop()         # undo
```

**Key insight — pruning:** The more aggressively you prune invalid branches, the faster the search. Sorting the input first enables early termination — for example, stop when a candidate exceeds the remaining target in Combination Sum.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 79 | Word Search | Medium | done | [solution](leet_code/back_tracking/79_word_search.py) |
| 78 | Subsets | Medium | done | [solution](leet_code/back_tracking/78_subset.py) |
| 22 | Generate Parentheses | Medium | done | [solution](leet_code/back_tracking/22_generate_parenthesis.py) |
| 39 | Combination Sum | Medium | done | [solution](leet_code/back_tracking/39_combination_sum.py) |

**Word Search — hint:**
For each cell matching `word[0]`, start DFS. Mark the current cell with a placeholder before recursing and restore it after — that is the backtracking step. Check bounds and character match before descending.

**Generate Parentheses — hint:**
Track `open` and `close` counts. You can add `(` when `open < n`, and `)` when `close < open`. Only complete strings where both counts equal `n` are added to results.

**Combination Sum — hint:**
Sort candidates. At each step, try each candidate from `start` onward allowing reuse. Prune when the candidate exceeds the remaining target. Pass the same index `i` rather than `i+1` to allow repetition.

---

## Graphs — Topological Sort

**Core idea:** Topological sort orders nodes of a directed acyclic graph so every edge points from an earlier node to a later one. Detect cycles by checking if all nodes were processed — any node with remaining in-degree greater than zero indicates a cycle.

**When to apply:**
- Dependency resolution and course prerequisites
- Build-order problems
- Detecting cycles in directed graphs

**Kahn's Algorithm:**
```python
from collections import deque
in_degree = [0] * n
for u, v in edges:
    graph[u].append(v)
    in_degree[v] += 1

queue = deque(i for i in range(n) if in_degree[i] == 0)
order = []
while queue:
    node = queue.popleft()
    order.append(node)
    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

return order if len(order) == n else []  # empty list means a cycle exists
```

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 207 | Course Schedule | Medium | done | [solution](leet_code/graph/207_course_schedule.py) |
| 210 | Course Schedule II | Medium | done | [solution](leet_code/graph/210_course_schedule_2.py) |

**Course Schedule — hint:**
Build an adjacency list and in-degree array. BFS from all nodes with in-degree 0. If the number of processed courses equals `numCourses`, return True; otherwise a cycle prevents completion.

**Course Schedule II — hint:**
Same as above but collect the BFS processing order. That order is a valid course sequence. Return it if its length equals `numCourses`, otherwise return an empty list.

---

## Dynamic Programming

**Core idea:** Break a problem into overlapping subproblems and store results to avoid recomputation. Two styles: top-down with memoization and bottom-up with tabulation.

**When to apply:**
- Optimal substructure: the global optimum is built from subproblem optima
- Overlapping subproblems: the same state is computed multiple times
- Classic signals: "count the ways," "minimum or maximum," "is it possible?"

**Bottom-up template:**
```python
dp = [base_case] * (n + 1)
for i in range(1, n + 1):
    dp[i] = transition(dp[i-1], dp[i-2], ...)
return dp[n]
```

**Key insight — state definition:** The hardest part is defining what `dp[i]` or `dp[i][j]` represents. Write it out in plain English before writing code. The recurrence follows naturally from that definition.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 338 | Counting Bits | Easy | done | [solution](leet_code/bit_manipulation/338_counting_bits.py) |
| 91 | Decode Ways | Medium | done | [solution](leet_code/dynamic_programming/91_decoded_ways.py) |
| 62 | Unique Paths | Medium | done | [solution](leet_code/dynamic_programming/62_unique_paths.py) |
| 221 | Maximal Square | Medium | done | [solution](leet_code/dynamic_programming/221_maximal_square.py) |
| 300 | Longest Increasing Subsequence | Medium | done | [solution](leet_code/dynamic_programming/300_longest_increasing_subsequence.py) |
| 139 | Word Break | Medium | todo | — |
| 1235 | Maximum Profit in Job Scheduling | Hard | todo | — |

**Counting Bits — hint:**
`dp[i] = dp[i >> 1] + (i & 1)`. Shifting right drops the last bit; `i & 1` tells you whether that dropped bit was 1.

**Decode Ways — hint:**
`dp[i]` is the number of ways to decode `s[:i]`. Add `dp[i-1]` if `s[i-1]` is non-zero (single digit); add `dp[i-2]` if `s[i-2:i]` is between 10 and 26 (two-digit decode).

**Maximal Square — hint:**
`dp[i][j]` is the side length of the largest all-ones square whose bottom-right corner is at `(i, j)`. If `matrix[i][j] == '1'`: `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`.

**Word Break — hint:**
`dp[i]` is True if `s[:i]` can be segmented. For each `i`, check all `j < i`: if `dp[j]` is True and `s[j:i]` is in the word set, set `dp[i] = True`.

**Maximum Profit in Job Scheduling — hint:**
Sort jobs by end time. For each job, binary search to find the latest job that ends before this one starts, then `dp[i] = max(dp[i-1], profit[i] + dp[prev])`.

---

## Greedy Algorithms

**Core idea:** Make the locally optimal choice at each step and trust it leads to the global optimum. Unlike dynamic programming, there is no looking back — each decision is final.

**When to apply:**
- The greedy choice property holds: local optimum leads to global optimum
- Sorting by some criterion enables a clear scan strategy
- As a counter-check, ask whether a greedy choice can ever be corrected later; if not, DP may be needed instead

**Key insight:** Find a potential counterexample. If you cannot, greedy likely works. Common signals are "earliest deadline," "smallest remaining," and "maximize coverage."

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 121 | Best Time to Buy and Sell Stock | Easy | done | [solution](leet_code/dynamic_programming/121_best_time_buy_sell.py) |
| 134 | Gas Station | Medium | done | [solution](leet_code/greedy/134_gas_station.py) |
| 55 | Jump Game | Medium | done | [solution](leet_code/greedy/55_jump_game.py) |

**Best Time to Buy and Sell Stock — hint:**
Track the minimum price seen so far. At each day, the best profit if selling today is `price - min_so_far`. Update the global max profit and the running minimum in one pass.

**Gas Station — hint:**
If total gas is at least total cost, a solution exists. The starting station is the one after the last point where the cumulative tank drops to zero — reset the tank and update the starting candidate there.

**Jump Game — hint:**
Track `max_reach`, the farthest index reachable so far. At each index `i`, if `i > max_reach` you are stuck. Otherwise update `max_reach = max(max_reach, i + nums[i])`. Return whether `max_reach` reaches the last index.

---

## Trie

**Core idea:** A tree where each path from root to a marked node spells a word. Nodes with common prefixes share the same path, making prefix queries O(L) instead of O(n * L).

**When to apply:**
- Autocomplete and prefix search
- Word existence and prefix checking
- Replacing words by their shortest root

**Node structure:**
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
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
```

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 208 | Implement Trie Methods | Medium | done | [solution](leet_code/trie/208_implement_trie.py) |
| 648 | Replace Words (Prefix Matching) | Medium | done | [solution](leet_code/trie/648_replace_words.py) |

**Implement Trie — hint:**
Keep a `children` dict and an `is_end` bool at each node. `insert` adds nodes along the path; `search` traverses and checks `is_end`; `startsWith` traverses and returns True if the path exists regardless of `is_end`.

**Replace Words — hint:**
Insert all roots into the trie. For each word in the sentence, walk the trie character by character and return the prefix the moment you hit an `is_end` node. If no root matches, keep the original word.

---

## Prefix Sum

**Core idea:** Precompute cumulative sums so any subarray sum from index `i` to `j` is retrieved in O(1) as `prefix[j+1] - prefix[i]`.

**When to apply:**
- Repeated subarray or substring sum queries
- Counting subarrays with a target sum, combined with a hash map

**Build prefix array:**
```python
prefix = [0] * (len(nums) + 1)
for i, num in enumerate(nums):
    prefix[i + 1] = prefix[i] + num
# sum of nums[i:j] = prefix[j] - prefix[i]
```

**Hash map pattern for counting subarrays:**
```python
count = 0
curr_sum = 0
seen = {0: 1}   # prefix sum -> frequency
for num in nums:
    curr_sum += num
    count += seen.get(curr_sum - k, 0)
    seen[curr_sum] = seen.get(curr_sum, 0) + 1
```

**Key insight:** Instead of storing the prefix array explicitly, use a hash map of running sums. For each new running sum `s`, look up `s - k` — if you have seen it before, those subarrays sum to `k`.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 2062 | Count Vowels in Substrings | Medium | todo | — |
| 560 | Subarray Sum Equals K | Medium | done | [solution](leet_code/prefix_sum/560_subarray_sum_equals_k.py) |

**Count Vowels in Substrings — hint:**
Build a prefix-vowel-count array. For each query `[start, end]`, the vowel count is `prefix[end + 1] - prefix[start]`. Build in O(n) and answer each query in O(1).

---

## Matrices

**Core idea:** Treat the matrix as a graph where each cell has up to 4 neighbors, or use index arithmetic for rotation and spiral traversal. Many matrix problems reduce to a DFS/BFS or a careful boundary-shrinking traversal.

**When to apply:**
- Grid traversal such as flood fill and island counting
- In-place rotation or transformation
- Row and column zeroing

**In-place rotation 90 degrees clockwise:**
```python
# Step 1: transpose — swap matrix[i][j] with matrix[j][i]
# Step 2: reverse each row
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for row in matrix:
    row.reverse()
```

**Spiral traversal:** Maintain four boundaries (`top`, `bottom`, `left`, `right`). Traverse each boundary layer, then shrink inward.

### Problems

| # | Problem | Difficulty | Status | Solution |
|---|---------|-----------|--------|----------|
| 54 | Spiral Matrix | Medium | done | [solution](leet_code/array/54_spiral_matrix.py) |
| 48 | Rotate Image | Medium | done | [solution](leet_code/array/48_rotate_image.py) |
| 73 | Set Matrix Zeroes | Medium | done | [solution](leet_code/array/73_set_matrix_zeros.py) |

**Rotate Image — hint:**
Two steps in place: transpose the matrix by swapping `[i][j]` with `[j][i]`, then reverse each row. This achieves a 90-degree clockwise rotation without extra space.

**Set Matrix Zeroes — hint:**
First pass: record which rows and columns contain a zero. Second pass: zero out those rows and columns. To do it in O(1) space, use the first row and first column as markers, but handle them separately to avoid conflicts.

**Spiral Matrix — hint:**
Use four boundary pointers and traverse right, down, left, up in sequence. After each direction, shrink the corresponding boundary inward and check if boundaries have crossed before continuing.
