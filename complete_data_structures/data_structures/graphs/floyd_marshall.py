"""This module implements the Floyd-Warshall algorithm."""

INF = 9999


# Printing the solution
def print_solution(num_vertices, distance):
    """Prints the solution matrix for Floyd-Warshall algorithm."""
    for i in range(num_vertices):
        for j in range(num_vertices):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


def floyd_warshall(num_vertices, graph):
    """Implements the Floyd-Warshall algorithm to find all-pairs shortest paths."""
    distance = graph
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    print_solution(num_vertices, distance)


graph_matrix = [[0, 8, INF, 1], [INF, 0, 1, INF], [4, INF, 0, INF], [INF, 2, 9, 1]]

floyd_warshall(4, graph_matrix)
