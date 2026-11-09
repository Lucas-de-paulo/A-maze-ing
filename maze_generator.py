import random
from collections import deque

VERMELHO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[34m"
AMARELO = "\033[33m"
RESET = "\033[0m"

WALL_COLOR = VERDE
PATH_COLOR = VERMELHO

class MazeGenerator:
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
        self.width = width
        self.height = height
        self.entry = (entry[1], entry[0])
        self.exit = (exit[1], exit[0])
        self.perfect = perfect
        self.seed = seed

        self.maze = []
        self.visited = []
        self.blocked: set[tuple[int, int]] = set()

        for row in range(height):
            maze_line = []
            visited_line = []

            for col in range(width):
                maze_line.append([True, True, True, True])
                visited_line.append(False)

            self.maze.append(maze_line)
            self.visited.append(visited_line)

    def get_neighbors(self, row: int, col: int) -> list[tuple[int, int]]:
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

    def get_unvisited_neighbors(self, row: int, col: int) -> list[tuple[int, int]]:
        unvisited = []

        for neighbor in self.get_neighbors(row, col):
            r, c = neighbor

            if not self.visited[r][c] and (r, c) not in self.blocked:
                unvisited.append(neighbor)

        return unvisited

    def get_open_neighbors(
        self, row: int, col: int
    ) -> list[tuple[int, int]]:
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
        stack = []
        row, col = self.entry

        self.place_42()

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
        for row in range(self.height):
            for col in range(self.width):
                if col < self.width - 1:
                    if self.maze[row][col][self.EAST]:
                        if random.choice([True, False]):
                            self.maze[row][col][self.EAST] = False
                            self.maze[row][col + 1][self.WEST] = False

                if row < self.height - 1:
                    if self.maze[row][col][self.SOUTH]:
                        if random.choice([True, False]):
                            self.maze[row][col][self.SOUTH] = False
                            self.maze[row + 1][col][self.NORTH] = False

    def find_shortest_path(self) -> list[tuple[int, int]]:
        queue = deque([self.entry])
        visited = {self.entry}
        came_from = {self.entry: None}

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
        current = self.exit

        while current is not None:
            path.append(current)
            current = came_from[current]

        return path[::-1]

    def encode_maze(self) -> list[str]:
        encoded_maze = []

        for row in self.maze:
            encoded_row = ""

            for cell in row:
                value = 0

                if cell[self.NORTH]:
                    value += 1

                if cell[self.EAST]:
                    value += 2

                if cell[self.SOUTH]:
                    value += 4

                if cell[self.WEST]:
                    value += 8

                encoded_row += format(value, "X")

            encoded_maze.append(encoded_row)

        return encoded_maze

    def place_42(self) -> None:
        x_place = int(self.width / 2)
        y_place = int(self.height / 2)

        self.blocked.add((y_place, x_place - 3))
        self.blocked.add((y_place, x_place - 2))
        self.blocked.add((y_place, x_place - 1))
        self.blocked.add((y_place, x_place + 3))
        self.blocked.add((y_place, x_place + 2))
        self.blocked.add((y_place, x_place + 1))

        self.blocked.add((y_place - 1, x_place - 3))
        self.blocked.add((y_place - 1, x_place + 3))

        self.blocked.add((y_place - 2, x_place - 3))
        self.blocked.add((y_place - 2, x_place + 1))
        self.blocked.add((y_place - 2, x_place + 2))
        self.blocked.add((y_place - 2, x_place + 3))

        self.blocked.add((y_place + 1, x_place - 1))
        self.blocked.add((y_place + 1, x_place + 1))

        self.blocked.add((y_place + 2, x_place - 1))
        self.blocked.add((y_place + 2, x_place + 1))
        self.blocked.add((y_place + 2, x_place + 2))
        self.blocked.add((y_place + 2, x_place + 3))

        print(f"Blocked: {self.blocked}")

    def display(
            self, path: list[tuple[int, int]] | None = None
            ) -> None:
        for row in range(self.height):
            top = ""

            for col in range(self.width):
                if self.maze[row][col][self.NORTH]:
                    top += WALL_COLOR + "*---" + RESET
                else:
                    top += WALL_COLOR + "*   " + RESET

            top += WALL_COLOR + "*" + RESET
            print(top)

            middle = ""
            for col in range(self.width):
                if self.maze[row][col][self.WEST]:
                    middle += WALL_COLOR + "|" + RESET
                else:
                    middle += WALL_COLOR + " " + RESET

                if (row, col) == self.entry:
                    middle += " S "
                elif (row, col) == self.exit:
                    middle += " E "
                elif (row, col) in self.blocked:
                    middle += " ■ "
                elif path and (row, col) in path:
                    middle += PATH_COLOR + " ⬤ " + RESET
                else:
                    middle += "   "

            middle += WALL_COLOR + "|" + RESET
            print(middle)

        bottom = ""
        for col in range(self.width):
            if self.maze[self.height - 1][col][self.SOUTH]:
                bottom += WALL_COLOR + "*---" + RESET
            else:
                bottom += WALL_COLOR + "*   " + RESET

        bottom += WALL_COLOR + "*" + RESET
        print(bottom)
