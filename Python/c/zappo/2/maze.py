def dfs_path(graph, start, goal):
    stack = []
    visited = set()

    stack.append((start, [start]))  # Tuple (node, list consisting path to node)

    while stack:
        (node, path) = stack.pop()

        if node not in visited:
            if node == goal:  # Goal check
                return path

            visited.add(node)  # Mark visited so we don't redo it

            for child in graph[node]:  # add children
                stack.append((child, path + [child]))

    return False, None



import collections

def _valid_neighbors(i, j, w, h, maze, visited):
    if i < 0 or i > h-1:
        return []
    if j < 0 or j > w-1:
        return []

    valid = []
    if (i-1,j) not in visited and i-1 >= 0 and maze[i-1][j] != '@':   # up
        valid.append( ((i-1,j), 'U') )
    if (i+1,j) not in visited and i+1 < h and maze[i+1][j] != '@':    # down
        valid.append( ((i+1,j), 'D') )
    if (i,j-1) not in visited and j-1 >= 0 and maze[i][j-1] != '@':   # left
        valid.append( ((i,j-1), 'L') )
    if (i,j+1) not in visited and j+1 < w and maze[i][j+1] != '@':    # right
        valid.append( ((i,j+1), 'R') )

    return valid

def find_path(maze):
    h = len(maze)
    w = len(maze[0])

    # find start
    start_pos = None
    for i in range(h):
        for j in range(w):
            if maze[i][j] == 'S':
                start_pos = (i,j)
                break

    # bfs to find shortest path. Could switch to dfs if memory is a constraint
    queue = collections.deque()
    visited = set()

    queue.append((start_pos,[]))

    while queue:
        (coods, path) = queue.popleft()
        i, j = coods

        if coods not in visited:
            if maze[i][j] == 'F':  # Goal check
                return "".join(path)

            visited.add(coods)  # Mark visited so we don't redo it

            # Add next squares to explore
            neighbors = _valid_neighbors(i,j,w,h, maze, visited)
            for cood, direction in neighbors:
                tup = (cood, path + [direction])
                queue.append(tup)

    return False, None



maze1 = [
    'S@@@',
    '++++',
    '@@@F'
]

maze1 = [
    '@S@@@@@',
    '@+++++@',
    '@@+@+@@',
    '@++@++@',
    '@@@@+@@',
    '@+++++@',
    '@F@@@@@'
]

lines_to_read = int(input())
maze = []
for i in range(lines_to_read):
    maze.append(input())

print(find_path(maze))