from parser import load_config
from maze_generator import MazeGenerator
from maze_display import MazeDisplay


def main() -> None:
    config = load_config("config.txt")

    generator = MazeGenerator(
        width=config.width,
        height=config.height,
        entry=config.entry,
        exit=config.exit,
        perfect=config.perfect,
        seed=config.seed
    )

    generator.generate()

    display = MazeDisplay(generator)

    path = generator.find_shortest_path()

    display.display(path)


if __name__ == "__main__":
    main()