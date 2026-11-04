from maze_generator import MazeGenerator

maze = MazeGenerator(3,4)

print(f"Visited = {maze.visited}\n\nLabirinto criado {maze.maze}")
print(f"Visited = {maze.visited}")

maze.generate()

print("\n=== Visited após generate(): ===")
print(maze.visited)

print("\n=== Labirinto após generate(): ===")
print(maze.maze)

display = maze.display()
print(f"Retorno de display = {display}")
encode_maze = maze.encode_maze()
print(f"Retorno de encode_maze = {encode_maze}")
generate = maze.generate()
print(f"Retorno de generate = {generate}")
get_neighbors = maze.get_neighbors
get_unvisited_neighbors = maze.get_unvisited_neighbors(0,0)
print(f"Retorno de get_neighbors = {get_unvisited_neighbors}")



