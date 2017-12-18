from math import gcd
from collections import deque


def _connected(graph, origin, destination):
    # Use Breadth first search since from sample cases it appears destination isn't far from origin.
    # Might want depth first search if destination would be far from input or input is very large (dfs use less memory)
    q = deque([origin])     # queue with fast add/remove from either end that we can use as FIFO queue
    visited = set()

    while q:
        removed = q.popleft()
        for child in graph[removed]:
            if removed == destination:
                return True
            if child not in visited:
                q.append(child)
                visited.add(child)
    return False    # we finished search without finding a connection


def connectedCities(n, g, originCities, destinationCities):
    graph = {x: [] for x in range(1, n+1)}       # init an adjacency list representation of the graph

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # print('i={} j={}'.format(i,j))
            if gcd(i,j) > g:
                graph[i].append(j)              # bidirectional edges so add i->j and j->i
                graph[j].append(i)
    # print(graph)

    ans = []
    for i in range(len(originCities)):
        if _connected(graph, originCities[i], destinationCities[i]):
            ans.append(1)
        else:
            ans.append(0)

    return ans

print(connectedCities(6, 0, [1,4,3,6], [3,6,2,5]))
print(connectedCities(6, 1, [1,2,4,6], [3,3,3,4]))
# print(connectedCities(100, 2, [3], [23]))

