*This project has been created as part of the 42 curriculum by wde-paul, lde-paul.*

# A-Maze-ing

## Description

A-Maze-ing is a Python project that generates random mazes based on a configuration file.

The project supports two generation modes:

- **Perfect Maze:** A maze with no loops and exactly one possible path between connected cells.
- **Pac-Man Mode:** A fully connected maze with multiple routes and few dead ends.

The maze includes the 42 pattern, a calculated shortest path, and an interactive terminal display.

## Instructions

**Requirements:** Python 3.10+, pip and Make.

Clone the repository and enter the project directory:

```bash
git clone <REPOSITORY_URL>
cd A-maze-ing
```

Install the development tools:

```bash
make install
```

Run the project:

```bash
make run
```

Or execute it directly:

```bash
python3 a_maze_ing.py config.txt
```

**Available Make commands:**

| Command | Description |
|---|---|
| `make install` | Install development tools. |
| `make run` | Run the project. |
| `make debug` | Run with Python debugger. |
| `make clean` | Remove temporary files and caches. |
| `make lint` | Run Flake8 and Mypy. |
| `make lint-strict` | Run stricter type checks. |

## Configuration File

The project uses a `config.txt` file with one `KEY=VALUE` pair per line. Lines starting with `#` are ignored.

| Key | Description | Example |
|---|---|---|
| `WIDTH` | Number of columns. | `WIDTH=20` |
| `HEIGHT` | Number of rows. | `HEIGHT=15` |
| `ENTRY` | Entry coordinates `(x,y)`. | `ENTRY=0,0` |
| `EXIT` | Exit coordinates `(x,y)`. | `EXIT=19,14` |
| `OUTPUT_FILE` | Output filename. | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | Selects the generation mode. | `PERFECT=False` |
| `SEED` | Optional seed for reproducibility. | `SEED=42` |

Example:

```ini
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=False
SEED=42
```

The parser validates the configuration, including required values, data types, dimensions, and entry and exit coordinates. The `SEED` parameter is optional.

## Project Structure

The project is divided into modules, each with a specific responsibility:

| File | Responsibility |
|---|---|
| `a_maze_ing.py` | Main entry point. Loads the configuration and connects the project modules. |
| `parser.py` | Reads and validates the configuration file. |
| `maze_generator.py` | Contains the `MazeGenerator` class and maze generation logic. |
| `maze_display.py` | Displays the maze, entry, exit, 42 pattern, and shortest path in the terminal. |
| `maze_writer.py` | Encodes the maze in hexadecimal format and saves the output file. |
| `maze_controller.py` | Handles the interactive menu and user actions. |
| `config.txt` | Stores the maze generation parameters. |

### Main Methods

**MazeGenerator**
- `generate()`: Generates the maze using Recursive Backtracker.
- `get_neighbors()`: Finds neighboring cells.
- `get_unvisited_neighbors()`: Finds unvisited neighbors.
- `get_open_neighbors()`: Finds accessible neighboring cells.
- `create_loops()`: Opens additional passages in Pac-Man mode.
- `find_shortest_path()`: Calculates the shortest path using BFS.
- `encode_maze()`: Converts the maze into hexadecimal representation.
- `place_42()`: Defines the closed cells that form the 42 pattern.

**MazeWriter**
- `path_to_directions()`: Converts the shortest path into N, E, S and W directions.
- `write()`: Saves the maze and its information to the output file.

**MazeDisplay**
- `display()`: Renders the maze in the terminal, with colored walls and highlighted elements.

**MazeController**
- `refresh_display()`: Updates the terminal display.
- `show_menu()`: Displays the available actions.
- `regenerate_maze()`: Generates and saves a new maze.
- `set_shortest_path_visibility()`: Shows or hides the shortest path.
- `change_wall_color()`: Changes the wall color.
- `run()`: Controls the interactive menu.

## Algorithm

The project uses **Recursive Backtracker**, based on Depth-First Search (DFS), to generate the maze.

The algorithm explores unvisited neighboring cells, removes the walls between connected cells, and uses a stack to backtrack when no unvisited neighbors remain.

We chose this algorithm because it is simple to implement, produces randomized mazes, and naturally generates perfect mazes.

For Pac-Man mode, additional passages are opened to create loops and alternative routes.

**Breadth-First Search (BFS)** is used to calculate the shortest path between the entry and exit. It explores cells level by level using a queue.

## Reusable Module

The `MazeGenerator` class, located in `maze_generator.py`, is designed to be reused independently of the display and controller modules.

Basic usage:

```python
from maze_generator import MazeGenerator

generator = MazeGenerator(
    width=20,
    height=15,
    entry=(0, 0),
    exit=(19, 14),
    perfect=True,
    seed=42
)

generator.generate()
```

Custom parameters allow users to define maze dimensions, entry, exit, generation mode, and random seed.

The generated structure is accessible through `generator.maze`.

The shortest path can be obtained using:

```python
path = generator.find_shortest_path()
```

The reusable module is packaged as `mazegen-*` and distributed as a `.whl` or `.tar.gz` file. The repository includes the required sources to rebuild the package.

## Team and Project Management

The project was developed by two students.

**[LOGIN_1]**
- [Describe actual responsibilities.]

**[LOGIN_2]**
- [Describe actual responsibilities.]

**Planning:** The project was initially divided into independent tasks, followed by module integration, testing, debugging, and documentation. The original plan evolved as implementation and integration revealed additional requirements.

**What worked well:** Dividing responsibilities, separating the code into modules, and testing different maze configurations.

**Tools used:** Python, Git, GitHub, Linux Terminal, Make, Flake8, Mypy, and the provided Maze Analyzer.

## Resources

- A-Maze-ing project subject and provided Maze Analyzer.

**AI Usage:** AI was used as a learning and development support tool to understand algorithms, discuss implementation approaches, review code, identify bugs, and design tests.

---

**A-Maze-ing — This is the way.**
