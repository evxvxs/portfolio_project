from amaze_pkg.junctions import Junction, Junction_Entrance, Junction_First, Junction_1_Turns, Junction_2_Turns, Junction_3_Turns, Junction_4_Turns, maze, regenerate
from amaze_pkg.entity import Entity


def main():
    regenerate()
    for jnumber, jturns in maze.items():
        if jnumber == 0:
            globals()['j%s' % jnumber] = Junction_Entrance(jnumber)
        elif jnumber == 1:
            globals()['j%s' % jnumber] = Junction_First(jnumber)
        elif jturns == 1:
            globals()['j%s' % jnumber] = Junction_1_Turns(jnumber)
        elif jturns == 2:
            globals()['j%s' % jnumber] = Junction_2_Turns(jnumber)
        elif jturns == 3:
            globals()['j%s' % jnumber] = Junction_3_Turns(jnumber)
        else:
            globals()['j%s' % jnumber] = Junction_4_Turns(jnumber)
            continue

    return_tuple = ()
    player_location = 0
    last_player_location = []
    prior = "south"
    last_prior = []
    doors = {}
    explored = [0]
    trigger = False
    approach = False
    entity = Entity()
    game_over = False

    while True:
        if player_location == 0:
            """ print(globals()['j%s' % player_location])
            print(prior)
            print(last_prior)
            print(last_player_location)
            print(doors)
            print(explored)
            print(trigger)
            print(approach) """
            # For Debug
            return_tuple = j0.nav(player_location, prior,
                                  last_player_location, last_prior, doors, explored)
            player_location = return_tuple[0]
            prior = return_tuple[1]
            last_player_location = (return_tuple[2])
            last_prior = (return_tuple[3])
            doors = (return_tuple[4])
            explored = (return_tuple[5])
            approach = (return_tuple[6])
            if player_location > 10:
                trigger = True
            game_over = entity.approach(trigger, approach)
            if game_over == True:
                over(player_location)
                break
        elif player_location == 1:
            """ print(globals()['j%s' % player_location])
            print(prior)
            print(last_prior)
            print(last_player_location)
            print(doors)
            print(explored)
            print(trigger)
            print(approach) """
            # For Debug
            return_tuple = j1.nav(player_location, prior,
                                  last_player_location, last_prior, doors, explored)
            player_location = return_tuple[0]
            prior = return_tuple[1]
            last_player_location = (return_tuple[2])
            last_prior = (return_tuple[3])
            doors = (return_tuple[4])
            explored = (return_tuple[5])
            approach = (return_tuple[6])
            if player_location > 10:
                trigger = True
            game_over = entity.approach(trigger, approach)
            if game_over == True:
                over(player_location)
                break
        elif player_location == 50:
            over(player_location)
            break
        else:
            """ print(globals()['j%s' % player_location])
            print(prior)
            print(last_prior)
            print(last_player_location)
            print(doors)
            print(explored)
            print(trigger)
            print(approach) """
            # For Debug
            return_tuple = globals()['j%s' % player_location].nav(
                player_location, prior, last_player_location, last_prior, doors, explored)
            player_location = return_tuple[0]
            prior = return_tuple[1]
            last_player_location = (return_tuple[2])
            last_prior = (return_tuple[3])
            doors = (return_tuple[4])
            explored = (return_tuple[5])
            approach = (return_tuple[6])
            if player_location > 10:
                trigger = True
            game_over = entity.approach(trigger, approach)
            if game_over == True:
                over(player_location)
                break


def over(player_location):
    if player_location == 50:
        print(f"""\nJust as you begin to think the maze will never end, you reach a dead end with a door.
You walk through the doorway, and wake up in your bed in a cold sweat... The nightmare is over.""")
    while True:
        play_again = input("Game over! Play again? (y/n): ")
        if play_again == "y":
            main()
            break
        elif play_again == "n":
            quit()


main()


# The maze is fully functional, or at least as much as it needs to be.
# TODO: Implement challenge rooms.
