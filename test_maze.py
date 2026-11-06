from maze_generator import MazeGenerator

maze = MazeGenerator(20,15,(0,0),(19,14),True,42)

print(f"Visited = {maze.visited}\n\nLabirinto criado {maze.maze}")
print(f"Visited = {maze.visited}")

maze.generate()

path = maze.find_shortest_path()
print("Menor caminho:", path)

print("\n=== Visited após generate(): ===")
print(maze.visited)

print("\n=== Labirinto após generate(): ===")
print(maze.maze)

print("Entrada:", maze.entry)
print("Célula inicial visitada:", maze.visited[1][1])
print("Todas as células visitadas:", all(
    all(row) for row in maze.visited
))

maze.display()
maze.display(path)
