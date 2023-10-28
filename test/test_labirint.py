# https://habr.com/ru/companies/hh/articles/769642/
from labirint import walk_it_maze


def test_walk_it_maze():
    # Test 1: Basic test from the original code.
    # There's a wall blocking the direct path, so the optimal path goes around the wall.
    N, M = (3, 3)
    maze = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    assert walk_it_maze(N, M, 0, 0, 2, 0, maze) == 2 # Expected shortest distance: 4

    # Test 2: No obstacles in the maze.
    # The maze is completely open, so the path is direct from start to destination.
    maze = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert walk_it_maze(N, M, 0, 0, 2, 2, maze) == 4  # Expected shortest distance: 4

    # Test 3: Destination is blocked.
    # The destination is surrounded by walls, making it unreachable.
    maze = [[0, 0, 0], [0, 1, 1], [0, 1, 0]]
    assert walk_it_maze(N, M, 0, 0, 2, 2, maze) == -1  # No path available, so expected: -1

    # Test 4: Starting position is the destination.
    # If the starting position and the destination are the same, distance should be 0.
    maze = [[0, 1, 0], [0, 1, 0], [0, 0, 0]]
    assert walk_it_maze(N, M, 1, 1, 1, 1, maze) == 0  # Expected shortest distance: 0

    # Test 5: Larger maze with various paths.
    # The optimal path in this maze zig-zags through the open spaces.
    N, M = (5, 5)
    maze = [[0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]]
    assert walk_it_maze(N, M, 0, 0, 4, 4, maze) == 8  # Expected shortest distance: 8

    print("All tests passed!")

if __name__ == "__main__":
    test_walk_it_maze()

    def debug_the_test():
        N, M = (3, 3)
        x1, y1 = (0, 0)
        x2, y2 = (2, 0)
        maze = [[0, 0, 0], [0, 1, 1], [0, 1, 0]]
        res = walk_it_maze(N, M,x1,y1,x2,y2,maze)
        print(res)
        assert res == 2 # exptected shortest distance 4
    # debug_the_test()
