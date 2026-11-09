class MazeDisplay:

    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"

    WALL_COLOR = GREEN
    PATH_COLOR = RED

    def __init__(self, maze_generator) -> None:
        self.generator = maze_generator


    def display(
            self, path: list[tuple[int, int]] | None = None
            ) -> None:
        for row in range(self.generator.height):
            top = ""

            for col in range(self.generator.width):
                if self.generator.maze[row][col][self.generator.NORTH]:
                    top += self.WALL_COLOR + "*---" + self.RESET
                else:
                    top += self.WALL_COLOR + "*   " + self.RESET

            top += self.WALL_COLOR + "*" + self.RESET
            print(top)

            middle = ""
            for col in range(self.generator.width):
                if self.generator.maze[row][col][self.generator.WEST]:
                    middle += self.WALL_COLOR + "|" + self.RESET
                else:
                    middle += self.WALL_COLOR + " " + self.RESET

                if (row, col) == self.generator.entry:
                    middle += " S "
                elif (row, col) == self.generator.exit:
                    middle += " E "
                elif (row, col) in self.generator.blocked:
                    middle += " ■ "
                elif path and (row, col) in path:
                    middle += self.PATH_COLOR + " ⬤ " + self.RESET
                else:
                    middle += "   "

            middle += self.WALL_COLOR + "|" + self.RESET
            print(middle)

        bottom = ""
        for col in range(self.generator.width):
            if self.generator.maze[self.generator.height - 1][col][self.generator.SOUTH]:
                bottom += self.WALL_COLOR + "*---" + self.RESET
            else:
                bottom += self.WALL_COLOR + "*   " + self.RESET

        bottom += self.WALL_COLOR + "*" + self.RESET
        print(bottom)
