import random
from collections import deque


class MazeGenerator:
    """Generate and manage mazes"""
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __init__(
            self,
            width: int,
            height: int,
            entry: tuple[int, int],
            exit: tuple[int, int],
            perfect: bool,
            seed: int | None = None,
            ) -> None:
        """Initialize the maze generator with the given parameters."""
        self.width = width
        self.height = height
        self.entry = (entry[1], entry[0])
        self.exit = (exit[1], exit[0])
        self.perfect = perfect
        self.seed = seed

        self.maze: list[list[list[bool]]] = []
        self.visited: list[list[bool]] = []
        self.blocked: set[tuple[int, int]] = set()

        if self.seed is not None:
            random.seed(self.seed)

        for row in range(height):
            maze_line = []
            visited_line = []

            for col in range(width):
                maze_line.append([True, True, True, True])
                visited_line.append(False)

            self.maze.append(maze_line)
            self.visited.append(visited_line)

    def get_neighbors(self, row: int, col: int) -> list[tuple[int, int]]:
        """Return all valid neighboring cells."""
        neighbors = []

        if row - 1 >= 0:
            neighbors.append((row - 1, col))

        if row + 1 < self.height:
            neighbors.append((row + 1, col))

        if col + 1 < self.width:
            neighbors.append((row, col + 1))

        if col - 1 >= 0:
            neighbors.append((row, col - 1))

        return neighbors

    def get_unvisited_neighbors(
            self,
            row: int, col: int
            ) -> list[tuple[int, int]]:
        """Return neighboring cells that have not been visited or blocked."""
        unvisited = []

        for neighbor in self.get_neighbors(row, col):
            r, c = neighbor

            if not self.visited[r][c] and (r, c) not in self.blocked:
                unvisited.append(neighbor)

        return unvisited

    def get_open_neighbors(
        self, row: int, col: int
    ) -> list[tuple[int, int]]:
        """Return neighboring cells connected by open passages."""
        neighbors = []

        if row > 0 and not self.maze[row][col][self.NORTH]:
            neighbors.append((row - 1, col))

        if col < self.width - 1 and not self.maze[row][col][self.EAST]:
            neighbors.append((row, col + 1))

        if row < self.height - 1 and not self.maze[row][col][self.SOUTH]:
            neighbors.append((row + 1, col))

        if col > 0 and not self.maze[row][col][self.WEST]:
            neighbors.append((row, col - 1))

        return neighbors

    def generate(self) -> None:
        """Generate the maze using the recursive backtracking algorithm."""
        self.maze = [
            [[True, True, True, True] for _ in range(self.width)]
            for _ in range(self.height)
        ]

        self.visited = [
            [False for _ in range(self.width)]
            for _ in range(self.height)
        ]

        stack = []
        row, col = self.entry

        self.visited[row][col] = True
        stack.append((row, col))

        while stack:
            neighbors = self.get_unvisited_neighbors(row, col)

            if neighbors:
                next_row, next_col = random.choice(neighbors)

                if next_row == row - 1:
                    self.maze[row][col][self.NORTH] = False
                    self.maze[next_row][next_col][self.SOUTH] = False

                elif next_row == row + 1:
                    self.maze[row][col][self.SOUTH] = False
                    self.maze[next_row][next_col][self.NORTH] = False

                elif next_col == col + 1:
                    self.maze[row][col][self.EAST] = False
                    self.maze[next_row][next_col][self.WEST] = False

                elif next_col == col - 1:
                    self.maze[row][col][self.WEST] = False
                    self.maze[next_row][next_col][self.EAST] = False

                self.visited[next_row][next_col] = True
                stack.append((next_row, next_col))
                row, col = next_row, next_col

            else:
                stack.pop()

                if stack:
                    row, col = stack[-1]

        if not self.perfect:
            self.create_loops()

    def create_loops(self) -> None:
        """Create additional passages to produce loops in the maze."""
        for row in range(self.height):
            for col in range(self.width):
                if (row, col) in self.blocked:
                    continue

                if self.maze[row][col].count(True) == 3:
                    if (
                        row > 0
                        and (row - 1, col) not in self.blocked
                        and self.maze[row][col][self.NORTH]
                    ):
                        self.maze[row][col][self.NORTH] = False
                        self.maze[row - 1][col][self.SOUTH] = False

                    elif (
                        row < self.height - 1
                        and (row + 1, col) not in self.blocked
                        and self.maze[row][col][self.SOUTH]
                    ):
                        self.maze[row][col][self.SOUTH] = False
                        self.maze[row + 1][col][self.NORTH] = False

                    elif (
                        col < self.width - 1
                        and (row, col + 1) not in self.blocked
                        and self.maze[row][col][self.EAST]
                    ):
                        self.maze[row][col][self.EAST] = False
                        self.maze[row][col + 1][self.WEST] = False

                    elif (
                        col > 0
                        and (row, col - 1) not in self.blocked
                        and self.maze[row][col][self.WEST]
                    ):
                        self.maze[row][col][self.WEST] = False
                        self.maze[row][col - 1][self.EAST] = False

    def find_shortest_path(self) -> list[tuple[int, int]]:
        """Find the shortest path between entry and exit using BFS."""
        queue = deque([self.entry])
        visited = {self.entry}
        came_from: dict[
            tuple[int, int],
            tuple[int, int] | None
            ] = {self.entry: None}

        while queue:
            current = queue.popleft()

            if current == self.exit:
                break

            row, col = current

            for neighbor in self.get_open_neighbors(row, col):
                if neighbor not in visited:
                    visited.add(neighbor)
                    came_from[neighbor] = current
                    queue.append(neighbor)

        if self.exit not in came_from:
            return []

        path = []
        path_current: tuple[int, int] | None = self.exit

        while path_current is not None:
            path.append(path_current)
            path_current = came_from[path_current]

        return path[::-1]
