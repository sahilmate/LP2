def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:  # Recursive DFS call
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited1 = set()  # To keep track of DFS visited nodes
    visited2 = set()  # To keep track of BFS visited nodes
    queue = []        # For BFS
    n = int(input("Enter number of nodes: "))
    graph = {}

    for i in range(1, n + 1):
        graph[i] = []  # Initialize empty adjacency list
        edges = int(input(f"Enter number of edges for node {i}: "))
        for j in range(edges):
            node = int(input(f"Enter edge {j+1} for node {i}: "))
            graph[i].append(node)

    start_node = int(input("Enter the starting node for traversal: "))

    print("\nThe following is DFS traversal:")
    dfs(visited1, graph, start_node)
    print("\nThe following is BFS traversal:")
    bfs(visited2, graph, start_node, queue)

if __name__ == "__main__":
    main()
    