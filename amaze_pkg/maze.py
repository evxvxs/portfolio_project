import random


def generate_maze(maze, junction):
    while junction < 100:
        maze[junction] = random.randint(1, 4)
        junction = junction + 1
    for jnumber, jturns in maze.items():
        print(f"""Junction #{jnumber} has {jturns} turns.""")
    input("Press enter to continue")
