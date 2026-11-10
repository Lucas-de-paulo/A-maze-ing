import sys
from parser import load_config
from maze_generator import MazeGenerator
from maze_display import MazeDisplay
from maze_controller import MazeController


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    try:
        config = load_config(sys.argv[1])
    except Exception as e:
        print(f"Error {e}")
        sys.exit(1)

    maze = MazeGenerator(
        width=config.width,
        height=config.height,
        entry=config.entry,
        exit=config.exit,
        perfect=config.perfect,
        seed=config.seed
    )

    maze.generate()

    display = MazeDisplay(maze)

    controller = MazeController(maze, display)
    controller.run()


if __name__ == "__main__":
    main()
