import os

from maze_display import MazeDisplay
from maze_generator import MazeGenerator
from maze_writer import MazeWriter


class MazeController:
    """Manage maze generation, display, and user interactions."""
    def __init__(
            self,
            generator: MazeGenerator,
            display: MazeDisplay,
            writer: MazeWriter,
            output_file: str,
            ) -> None:
        """Initialize the controller with the maze components."""
        self.generator = generator
        self.display = display
        self.writer = writer
        self.output_file = output_file
        self.shortest_path_visibility = True

    def refresh_display(self) -> None:
        """Refresh the terminal and display the current maze."""
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.shortest_path_visibility:
            shortest_path = self.generator.find_shortest_path()
            self.display.display(shortest_path)
        else:
            self.display.display()

    def show_menu(self) -> None:
        """Display the available interaction options."""
        print("=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show / Hide the shortest path")
        print("3. Rotate the wall colours")
        print("4. Quit")

    def regenerate_maze(self) -> None:
        """Generate a new maze and update the output file."""
        self.generator.generate()
        try:
            self.writer.write(self.output_file)
        except OSError as e:
            print((f"Error writing to file {self.output_file}: {e}"))
        self.refresh_display()

    def set_shortest_path_visibility(self) -> None:
        """Toggle the visibility of the shortest path."""
        self.shortest_path_visibility = not self.shortest_path_visibility

        self.refresh_display()

    def change_wall_color(self) -> None:
        """Allow the user to change the maze wall color."""
        print("\n=== Wall color ===")
        print("1. Red")
        print("2. Green")
        print("3. Blue")
        print("4. Yellow")

        try:
            option = input("Choose a color: ")
        except (EOFError, KeyboardInterrupt):
            return

        if option == "1":
            self.display.WALL_COLOR = self.display.RED
        elif option == "2":
            self.display.WALL_COLOR = self.display.GREEN
        elif option == "3":
            self.display.WALL_COLOR = self.display.BLUE
        elif option == "4":
            self.display.WALL_COLOR = self.display.YELLOW
        else:
            print("Invalid option!")
            return

        self.refresh_display()

    def run(self) -> None:
        """Run the interactive maze menu."""
        if self.generator.width < 9 or self.generator.height < 7:
            print("\nSize too small for place 42\n")
        while True:
            self.show_menu()
            try:
                option = input("Choice? (1-4): ")
            except (EOFError, KeyboardInterrupt):
                print("Closed")
                return

            if option == "1":
                try:
                    self.regenerate_maze()
                except (ValueError, EOFError) as e:
                    print(f"It was not possible to regenerate: {e}")
            elif option == "2":
                self.set_shortest_path_visibility()
            elif option == "3":
                self.change_wall_color()
            elif option == "4":
                print("Exiting maze...")
                break
            else:
                print("\nInvalid option!\n")
