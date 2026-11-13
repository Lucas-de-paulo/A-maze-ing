"""Main entry point for the A-Maze-ing project."""

import sys
from parser import load_config
from maze_generator import MazeGenerator
from maze_display import MazeDisplay
from maze_controller import MazeController
from maze_writer import MazeWriter


def main() -> None:
    """Load configuration, generate, save, and display the maze."""
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    try:
        config = load_config(sys.argv[1])
    except ValueError as e:
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

    try:
        maze.generate()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    writer = MazeWriter(maze)

    try:
        writer.write(config.output_file)
    except OSError as error:
        print(f"Error: {error}")
        sys.exit(1)

    display = MazeDisplay(maze)
    controller = MazeController(maze, display, writer, config.output_file)
    controller.refresh_display()
    controller.run()


if __name__ == "__main__":
    main()
