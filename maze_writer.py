from maze_generator import MazeGenerator


class MazeWriter:
    def __init__(self, generator: MazeGenerator) -> None:
        self.generator = generator


    def path_to_directions(self) -> str:
        directions = ""
        path = self.generator.find_shortest_path()
        for n in range(len(path) - 1):
            current_tuple = path[n]
            current_row = current_tuple[0]
            current_col = current_tuple[1]

            next_position  = path[n + 1]
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

    def write(self, output_file: str) -> None:
        encoded_maze = self.generator.encode_maze()
        entry_coord = self.generator.entry
        exit_coord = self.generator.exit
        directions = self.path_to_directions()

        with open(output_file, "w") as file:
            for row in encoded_maze:
                file.write(row + "\n")

            file.write("\n")
            file.write(f"{entry_coord[1]},{entry_coord[0]}\n")
            file.write(f"{exit_coord[1]},{exit_coord[0]}\n")
            file.write(directions + "\n")