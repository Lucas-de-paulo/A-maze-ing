import random


class MazeGenerator:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.maze = []
        self.visited = []

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

            if not self.visited[r][c]:
                unvisited.append(neighbor)

        return unvisited


    def generate(self) -> None:
        stack = []
        row = 0
        col = 0

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


    def display(self) -> None:
        for row in range(self.height):
            top = ""

            for col in range(self.width):
                if self.maze[row][col][self.NORTH]:
                    top += "*---"
                else:
                    top += "*   "

            top += "*"
            print(top)
            middle = ""

            for col in range(self.width):
                if self.maze[row][col][self.WEST]:
                    middle += "|"
                else:
                    middle += " "

                middle += "   "

            middle += "|"
            print(middle)
        bottom = ""

        for col in range(self.width):
            if self.maze[self.height - 1][col][self.SOUTH]:
                bottom += "*---"
            else:
                bottom += "+   "

        bottom += "*"
        print(bottom)