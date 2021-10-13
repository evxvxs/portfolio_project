from random import randrange
from amaze_pkg.maze import generate_maze
from amaze_pkg.rooms import Challenge_Rooms
import random

maze = {0: 1, 1: 4, 2: 4, 3: 4, 4: 4}
junction = 5
player_location = 0
challenge = Challenge_Rooms()
# position_previous = 0
# previous = "north"
# last_previous = "north"


def regenerate():
    generate_maze(maze, junction)
    challenge.current = 0
    challenge.rooms = [0, 1, 2, 3, 4]


class Junction:
    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return f"{self.position=}"


class Junction_Entrance(Junction):
    def __init__(self, position):
        super().__init__(position)
        self.turns = 1
        self.type = "entrance"

    def __repr__(self):
        return f"{self.position=} {self.turns=} {self.type=}"

    def nav(self, player_location, prior, last_player_location, last_prior, doors, explored):
        print(f"""\nYou are at the entrance the maze. The door has been sealed behind you. You can only move North, or wait.
\n1) Move north
2) Wait""")
        option = input("\nChoose an option: ")
        if option == str(1):
            if (player_location + 0.1) not in doors:
                prior = "south"
                last_player_location.append(player_location)
                last_prior.append(prior)
                while player_location in explored:
                    player_location += 1
                doors[last_player_location[-1] + 0.1] = player_location
                explored.append(player_location)

                # For Debug
                print(f"""\nYou move north to junction {player_location}.""")
                return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif (player_location + 0.1) in doors:
                prior = "south"
                last_player_location.append(player_location)
                last_prior.append(prior)
                player_location = doors[(player_location + 0.1)]
                # For Debug
                print(f"""\nYou move north to junction {player_location}.""")
                return player_location, prior, last_player_location, last_prior, doors, explored, False
        else:
            print(f"""\nYou choose to wait...""")
            return player_location, prior, last_player_location, last_prior, doors, explored, True


class Junction_First(Junction):
    def __init__(self, position):
        super().__init__(position)
        self.turns = 4
        self.type = "first junction"

    def __repr__(self):
        return f"{self.position=} {self.turns=} {self.type=}"

    def nav(self, player_location, prior, last_player_location, last_prior, doors, explored):
        print(f"""\nYou are at the first junction in the maze. You can move in any direction, or wait.
\n1) Move north
2) Move east
3) Move west
4) Move south (Previous Room)
5) Wait""")
        option = input("\nChoose an option: ")
        if option == str(1):
            if (player_location + 0.1) not in doors:
                prior = "south"
                last_player_location.append(player_location)
                last_prior.append(prior)
                while player_location in explored:
                    player_location += 1
                doors[last_player_location[-1] + 0.1] = player_location
                explored.append(player_location)

                # For Debug
                print(f"""\nYou move north to junction {player_location}.""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif (player_location + 0.1) in doors:
                prior = "south"
                last_player_location.append(player_location)
                last_prior.append(prior)
                player_location = doors[(player_location + 0.1)]
                # For Debug
                print(f"""\nYou move north to junction {player_location}.""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
        elif option == str(2):
            if (player_location + 0.2) not in doors:
                prior = "west"
                last_player_location.append(player_location)
                last_prior.append(prior)
                while player_location in explored:
                    player_location += 1
                doors[last_player_location[-1] + 0.2] = player_location
                explored.append(player_location)

                # For Debug
                print(f"""\nYou move east to junction {player_location}.""")
                return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif (player_location + 0.2) in doors:
                prior = "west"
                last_player_location.append(player_location)
                last_prior.append(prior)
                player_location = doors[player_location + 0.2]
                # For Debug
                print(f"""\nYou move east to junction {player_location}.""")
                return player_location, prior, last_player_location, last_prior, doors, explored, False
        elif option == str(3):
            if (player_location + 0.3) not in doors:
                prior = "east"
                last_player_location.append(player_location)
                last_prior.append(prior)
                while player_location in explored:
                    player_location += 1
                doors[last_player_location[-1] + 0.3] = player_location
                explored.append(player_location)

                # For Debug
                print(f"""\nYou move west to junction {player_location}.""")
                return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif (player_location + 0.3) in doors:
                prior = "east"
                last_player_location.append(player_location)
                last_prior.append(prior)
                player_location = doors[player_location + 0.3]
                # For Debug
                print(f"""\nYou move west to junction {player_location}.""")
                return player_location, prior, last_player_location, last_prior, doors, explored, False
        elif option == str(4):
            player_location = last_player_location.pop()
            prior = last_prior.pop()
            print(
                f"""\nYou move south to junction {player_location}, the entrance to the maze.""")
            return player_location, prior, last_player_location, last_prior, doors, explored, False
        else:
            print(f"""\nYou choose to wait...""")
            return player_location, prior, last_player_location, last_prior, doors, explored, True


class Junction_1_Turns(Junction):
    def __init__(self, position):
        super().__init__(position)
        self.turns = 1
        self.type = "one turn"

    def __repr__(self):
        return f"{self.position=} {self.turns=} {self.type=}"

    def nav(self, player_location, prior, last_player_location, last_prior, doors, explored):
        print(f"""\nYou are at junction {player_location}. A dead end... There is {self.turns} direction you can move. 
\n1) Move {prior} (Previous Room)
2) Wait""")
        option = input("\nChoose an option: ")
        if option == str(1):
            print(
                f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
            player_location = last_player_location.pop()
            prior = last_prior.pop()
            return player_location, prior, last_player_location, last_prior, doors, explored, True
        else:
            print(f"""\nYou choose to wait...""")
            return player_location, prior, last_player_location, last_prior, doors, explored, True


class Junction_2_Turns(Junction):
    def __init__(self, position):
        super().__init__(position)
        self.turns = 2
        self.type = "two turn"

    def __repr__(self):
        return f"{self.position=} {self.turns=} {self.type=}"

    def nav(self, player_location, prior, last_player_location, last_prior, doors, explored):
        print(explored)
        print(player_location)
        if player_location == explored[-1]:
            challenge.room(random.randrange(0, 5))
        if prior == "north":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move south
3) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
        elif prior == "south":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move north
3) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
        elif prior == "east":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move west
3) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
        elif prior == "west":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move east
3) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True


class Junction_3_Turns(Junction):
    def __init__(self, position):
        super().__init__(position)
        self.turns = 3
        self.type = "three turn"

    def __repr__(self):
        return f"{self.position=} {self.turns=} {self.type=}"

    def nav(self, player_location, prior, last_player_location, last_prior, doors, explored):
        if prior == "north":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move south
3) Move east
4) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(3):
                if (player_location + 0.2) not in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.2] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.2) in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.2)]
                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
        elif prior == "south":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move north
3) Move west
4) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(3):
                if (player_location + 0.2) not in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.2] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.2) in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.2)]
                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
        elif prior == "east":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move west
3) Move north
4) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou west north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(3):
                if (player_location + 0.2) not in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.2] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.2) in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.2)]
                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
        elif prior == "west":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move east
3) Move south
4) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(3):
                if (player_location + 0.2) not in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.2] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.2) in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.2)]
                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, True
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True


class Junction_4_Turns(Junction):
    def __init__(self, position):
        super().__init__(position)
        self.turns = 4
        self.type = "four turn"

    def __repr__(self):
        return f"{self.position=} {self.turns=} {self.type=}"

    def nav(self, player_location, prior, last_player_location, last_prior, doors, explored):
        if prior == "north":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move south
3) Move east
4) Move west
5) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(3):
                if (player_location + 0.2) not in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.2] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.2) in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.2)]
                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(4):
                if (player_location + 0.3) not in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.3] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.3) in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.3)]
                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
        elif prior == "south":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move north
3) Move west
4) Move east
5) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(3):
                if (player_location + 0.2) not in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.2] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.2) in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.2)]
                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(4):
                if (player_location + 0.3) not in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.3] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.3) in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.3)]
                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
        elif prior == "east":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move west
3) Move north
4) Move south
5) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "east"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move west to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(3):
                if (player_location + 0.2) not in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.2] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.2) in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.2)]
                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(4):
                if (player_location + 0.3) not in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.3] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.3) in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.3)]
                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
        elif prior == "west":
            print(f"""\nYou are at junction {player_location}. There is {self.turns} directions you can move.
\n1) Move {prior} (Previous Room)
2) Move east
3) Move south
4) Move north
5) Wait""")
            option = input("\nChoose an option: ")
            if option == str(1):
                print(
                    f"""\nYou move {last_prior[-1]} to junction {last_player_location[-1]}.""")
                player_location = last_player_location.pop()
                prior = last_prior.pop()
                return player_location, prior, last_player_location, last_prior, doors, explored, True
            elif option == str(2):
                if (player_location + 0.1) not in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.1] = player_location
                    explored.append(player_location)
                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.1) in doors:
                    prior = "west"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.1)]
                    # For Debug
                    print(
                        f"""\nYou move east to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(3):
                if (player_location + 0.2) not in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.2] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.2) in doors:
                    prior = "north"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.2)]
                    # For Debug
                    print(
                        f"""\nYou move south to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            elif option == str(4):
                if (player_location + 0.3) not in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    while player_location in explored:
                        player_location += 1
                    doors[last_player_location[-1] + 0.3] = player_location
                    explored.append(player_location)

                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
                elif (player_location + 0.3) in doors:
                    prior = "south"
                    last_player_location.append(player_location)
                    last_prior.append(prior)
                    player_location = doors[(player_location + 0.3)]
                    # For Debug
                    print(
                        f"""\nYou move north to junction {player_location}.""")
                    return player_location, prior, last_player_location, last_prior, doors, explored, False
            else:
                print(f"""\nYou choose to wait...""")
                return player_location, prior, last_player_location, last_prior, doors, explored, True
