class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find_leader(self, x):
        if self.parent[x] == x:
            return x
        return self.find_leader(self.parent[x])

    def find_leader_with_path_compression(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find_leader_with_path_compression(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        x_leader = self.find_leader_with_path_compression(x)
        y_leader = self.find_leader_with_path_compression(y)

        if x_leader != y_leader:
            if self.rank[x_leader] > self.rank[y_leader]:
                self.parent[y_leader] = x_leader
            elif self.rank[y_leader] > self.rank[x_leader]:
                self.parent[x_leader] = y_leader
            else:
                self.parent[y_leader] = x_leader
                self.rank[x_leader] += 1

    def is_same(self, x, y):
        return self.find_leader_with_path_compression(x) == self.find_leader_with_path_compression(y)

# Example 1: Basic Operations
print("--- Example 1: Basic Operations ---")
dsj = DisjointSet(5)
print(f"Initial parent array: {dsj.parent}") # Output: [0, 1, 2, 3, 4]
print(f"Are 1 and 4 in the same set? {dsj.is_same(1, 4)}") # Output: False

dsj.merge(1, 4)
print(f"After merging 1 and 4, parent array: {dsj.parent}") # Output: [0, 4, 2, 3, 4] or [0, 1, 2, 3, 1]
print(f"Are 1 and 4 in the same set? {dsj.is_same(1, 4)}") # Output: True

dsj.merge(2, 3)
print(f"After merging 2 and 3, parent array: {dsj.parent}") # Output: e.g., [0, 4, 3, 3, 4]
print(f"Are 2 and 3 in the same set? {dsj.is_same(2, 3)}") # Output: True

dsj.merge(1, 3)
# The set of {1, 4} will merge with the set of {2, 3}
print(f"After merging 1 and 3, parent array: {dsj.parent}") # Example output: [0, 4, 3, 4, 4]
print(f"Are 2 and 4 in the same set? {dsj.is_same(2, 4)}") # Output: True (since 1, 2, 3, and 4 are now connected)

print("\n" + "-"*35 + "\n")

# Example 2: Using the `find_leader` with path compression
print("--- Example 2: Path Compression in action ---")
dsj_pc = DisjointSet(6)
dsj_pc.parent = [0, 0, 1, 2, 3, 4]
# Tree structure: 5 -> 4 -> 3 -> 2 -> 1 -> 0

print(f"Initial parent array: {dsj_pc.parent}") # Output: [0, 0, 1, 2, 3, 4]
print(f"Leader of 5 (before compression): {dsj_pc.find_leader(5)}") # Traverses the chain to find 0
print(f"Parent array after find_leader: {dsj_pc.parent}") # Parent array is unchanged

print(f"Leader of 5 (with path compression): {dsj_pc.find_leader_with_path_compression(5)}") # Finds 0
print(f"Parent array after find_leader_with_path_compression: {dsj_pc.parent}") 
# Output: [0, 0, 0, 0, 0, 0] or similar. All nodes now point directly to the root (0).