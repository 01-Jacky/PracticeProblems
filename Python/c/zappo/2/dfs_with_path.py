
def dfs_no_path(graph, start, goal):
    stack = []
    visited = set()

    stack.append(start)

    while stack:
        node = stack.pop()

        if node not in visited:
            if node == goal:            # Goal check
                return True

            visited.add(node)           # Mark visited so we don't redo it

            for child in graph[node]:               # add children
                stack.append(child)

    return False


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

g2 = {"a": ["d"],
     "b": ["c"],
     "c": ["b", "c", "d", "e"],
     "d": ["a", "c"],
     "e": ["c"],
     "f": []
     }

start = 'a'
goal = 'b'
found = dfs(g2, start, goal)

print(found)