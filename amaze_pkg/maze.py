import random


def generate_maze(maze, junction):
    input(f"""\nWelcome to AMAZE
Press enter to begin """)
    while junction < 32:
        maze[junction] = random.randint(1, 4)
        junction = junction + 1
    for jnumber, jturns in maze.items():
        print(f"""Junction #{jnumber} has {jturns} turns.""")
        # For debug
    input(f"""\nThe last thing you can remember is falling asleep in your bed. You're not sure how you
got here, but you are falling into a dark abyss. This is initially terrifying,
but after falling for what seems like hours, you start to drift off. Eventually,
you see a dim light in the distance, which grows bigger as you rapidly approach
until light consumes your field of vision.

You are thrurst forward into a doorway where you land quite suddenly, uninjured,
on your feet. You hear a slam from behind, where the door that you entered through
closes abruptly. There are strange shifting symbols on the floor at your feet.
Although they are shifting and you don't recognize the language, you understand
somehow that it says "AMAZE" While your surroundings seem to be stable and
unchanging, something doesn't feel right. You can feel the floor shifting beneath
you...

You notice you have a compass in your right hand. It indicates that the hallway
proceeding in front of you heads north.

Press enter to continue """)
