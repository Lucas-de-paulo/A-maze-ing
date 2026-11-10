from maze_display import MazeDisplay
from maze_generator import MazeGenerator
import os

class MazeController:
    def __init__(self, generator: MazeGenerator, display: MazeDisplay) -> None:
        self.generator = generator
        self.display = display
        self.shortest_path_visibility = True

    def refresh_display(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.shortest_path_visibility:
            shortest_path = self.generator.find_shortest_path()
            self.display.display(shortest_path)
        else:
            self.display.display()

    def show_menu(self) -> None:
        print("\n=== MAZE CONTROLLER ===")
        print("1. generate maze")
        print("2. Set shortest path visibility")
        print("3. Change wall color")
        print("4. Exit")

    def regenerate_maze(self) -> None:
        self.generator.generate()

        self.refresh_display()

    def set_shortest_path_visibility(self) -> None:
        self.shortest_path_visibility = not self.shortest_path_visibility

        self.refresh_display()

    def change_wall_color(self) -> None:
        print("\n=== Wall color ===")
        print("1. Red")
        print("2. Green")
        print("3. Blue")
        print("4. Yellow")

        option = input("Choose a color: ")

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
        while True:
            self.show_menu()
            option = input("Choose an option: ")

            if option == "1":
                self.regenerate_maze()
            elif option == "2":
                self.set_shortest_path_visibility()
            elif option == "3":
                self.change_wall_color()
            elif option == "4":
                print("Exiting maze...")
                break
            else:
                print("Invalid option!")
