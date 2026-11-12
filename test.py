
from maze_generator import MazeGenerator

found = []

for seed in range(1000):
    maze = MazeGenerator(
        width=20,
        height=15,
        entry=(0, 0),
        exit=(19, 14),
        perfect=False,
        seed=seed
    )
    maze.generate()

    for row in range(maze.height - 2):
        for col in range(maze.width - 2):
            open_area = True

            for r in range(row, row + 3):
                for c in range(col, col + 2):
                    if maze.maze[r][c][maze.EAST]:
                        open_area = False

            for r in range(row, row + 2):
                for c in range(col, col + 3):
                    if maze.maze[r][c][maze.SOUTH]:
                        open_area = False

            if open_area:
                found.append((seed, row, col))

print("Áreas 3x3 encontradas:", found)
print("Resultado:", "FALHOU" if found else "PASSOU")
