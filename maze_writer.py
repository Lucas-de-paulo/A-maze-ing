from maze_generator import MazeGenerator


class MazeWriter:
    """Write the generated maze to an output file."""
    def __init__(self, generator: MazeGenerator) -> None:
        """Initialize the writer with a maze generator."""
        self.generator = generator

    def path_to_directions(self) -> str:
        """Convert the shortest path into directional instructions."""
        directions = ""
        path = self.generator.find_shortest_path()
        for n in range(len(path) - 1):
            current_tuple = path[n]
            current_row = current_tuple[0]
            current_col = current_tuple[1]

            next_position = path[n + 1]
            next_position_row = next_position[0]
            next_position_col = next_position[1]

            if next_position_row == current_row - 1:
                directions += "N"
            elif next_position_row == current_row + 1:
                directions += "S"
            elif next_position_col == current_col + 1:
                directions += "E"
            elif next_position_col == current_col - 1:
                directions += "W"

        return directions

    def encode_maze(self) -> list[str]:
        """Encode the maze walls as hexadecimal values."""
        encoded_maze = []

        for row in self.generator.maze:
            encoded_row = ""

            for cell in row:
                value = 0

                if cell[0]:
                    value += 1

                if cell[1]:
                    value += 2

                if cell[2]:
                    value += 4

                if cell[3]:
                    value += 8

                encoded_row += format(value, "X")

            encoded_maze.append(encoded_row)

        return encoded_maze

    def write(self, output_file: str) -> None:
        """Write the maze, coordinates, and solution to a file."""
        encoded_maze = self.encode_maze()
        entry_coord = self.generator.entry
        exit_coord = self.generator.exit
        directions = self.path_to_directions()

        try:
            with open(output_file, "w") as file:
                for row in encoded_maze:
                    file.write(row + "\n")

                file.write("\n")
                file.write(f"{entry_coord[1]},{entry_coord[0]}\n")
                file.write(f"{exit_coord[1]},{exit_coord[0]}\n")
                file.write(directions + "\n")
        except OSError as error:
            raise OSError(f"Error in write file {output_file}: {error}")
