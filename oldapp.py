# This was my first attempt before learning object oriented programming.
from amaze_pkg.maze import generate_maze
import random

maze = {0: 1, 1: 4, 2: 1}
junction = 3
position = 0
position_previous = 0
previous = "north"
last_previous = "north"
generate_maze(maze, junction)

while True:
    next_room = {"north": (position + 1), "east": (position + 2), "west":
                 (position + 3), "south": (position + 4), "backtrack": (position - 1)}
    if position == 0:
        print(f"""\nYou are at the entrance the maze. The door has been sealed behind you. You can only move North, or wait.
\n1) Move north
2) Wait""")
        option = input("\nChoose an option: ")
        if option == str(1):
            position_previous = position
            position = next_room["north"]
            previous = "south"
            print(f"""\nYou move north to junction {position}.""")
            continue
        else:
            print(f"""\nYou choose to wait...""")
            continue
    elif position == 1:
        print(f"""\nYou are at the first junction in the maze. You can move in any direction, or wait.
\n1) Move north
2) Move east
3) Move west
4) Move south (Previous Room)
5) Wait""")
        option = input("\nChoose an option: ")
        if option == str(1):
            position_previous = position
            position = next_room["north"]
            last_previous = previous
            previous = "south"
            print(f"""\nYou move north to junction {position}.""")
            continue
        elif option == str(2):
            position_previous = position
            position = next_room["east"]
            last_previous = previous
            previous = "west"
            print(f"""\nYou move east to junction {position}.""")
            continue
        elif option == str(3):
            position_previous = position
            position = next_room["west"]
            last_previous = previous
            previous = "east"
            print(f"""\nYou move west to junction {position}.""")
            continue
        elif option == str(4):
            position_previous = position
            position = next_room["backtrack"]
            last_previous = previous
            previous = "north"
            print(
                f"""\nYou move south to junction {position}, the entrance to the maze.""")
            continue
        else:
            print(f"""\nYou choose to wait...""")
            continue
    elif position >= 2:
        print(
            f"""\nYou are at junction {position}. There is {maze[position]} direction you can move.""")
        if maze[position] == 1:
            print(f"""\n1) Move {previous} (Previous Room)
2) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                position_previous = position
                position = next_room["backtrack"]
                print(f"""\nYou move {previous} to the previous junction.""")
                previous = last_previous
                continue
            else:
                print(f"""\nYou choose to wait...""")
                continue
        if maze[position] == 2:
            if previous == "north":
                print(f"""\n1) Move {previous} (Previous Room)
2) Move south
3) Wait""")
                option = input("\nChoose an option: ")
                if option == str(1):
                    position_previous = position
                    position = next_room["backtrack"]
                    print(
                        f"""\nYou move {previous} to the previous junction.""")
                    previous = last_previous
                    continue
                elif option == str(2):
                    position_previous = position
                    position = next_room["south"]
                    last_previous = previous
                    previous = "north"
                    print(f"""\nYou move south to junction {position}.""")
                    continue
                else:
                    print(f"""\nYou choose to wait...""")
                    continue
            if previous == "east":
                print(f"""\n1) Move {previous} (Previous Room)
2) Move west
3) Wait""")
                option = input("\nChoose an option: ")
                if option == str(1):
                    position_previous = position
                    position = next_room["backtrack"]
                    print(
                        f"""\nYou move {previous} to the previous junction.""")
                    previous = last_previous
                    continue
                elif option == str(2):
                    position_previous = position
                    position = next_room["west"]
                    last_previous = previous
                    previous = "east"
                    print(f"""\nYou move west to junction {position}.""")
                    continue
                else:
                    print(f"""\nYou choose to wait...""")
                    continue
            if previous == "south":
                print(f"""\n1) Move {previous} (Previous Room)
2) Move north
3) Wait""")
                option = input("\nChoose an option: ")
                if option == str(1):
                    position_previous = position
                    position = next_room["backtrack"]
                    print(
                        f"""\nYou move {previous} to the previous junction.""")
                    previous = last_previous
                    continue
                elif option == str(2):
                    position_previous = position
                    position = next_room["north"]
                    last_previous = previous
                    previous = "south"
                    print(f"""\nYou move north to junction {position}.""")
                    continue
                else:
                    print(f"""\nYou choose to wait...""")
                    continue
            if previous == "west":
                print(f"""\n1) Move {previous} (Previous Room)
2) Move east
3) Wait""")
                option = input("\nChoose an option: ")
                if option == str(1):
                    position_previous = position
                    position = next_room["backtrack"]
                    print(
                        f"""\nYou move {previous} to the previous junction.""")
                    previous = last_previous
                    continue
                elif option == str(2):
                    position_previous = position
                    position = next_room["east"]
                    last_previous = previous
                    previous = "west"
                    print(f"""\nYou move east to junction {position}.""")
                    continue
                else:
                    print(f"""\nYou choose to wait...""")
                    continue


# Currently the room one and two work. After that, only rooms with one or two exits work. Need to code
# For rooms with 3 and 4 exits.
