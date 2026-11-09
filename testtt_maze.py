from config import load_config
from maze_generator import MazeGenerator


def main() -> None:
    config = load_config("config.txt")

    maze = MazeGenerator(
        width=config.width,
        height=config.height,
        entry=config.entry,
        exit=config.exit,
        perfect=config.perfect,
        seed=config.seed
    )

    print("Largura:", config.width)
    print("Altura:", config.height)
    print("Entrada:", config.entry)
    print("Saída:", config.exit)
    print("Perfect:", config.perfect)

    maze.generate()

    path = maze.find_shortest_path()

    print("Menor caminho:", path)

    maze.display(path)


if __name__ == "__main__":
    main()
