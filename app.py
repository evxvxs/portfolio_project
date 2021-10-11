from amaze_pkg.junctions import Junction, Junction_Entrance, Junction_First, Junction_1_Turns, Junction_2_Turns, Junction_3_Turns, Junction_4_Turns, maze

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

while True:
    if player_location == 0:
        print(globals()['j%s' % player_location])
        print(prior)
        print(last_prior)
        print(last_player_location)
        print(doors)
        print(explored)
        # For Debug
        return_tuple = j0.nav(player_location, prior,
                              last_player_location, last_prior, doors, explored)
        player_location = return_tuple[0]
        prior = return_tuple[1]
        last_player_location = (return_tuple[2])
        last_prior = (return_tuple[3])
        doors = (return_tuple[4])
        explored = (return_tuple[5])
    elif player_location == 1:
        print(globals()['j%s' % player_location])
        print(prior)
        print(last_prior)
        print(last_player_location)
        print(doors)
        print(explored)
        # For Debug
        return_tuple = j1.nav(player_location, prior,
                              last_player_location, last_prior, doors, explored)
        player_location = return_tuple[0]
        prior = return_tuple[1]
        last_player_location = (return_tuple[2])
        last_prior = (return_tuple[3])
        doors = (return_tuple[4])
        explored = (return_tuple[5])
    else:
        print(globals()['j%s' % player_location])
        print(prior)
        print(last_prior)
        print(last_player_location)
        print(doors)
        print(explored)
        # For Debug
        return_tuple = globals()['j%s' % player_location].nav(
            player_location, prior, last_player_location, last_prior, doors, explored)
        player_location = return_tuple[0]
        prior = return_tuple[1]
        last_player_location = (return_tuple[2])
        last_prior = (return_tuple[3])
        doors = (return_tuple[4])
        explored = (return_tuple[5])

# The maze is fully functional, or at least as much as it needs to be.
# TODO: Implement entity. Implement challenge rooms. Implement Victory Conditions. Implement quit and restart options.
