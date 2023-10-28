from collections import deque
import math

def is_valid(x, y, N, M, maze):
    """check to not wall and coords inside the maze"""
    if 0 <= x < M and 0 <= y < N:
        return maze[x][y] == 0
    else:
        return False

def walk_it_maze(N, M, x1, y1, x2, y2, maze):
    coords = [(x1, y1, 0)]
    queue = deque(coords)  # each element of the queue is a tuple (x, y, distance)
    visited = [[False for _ in range(N)] for _ in range(M)]
    visited[x1][y1] = True  # mark the starting point as visited

    # directions for movement (left, right, up, down)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        x, y, distance = queue.popleft()

        if (x == x2) and (y == y2):  # if we've reached the destination
            return distance

        for dx, dy in directions:
            newx, newy = x + dx, y + dy
            if is_valid(newx, newy, N, M, maze) and not visited[newx][newy]:
                visited[newx][newy] = True
                queue.append((newx, newy, distance + 1))

    return -1  # return -1 if no path is found




if __name__ == "__main__":
    N, M = (3, 3)
    x1, y1 = (0, 0)
    x2, y2 = (2, 0)
    maze = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    print(walk_it_maze(N,M,x1,y1,x2,y2,maze))
