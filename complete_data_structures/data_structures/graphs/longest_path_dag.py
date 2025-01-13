def longest_path_length(graph):
    """
    Calculates the length of the longest path in a Directed Acyclic Graph (DAG).

    Args:
    graph: A dictionary representing the graph where keys are nodes and
            values are lists of their adjacent nodes.

    Returns:
    The length of the longest path in the graph.
    """

    def dfs(node, visited, dp):
        """
        Performs Depth First Search (DFS) to calculate the longest path
        starting from a given node.

        Args:
        node: The current node being visited.
        visited: A set to keep track of visited nodes to avoid cycles.
        dp: A dictionary to store the longest path lengths for each node.

        Returns:
        The length of the longest path starting from the given node.
        """
        if node in dp:
            return dp[node]
        visited.add(node)
        max_length = 0
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                max_length = max(max_length, dfs(neighbor, visited, dp))
        dp[node] = 1 + max_length  # 1 for the current node
        return dp[node]

    longest_path = 0
    dp = {}  # Memoization for dynamic programming
    for node in graph:
        visited = set()
        longest_path = max(longest_path, dfs(node, visited, dp))
    return longest_path


# Example usage:
graph = {0: [1, 2], 1: [3], 2: [3], 3: [4], 4: []}

result = longest_path_length(graph)
print("Length of the longest path:", result)  # Output: 4
