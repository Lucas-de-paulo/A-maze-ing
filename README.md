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

**MazeWriter**
- `path_to_directions()`: Converts the shortest path into N, E, S and W directions.
- `write()`: Saves the maze and its information to the output file.
- `encode_maze()`: Converts the maze walls into hexadecimal values.

**MazeDisplay**
- `display()`: Renders the maze in the terminal, with colored walls and highlighted elements.

**MazeController**
- `refresh_display()`: Updates the terminal display.
- `show_menu()`: Displays the available actions.
- `regenerate_maze()`: Generates and saves a new maze.
- `set_shortest_path_visibility()`: Shows or hides the shortest path.
- `change_wall_color()`: Changes the wall color.
- `run()`: Controls the interactive menu.

**a_maze_ing.py**
- `main()`: Loads the configuration and coordinates the application.
- `place_42()`: Defines the blocked cells that form the 42 pattern.

## Algorithm

The project uses **Recursive Backtracker**, based on Depth-First Search (DFS), to generate the maze.

The algorithm explores unvisited neighboring cells, removes the walls between connected cells, and uses a stack to backtrack when no unvisited neighbors remain.

We chose this algorithm because it is simple to implement, produces randomized mazes, and naturally generates perfect mazes.

For Pac-Man mode, additional passages are opened to create loops and alternative routes.

**Breadth-First Search (BFS)** is used to calculate the shortest path between the entry and exit. It explores cells level by level using a queue.

## Reusable Module

The `MazeGenerator` class, located in `maze_generator.py`, is designed to be reused independently of the display and controller modules.

It can be imported into other Python projects to generate mazes using the Recursive Backtracker algorithm.

### Basic Usage

Import the class:

```python
from maze_generator import MazeGenerator
```

Create a generator instance:

```python
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

### Parameters

The `MazeGenerator` constructor accepts the following parameters:

| Parameter | Description |
|---|---|
| `width` | Number of columns in the maze. |
| `height` | Number of rows in the maze. |
| `entry` | Entry coordinates `(x, y)`. |
| `exit` | Exit coordinates `(x, y)`. |
| `perfect` | Defines whether the maze is perfect (`True`) or contains additional passages (`False`). |
| `seed` | Optional random seed for reproducible maze generation. |

### Accessing the Generated Maze

The generated maze structure is accessible through the `generator.maze` attribute.

Each cell contains four boolean values representing its walls:

- `0`: North
- `1`: East
- `2`: South
- `3`: West

A value of `True` indicates a closed wall, while `False` indicates an open passage.

To retrieve the shortest path between the entry and exit:

```python
path = generator.find_shortest_path()
print(path)
```

The method returns a list of `(row, column)` coordinates representing the shortest path.

### Installation in Another Project

The reusable module is distributed as a Python package in `.whl` and `.tar.gz` formats.

To install the package in another Python project, use pip:

```bash
python -m pip install ./dist/mazegen_de_pauls-0.1.0-py3-none-any.whl
```

Alternatively, install the source distribution:

```bash
python -m pip install ./dist/mazegen_de_pauls-0.1.0.tar.gz
```

After installation, import and use the class as shown in the Basic Usage section.

### Rebuilding the Package

The package can be rebuilt from the project source using the Python build tool:

```bash
python -m pip install build
python -m build
```

This generates the distribution files inside the `dist/` directory.

The package configuration is defined in `pyproject.toml`.

## Team and Project Management

The project was developed by two students.

***lde-paul***

- Developed the configuration parser and validation logic.

- Implemented the 42 pattern placement and blocked-cell management.

- Developed the main application entry point (a_maze_ing.py).

- Created the Makefile and project license.

- Performed functional testing, debugging, and validation of the application.

***wde-paul***

- Developed the maze generation algorithm and shortest-path calculation.

- Implemented the maze visualization and display functionality.

- Developed the maze output writer and file generation.

- Created the project documentation (README.md).

- Configured the Python package (pyproject.toml) and built the distributable packages (.whl and .tar.gz).

**Planning:** The project was initially divided into independent tasks, followed by module integration, testing, debugging, and documentation. The original plan evolved as implementation and integration revealed additional requirements.

**What worked well:** Dividing responsibilities, separating the code into modules, and testing different maze configurations.

**What could be improved:** Earlier integration between modules could have reduced compatibility issues and rework. More frequent joint testing during development would also have helped identify problems sooner.

**Tools used:** Python, Git, GitHub, Linux Terminal, Make, Flake8, Mypy, and the provided Maze Analyzer.

## Resources

### Articles

- https://www.geeksforgeeks.org/dsa/depth-first-search-or-dfs-for-a-graph/ **dfs algorithm**
- https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/ **bfs algorithm**
- https://www.w3schools.com/dsa/dsa_algo_graphs_traversal.php **dsa algorithm**


- A-Maze-ing project subject and provided Maze Analyzer.

**AI Usage:** AI was used as a learning and development support tool to understand algorithms, discuss implementation approaches, review code, identify bugs, and design tests.
