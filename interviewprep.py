from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    # performs the BFS and writes to a var
    while queue:
        node = queue.popleft()

        if node not in visited:
            result.append(node)
            visited.add(node)

            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

    # Reaching here means we're done w/ BFS
    return result



#Shortest Path Function

def find_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            if node in graph:
                for neighbor in graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    return None


#Format Function

def format_bfs_result(bfs_result):
    return " - > ".join(bfs_result)


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
# What is the expected output?
# Perform BFS starting from node 'A'
""" 
    A
   / \
  B   C
 /|    \
D E     F

Answer must be formatted in "A -> B -> C ..." format

Find the shortest path between two nodes.
find shortest path between B and F
 """

# Example of using the BFS function
bfs_result = bfs(graph, 'A')
print("BFS Traversal:", " -> ".join(bfs_result))

# Example of using the shortest path function
shortest_path = find_shortest_path(graph, 'B', 'F')
formatted_shortest_path = format_bfs_result(shortest_path)
print("Shortest Path:", formatted_shortest_path)